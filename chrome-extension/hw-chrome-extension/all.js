chrome.action.onClicked.addListener(function (tab) {
    chrome.scripting.executeScript({
        files: ["toggle-show-hide.js"],
        target : {tabId : tab.id}
    });
});


chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    chrome.action.setIcon({
        path: request.newIconPath,
        tabId: sender.tab.id
    });
    chrome.action.setTitle({
        title: "No Huwise portal detected. Extension disabled."
    })
});
