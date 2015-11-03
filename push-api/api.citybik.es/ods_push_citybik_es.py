# -*- coding:utf-8 -*-

from StringIO import StringIO
import datetime

__author__ = 'fpassaniti'

import ijson
import requests
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

''' PUSH '''
DOMAIN=' YOUR OPENDATASOFT DOMAIN HERE !!! '
PUSH_OR_API_LEY=' YOUR API KEY HERE !!! '
push_base_url = 'http://%s/api/push/1.0/pastedtext/realtime0/push/?pushkey=%s'%(DOMAIN,PUSH_OR_API_LEY)

''' GET '''
get_base_url = "http://api.citybik.es"
networks_url = "/v2/networks"
ijson_networks_rule = "networks"
ijson_stations_rule = "network.stations"

get_ret = requests.get(get_base_url + networks_url)

if get_ret.status_code != 200:
    print "GET CityBik error, code %d, msg %s"%(get_ret.status_code,get_ret.reason)
    exit

for networks in ijson.items(StringIO(get_ret.content), ijson_networks_rule):
    for network in networks:
        href = network['href']

        station_ret = requests.get(get_base_url + href)
        if station_ret.status_code == 200:

            push_list = list()

            for stations in ijson.items(StringIO(station_ret.content), ijson_stations_rule):
                for station in stations:
                    station['network_name'] = network['name']
                    station['network_location'] = json.dumps(network['location'], cls=DecimalEncoder)
                    station['network_company'] = network['company']
                    station['extra'] = json.dumps(station['extra'], cls=DecimalEncoder)
                    station['geo'] = "%f, %f" % (station['latitude'], station['longitude'])

                    push_list.append(station)

            ret = requests.post(push_base_url, data=json.dumps(push_list, cls=DecimalEncoder))
            ret.raise_for_status()

