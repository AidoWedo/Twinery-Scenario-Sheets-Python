function doGet() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  
  try {
    var scenarioOverview = getDataFromSheet(sheet.getSheetByName("Scenario Overview"));
    var branch1 = getDataFromSheet(sheet.getSheetByName("Branch 1"));
    var branch2 = getDataFromSheet(sheet.getSheetByName("Branch 2"));
    var choicesAndConsequences = getDataFromSheet(sheet.getSheetByName("Choices and Consequences"));
    var tryToImprovise = getDataFromSheet(sheet.getSheetByName("Try to Improvise"));
    var contemplate = getDataFromSheet(sheet.getSheetByName("Contemplate"));
    
    var data = {
      scenarioOverview: scenarioOverview,
      branch1: branch1,
      branch2: branch2,
      choicesAndConsequences: choicesAndConsequences,
      tryToImprovise: tryToImprovise,
      contemplate: contemplate
    };
    
    return ContentService.createTextOutput(JSON.stringify(data))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({error: error.message, stack: error.stack}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function getDataFromSheet(sheet) {
  if (!sheet) {
    throw new Error("Sheet not found. Please check if the sheet name is correct.");
  }
  
  var data = sheet.getDataRange().getValues();
  var headers = data.shift();
  return data.map(function(row) {
    var obj = {};
    headers.forEach(function(header, i) {
      obj[header] = row[i] === "" ? null : row[i];
    });
    return obj;
  });
}