# Edit metadata in Bulk with API Management

*You must have API management activated on your domain in order to update metadata in bulk. If this is not the case, contact your CSM or the support to ask for its activation.*

## Create your data file of new metadatas

1. Create and configure a "domaindatasets://" dataset. If you don't know how to do so, please read the [documentation](https://help.opendatasoft.com/platform/en/publishing_data/04_configuring_a_source/connectors/dataset_of_datasets.html "domaindatasets ODS documentation").
2. In the export tab of this dataset, export as a CSV the datasets for which you want to update the metadatas
3. Import this file in a Google Sheet, and specify a ";" separator (or "," if you have configured this separator on your domain)
4. Change the metadata values within your google sheet, delete all the columns of metadata you do not wish to update, then export it as a CSV with comma separated values
5. Send this CSV file to your CSM or run yourself the Postman collection in this folder entitled ["Metadata changes - Update multiple metadata values at once.json"](https://github.com/opendatasoft/ods-cookbook/blob/master/management-api/Metadata%20changes%20-%20Update%20multiple%20metadata%20values%20at%20once.postman_collection.json), with the CSV export as the datafile. Please read the collection description in Postman first.
