#!/usr/bin/python
import MySQLdb
import MySQLdb.cursors
import json
import datetime
import requests
import time

''' PUSH '''
DOMAIN='YOURDOMAIN.opendatasoft.com'
PUSH_OR_API_LEY='YOUR API KEY HERE'
push_base_url = 'http://%s/api/push/1.0/am/realtime/push/?pushkey=%s'%(DOMAIN,PUSH_OR_API_LEY)

# A specific datetime encoder for json.dumps
class DTEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return str(o)
        if isinstance(o, datetime.date):
            return str(o)
        return super(DTEncoder, self).default(o)

fields = None

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                     passwd="", # your password
                     db="YOURDB", # name of the data base
                     cursorclass=MySQLdb.cursors.SSCursor) # Streamed cursor
cur = db.cursor()

cur.execute("select * from X LEFT JOIN Y ON X.id = Y.id where X.zip = \"0\"")

cpt_total = 0
doc_list = list() # Push buffer to increase push speed and optimize processing
cpt = 0 # Push buffer counter

now = datetime.datetime.now()

fields = [i[0] for i in cur.description]

for row in cur:
    # build the dict / record
    record = dict()
    for i, e in enumerate(fields):
        record[e] = row[i]

    # append to the buffer list
    doc_list.append(record)
    cpt += 1
    cpt_total += 1
    # every 100 -> Push !
    if (cpt >= 100):
        ret = requests.post(push_base_url, data=json.dumps(doc_list, cls=DTEncoder))
        ret.raise_for_status()
        cpt = 0
        doc_list = list()
        delta = datetime.datetime.now() - now
        print "[Push status] %d documents pushed in %.2f minutes"%(cpt_total, delta.total_seconds() / 60)

if cpt != 0:
    ret = requests.post(push_base_url, data=json.dumps(doc_list, cls=DTEncoder))
    ret.raise_for_status()

delta = datetime.datetime.now() - now
print "*** END ***"
print "[Total time] %d documents pushed in %.2f minutes"%(cpt_total, delta.total_seconds() / 60)

db.close()
