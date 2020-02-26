import datetime
import re
from collections import OrderedDict
import sys
import requests
import logging
import tempfile
import csv
import errno

from .storages import LocalStorage

logger = logging.getLogger(__name__)


class Historifier(object):
    def __init__(self, domain_id, dataset_id, apikey=None, api_version="2", storage=None, delimiter=u';', schema_name=None,
                 time_format=None, timestamp_fieldname="timestamp", dirname_scheme=None, filename_scheme=None):
        if storage is None:
            storage = LocalStorage()
        if schema_name is None:
            schema_name = 'schema'
        if time_format is None:
            time_format = '%Y-%m-%d'
        if dirname_scheme is None:
            dirname_scheme = '{}#{}'
        if filename_scheme is None:
            filename_scheme = '{}-{}.csv'

        if api_version == "1":
            self.base_url = 'https://{}.opendatasoft.com/api/records/1.0/download/?dataset={}'.format(domain_id, dataset_id)
        elif api_version == "2":
            self.base_url = 'https://{}.opendatasoft.com/api/v2/catalog/datasets/{}/'.format(domain_id, dataset_id)
        else:
            raise ValueError("API Version '%s' not recognized, currently supporting API Version 1 and 2" % api_version)

        self.domain_id = domain_id
        self.dataset_id = dataset_id
        self.apikey = apikey
        self.api_version = api_version
        self.storage = storage
        self.delimiter = delimiter.encode()
        self.schema_name = schema_name
        self.time_format = time_format
        self.timestamp_fieldname = timestamp_fieldname.encode()
        self.dirname_scheme = dirname_scheme
        self.filename_scheme = filename_scheme
        self.append_dir = 'current'
        self.histo_dir = 'archive'

    def fetch_records(self):
        fetch_time = self.get_time()

        if self.api_version == "1":
            r = requests.get(self.base_url, stream=True, timeout=90, params={
                'apikey': self.apikey,
                'csv_separator': self.delimiter,
                'format':'csv',
                'use_labels_for_header':'false'
            })
        elif self.api_version == "2":
            r = requests.get(self.base_url + 'exports/csv', stream=True, timeout=90, params={
                'apikey': self.apikey,
                'delimiter': self.delimiter,
                'list_separator': ','
            })

        r.raise_for_status()

        if len(r.content.strip()) <= 0: # empty result
            raise ValueError("Empty dataset or wrong request: the output is empty (no schema)")

        tmp_f = self.get_temp_file()
        lines = r.iter_lines(chunk_size=1024)
        for i, line in enumerate(lines):
            if i == 0:
                line += '%s%s' % (self.delimiter, self.timestamp_fieldname)
            else:
                line += '%s%s' % (self.delimiter, fetch_time.isoformat())
            tmp_f.write(line + '\n')

        return tmp_f, fetch_time

    def fetch_aggregations(self, select=None, where=None, group_by=None, map_on=None):
        fetch_time = self.get_time()
        tmp_f = self.get_temp_file()

        aggregations = []

        if map_on:
            r = requests.get(self.base_url + 'aggregates', stream=True, timeout=30, params={
                'select': map_on,
                'group_by': map_on,
                'apikey': self.apikey
            })

            r.raise_for_status()

            jobs = [aggregation[map_on] for aggregation in r.json()['aggregations']]
            for i, job in enumerate(jobs):
                map_where = map_on + '=' + str(job)
                if where:
                    map_where = map_where + ' AND ' + where

                aggregations.extend(self._fetch_aggregations(select=select, where=map_where, group_by=group_by))
        else:
            aggregations = self._fetch_aggregations(select=select, where=where, group_by=group_by)

        if not aggregations:
            return None, None

        keys = aggregations[0].keys()
        writer = csv.DictWriter(tmp_f, fieldnames=OrderedDict([(key, None) for key in (keys + [self.timestamp_fieldname])]),
                                delimiter=self.delimiter)
        writer.writeheader()
        writer.writerows([dict([(self.timestamp_fieldname, fetch_time.isoformat())], **aggregation) for aggregation in aggregations])
        return tmp_f, fetch_time

    def _fetch_aggregations(self, select=None, where=None, group_by=None):
        r = requests.get(self.base_url + 'aggregates', stream=True, timeout=30, params={
            'select': select,
            'where': where,
            'group_by': group_by,
            'apikey': self.apikey
        })

        r.raise_for_status()

        aggregations = r.json()['aggregations']
        return aggregations

    def save(self, temp_f, fetch_time):
        temp_f.seek(0)
        schema = temp_f.readline()

        stored_schema = self.get_schema()
        if stored_schema is None:
            self.save_schema(schema)
        elif not self.schema_equals(stored_schema, schema, self.delimiter):
            self.mkdir_dataset()
            self.save_schema(schema)

        temp_f.seek(0)
        if self.is_appending(fetch_time):
            temp_f.seek(len(temp_f.readline()))

        self.save_records(temp_f, fetch_time)

    def get_dataset_dirs(self):
        return sorted(
                list(
            filter(re.compile(self.dirname_scheme.format(self.dataset_id, '\d*')).search, self.storage.get_dirs())),
            key=lambda x: x[-1])

    def get_dataset_dir(self):
        dirs = self.get_dataset_dirs()
        if len(dirs) == 0:
            return self.mkdir_dataset()

        dataset_dir = dirs[-1]
        append_path = self.storage.join(dataset_dir, self.append_dir)
        if not self.storage.exists(append_path):
            self.storage.mkdir(append_path)
        histo_path = self.storage.join(dataset_dir, self.histo_dir)
        if not self.storage.exists(histo_path):
            self.storage.mkdir(histo_path)

        return dataset_dir

    def get_new_dataset_dirname(self):
        return self.dirname_scheme.format(self.dataset_id, len(self.get_dataset_dirs()))

    def mkdir_dataset(self):
        dirname = self.get_new_dataset_dirname()
        self.storage.mkdir(dirname)
        self.storage.mkdir(self.storage.join(dirname, self.append_dir))
        self.storage.mkdir(self.storage.join(dirname, self.histo_dir))
        return dirname

    def is_appending(self, fetch_time):
        if self.storage.exists(
                self.storage.join(self.get_dataset_dir(), self.append_dir, self.get_resource_name(fetch_time))):
            return True
        files = self.storage.get_files(self.storage.join(self.get_dataset_dir(), self.append_dir))
        for file in files:
            self.storage.move(self.storage.join(self.get_dataset_dir(), self.append_dir, file),
                              self.storage.join(self.get_dataset_dir(), self.histo_dir, file))
        return False

    def get_schema(self):
        try:
            return self.storage.get(self.storage.join(self.get_dataset_dir(), self.to_schema_name()))
        except IOError as e:
            if e.errno != errno.ENOENT:
                logger.exception(e)
                sys.exit(1)
            return None

    def to_schema_name(self):
        return self.filename_scheme.format(self.dataset_id, self.schema_name)

    def get_resource_name(self, fetch_time):
        return self.filename_scheme.format(self.format_time(fetch_time), self.dataset_id)

    def format_time(self, fetch_time):
        return fetch_time.strftime(self.time_format)

    def save_schema(self, schema):
        self.storage.save(self.storage.join(self.get_dataset_dir(), self.to_schema_name()), schema)

    def save_records(self, records, fetch_time):
        self.storage.save(
            self.storage.join(self.get_dataset_dir(), self.append_dir, self.get_resource_name(fetch_time)), records)

    @staticmethod
    def get_temp_file():
        return tempfile.SpooledTemporaryFile(mode='w+', max_size=1024 * 32)

    @staticmethod
    def schema_equals(a, b, sep):
        a = a.strip()
        b = b.strip()

        if sep is None: # can't be... we must know it to compare schemas
            return False
        if not isinstance(a, list):
            a = a.split(sep)
        if not isinstance(b, list):
            b = b.split(sep)
        return len(set(a)-set(b)) <= 0

    @staticmethod
    def get_time():
        return datetime.datetime.utcnow()
