### "Alert me when my dataset is no longer updated" (ie the processing date didn't change since more than 15 minutes)

This use case is useful for real time dataset that are updated every minutes for example.
 
The aim is then to check through the API the `data_processed` metadata of the dataset that highlight the user on the last processing time of the dataset.
If it's older than 15, 30 or X minutes, Zapier can then trigger an action.

To execute this scenario with need a more advanced Zap, to execute some code to get the metadata, compare it etc...
But we also need an alarm trigger status, "on" or "off" ! We don't want an alert each time Zapier will check the metadata.
We want Zapier to fire an alert the first time, but as long as the dataset is not fixed and is not working better, we keep the alarm down.
As soon as the dataset start to be updated again, we want to active the alarm again.
 
Here is the bloc of code to copy paste and adapt in Zapier :

```python
import datetime

domainid = "--DOMAIN ID HERE--"
datasetid = "--DATASET ID HERE--"
apikey = "--API KEY HERE--"
getquery = "https://%s.opendatasoft.com/api/v2/catalog/datasets/%s?apikey=%s"%(domainid, datasetid, apikey)

store = StoreClient(str(hash('%s%s' % (domainid, datasetid))))
store_key = "alert-status"

req = requests.get(getquery)
req.raise_for_status()

jsonresponse = req.json()

if jsonresponse.get('dataset'):
    value = jsonresponse['dataset']['metas']['default']['data_processed']

    now = datetime.datetime.utcnow()
    dt = datetime.datetime.strptime(value,"%Y-%m-%dT%H:%M:%S+00:00")
    in_late = (now + datetime.timedelta(minutes=-15)) > dt

    last_alarm_status = store.get(store_key)
    if last_alarm_status is None:
        last_alarm_status = "on"
    new_alarm_status = last_alarm_status
    trigger_alarm = False

    if last_alarm_status == "on":
        if in_late:
            trigger = True
            new_alarm_status = "off"
        else:
            trigger = False
            new_alarm_status = "on"
    else:
        trigger = False
        if in_late:
            new_alarm_status = "off"
        else:
            new_alarm_status = "on"

    store.set(store_key, new_alarm_status)

    if trigger:
        return {"data_processed":dt.strftime("%Y/%m/%d %H:%M:%S"), "utcnow":now.strftime("%Y/%m/%d %H:%M:%S"), "datasetid" : datasetid}
    else:
        return {"data_processed":now.strftime("%Y/%m/%d %H:%M:%S"), "utcnow":now.strftime("%Y/%m/%d %H:%M:%S"), "datasetid" : datasetid}

```

A little explanation:

1. It contacts the API to get the dataset information
2. It get the value of the data_processed data
3. It computes the time delta between now and the data_processed time and see if it's bigger than 15 minutes
3. It get the value of the alarm status (on or off)
4. Then it goes through all the combination:
    - if alarm status is On and the dataset processing time is in late (more than 15 minutes) : it triggers and set the alarm to "off"
    - if alarm status is On and the dataset processing time is not in late : nothing to do, keep as is
    - if alarm status is Off and the dataset processing time is in late : nothing to do, we are waiting for the dataset to come back to normal to activate the alarm again
    - if alarm status is Off and the dataset processing time is not longer in late : we reactivate the alarm


Once the trigger is set-up in Zapier, feel free to add any action you'd like, SMS, Emails, Slack, Yammer etc... and compose your message with the few metadata returned by the python code :
 - data_processed
 - utcnow (compared date)
 - datasetid
 
Feel free to add any meta you'd like by adding new keys and values on the json returned object :

```python
return {"data_processed":dt.strftime("%Y/%m/%d %H:%M:%S"), "utcnow":now.strftime("%Y/%m/%d %H:%M:%S"), "datasetid" : datasetid, "continue" : 1}
```

