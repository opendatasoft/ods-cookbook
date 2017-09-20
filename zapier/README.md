# Zapier integration !

Zapier is a web-based service that allows end users to integrate the web applications they use.
As any OpenDataSoft end-user or customer, you'll then be able to directly connect OpenDataSoft API to Zapier workflow to generate alerts or action based on your favorite data.

Here is a list of some possible use cases :
 
  - Getting an alert* when a new dataset is published on your favorite OpenData portal.
  - Getting an alert* when a real time dataset hasn't seen it's data updated since more than 15 minutes
  - Getting an alert* when a new record match your research in your favorite dataset

*Alerts are the end of Zapier workflow to send a message through any kind of communication tool like Slack, Yammer, E-mail, SMS etc...
  

## Simple mode : Zapier WebHook - Retrieve poll

The concept is very simple, Zapier will poll an URL and look for new entries.
As any OpenDataSoft datasets or catalogs, APIs are available to list all the entries (ie records or datasets).

Zapier is then able to poll the API, and for each new entry, trigger an action.

The requirements are :
- having an API -> simple with OpenDataSoft !
- having a sort field : the query must return new entries first !
- having a unique identifier to let Zapier know if it's really new or not

If you fulfill all these requirements let's go !

 - [Alert me if new datasets are publish for a specific search or a specific theme !](./new-dataset-alert.md)
 - [Alert me if there is a new record matching my criteria !](./new-record-alert.md)


## Advanced mode : python code !

Zapier allows any user to execute javascript or python code directly on Zapier platform !

Any user is free to then develop their own triggers or actions. We will then see how to have advanced triggers in python, checking the API, getting the data, processing it, and returning objects to be pushed to Zapier actions.

The requirements are :
- having a API also obviously -> still not a problem with OpenDataSoft
- being able to use the API and it's parameters with ease
- having some basic development skills to understand what's happening
- having a deep look at [Zapier python code documentation](https://zapier.com/help/code-python/)

If you fulfill, more or less, these requirements, let's pursue !

 - [Alert me when my dataset is no longer updated (ie the processing date didn't change since more than 15 minutes)](./zapier-monitor-data-processed.md)
 - [Alert me when value changes on a specific record or on several records](./zapier-monitor-field-value.md)
 
 
