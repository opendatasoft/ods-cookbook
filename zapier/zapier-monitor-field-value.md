### "Alert me when value changes on a specific record or on several records" 

This use case is useful when you want to monitor a specific value or be alerted for any changes on one or several records.

For exemple : 
 - A parking spot becomes available
 - An asset status switch from "Working" to "Failure"

 
The aim is then to get the records through the API, for each record get the supervised metadata's value and compare it to the previous one.
If it changed, Zapier can trigger an action.

To execute this scenario with need a more advanced Zap, to execute some code to get the metadata, compare it etc...
 
Here is the bloc of code to copy paste and adapt in "Code / Python" Zapier trigger :

```python
domainid = "data.issy.com"
datasetid = "disponibilite-parking-aximumcolas"
apikey = "--APIKEY--"
store = StoreClient(str(hash('%s%s' % (domainid, datasetid))))
getfailsafe = "https://%s/api/records/1.0/search/?dataset=%s&rows=100&apikey=%s"%(domainid, datasetid, apikey)

req = requests.get(getfailsafe)
req.raise_for_status()

keys = dict()
output = list()

if req.json().get('nhits') and len(req.json().get('records',[])) > 0:
    for record in req.json()['records']:
        store_key = '%s' % record['fields']['identifiant_place']
        status = '%s' % record['fields']['etat']
        keys[store_key] = status
stored_keys = store.get_many(keys)
for key in keys:
    if not stored_keys.has_key(key) or stored_keys[key] is None:
        keys[key] = -1
    else:
        if keys[key] != stored_keys[key]:
            output.append({"new_status":keys[key], "last_status":stored_keys[key], "identifiant_place": key, "continue":1})
store.set_many(keys)
if len(output) == 0:
    return {"last_status":-1, "new_status":-1, "identifiant_place" : "X", "continue" : 0}
else:
    return output
```


A little explanation:

1. It contacts the API to get the record list
2. For each record : it get the identifier of the record and the supervised value
   - If this identifier has already been seen, we compare the previous value
     - If the value is different : we add this record to the alert list that will be returned at the end of the Zap
     - If the value is the same, nothing happen
3. In any case we store the value for each identifier for the next Zap call


Once the trigger is set-up in Zapier, before setting up the action, you will need to add a filter.
The filter settings should be :
  - "Only continue if..."
  - "continue" Greater than "0"
  
This will let pass real alerts, and prevent the false one to trigger any alert. 
(ie false one is simply the default alert that send all values to "-1" and identifier to "X". It's just needed at the beginning to set up the action)

 
In this exemple, we are monitoring available parking spots. Each time a car park in or out. The parking spot status change and an alert is sent.
An easy improvement would be to filter the initial API query to a specific area, for example a neighbourhood or a street. 
And add a Zapier filter to only let pass when parking spot status switch to free. 
 
**It would result in a nice Zap that send an alert each time a parking spot becomes free in your street !** 

 
Feel free to add any meta you'd like by adding new keys and values on the json returned object :

```python
            output.append({"new_status":keys[key], "last_status":stored_keys[key], "identifiant_place": key, "continue":1})
```

