import os
import errno
import logging
import shutil

from ..storage import Storage

logger = logging.getLogger(__name__)


class LocalStorage(Storage):
    def __init__(self, root_dir='test', schema='schema'):
        super(Storage, self).__init__()
        self.streamable = True
        self.root_dir = root_dir
        self.schema = schema

        try:
            os.makedirs(root_dir)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(root_dir):
                pass
            else:
                logger.exception(exc)
                raise exc

    def get(self, path):
        with open(os.path.join(self.root_dir, path), 'r') as f:
            return f.read()

    def exists(self, path):
        return os.path.isfile(os.path.join(self.root_dir, path))

    def save(self, path, lines):
        with open(os.path.join(self.root_dir, path), 'a') as f:
            for line in lines:
                f.write(line)

    def mkdir(self, path):
        try:
            os.mkdir(os.path.join(self.root_dir, path))
        except OSError:
            pass

    def get_dirs(self):
        return os.listdir(self.root_dir)

    def get_files(self, path):
        def _file_getctime(filename):
            return os.path.getctime(os.path.join(self.root_dir, path, filename))

        return sorted(os.listdir(os.path.join(self.root_dir, path)), key=_file_getctime)

    def move(self, source, dest):
        shutil.move(os.path.join(self.root_dir, source), os.path.join(self.root_dir, dest))

    def join(self, *paths):
        return os.path.join(*paths)

