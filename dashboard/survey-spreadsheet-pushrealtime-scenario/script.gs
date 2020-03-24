/* Get push url from Script Properties */
var pushurl = PropertiesService.getScriptProperties().getProperty('pushurl');

/* Go over each file paths, get the file, load them, and create base64 payloads */
/*
input : payload['Screenshot(s)'] = "path1, path2, path3"
ouput : payload['image1'] = {'content':'base64','content-type':'mime/mime'}
*/
function processImages(payload) {
  var photos = payload['Screenshot(s)'].split(', ');
  for(var i = 0; i < photos.length; i++) {
    photos[i] = photos[i].replace("https://drive.google.com/open?id=","");
    var f = DriveApp.getFileById(photos[i]);
    var data = Utilities.base64Encode(f.getAs(f.getMimeType()).getBytes());
    payload['image' + (i + 1)] = {'content':data, 'content-type':f.getMimeType()}; // 'image/png' ? as mime type ? f.getMimeType() ?
  }
  return payload;
}

/* Go over each meta, and create the payload with images */
function processNamedValues(e) {
  var payload = {};

  for(var k in e.namedValues) {
    payload[k] = e.namedValues[k][0];
  }

  payload = processImages(payload);
  return payload;
}


/* When not all meta are available in the event, and only the row number of the edit :
it get the sheet, get the content, get the row, and go over it to create the payload
*/
function processRange(e) {
  var payload = {};

  var sheet = SpreadsheetApp.getActiveSheet();
  var data = sheet.getDataRange().getValues();
  var modificationline = e.range.rowStart;
  Logger.log('The row number %d has been modified', modificationline);
  var header = data[0];
  var payload = {};
  for (var j = 0; j < header.length; j++) {
    payload[header[j]] = data[modificationline -1][j]; // modificatonline - 1 because data index start from 0, unlike the rows numbers in Gsheets
  }

  payload = processImages(payload);
  return payload;
}

/* Push the payload in an HTTP POST query to the PushAPI URL */
function push(payload) {
  var options = {
    'muteHttpExceptions' : true,
    'method' : 'post',
    'contentType': 'application/json',
    'payload' : JSON.stringify(payload)
  };
  var response = UrlFetchApp.fetch(pushurl, options);
  var rc = response.getResponseCode();
  var responseText = response.getContentText();
  if (rc !== 200) {
    Logger.log("Response (%s) %s",
               rc,
               responseText );
    Logger.log(options.payload);
  } else {
    Logger.log("Submit pushed successfully");
  }
}

/* Main function :
- check the kind of event (new line, edit line etc...)
- call the appropriate function to process the event
- create the payload
- push it to the PushAPI
*/
function submit(e) {
  var payload = {};
  if (e.namedValues) {
    console.log('namedValues case');
    if (e.namedValues['Domain ID'][0] != '') {
      Logger.log('namedValues domainid not null ! submit form case');
      payload = processNamedValues(e);
    } else {
      Logger.log('namedValues domainid NULL ! edit form response case');
      payload = processRange(e);
    }
  } else {
    Logger.log('NO namedValues : edit sheet case');
    payload = processRange(e);
  }

  push(payload);
}

/* From the GSheets menu, ability to repush all rows to the PushAPI, line by line
*/
function repushAll() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var data = sheet.getDataRange().getValues();

  var header = data[0];
  for (var i = 1; i < data.length; i++) {
    var payload = {};
    Logger.log("Building line %s", i);
    for (var j = 0; j < header.length; j++) {
      payload[header[j]] = data[i][j];
    }
    payload = processImages(payload);
    push(payload);
    Logger.log("Line %s pushed", i);
  }
}

/* utilitary function, to create the GSheets menu, need to be called only once at setup */
function setupActionMenu() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Opendatasoft actions')
  .addItem('Set Push URL', 'updatePushURL')
  .addItem('Repush all lines', 'repushAll')
  .addToUi();
}

/* GSheets utilitary menu action : set up a new push url */
function updatePushURL() {
  var name = Browser.inputBox('Set a new push URL to push content');
  Logger.log('Updating Push URL to : %s', name);
  if (name != 'cancel') {
    PropertiesService.getScriptProperties().setProperty('pushurl', name);
    Logger.log('Push URL updated to : %s', name);
  }
}
