if (document.querySelector("[ng-app=\"ods.frontend\"]") != undefined) {
    add_bo_links();
} else {
    chrome.runtime.sendMessage({
        newIconPath: {
            16: "hw-not-found16.png",
            48: "hw-not-found48.png",
            128: "hw-not-found128.png"
        }
    });
}


function add_bo_links() {
    var list = document.getElementById("hw-helper-list");
    if (list == null) {
        list = document.createElement("div");
        list.id = "hw-helper-list";
    } else {
        list.appendChild(document.createElement("hr"));
    }

    re = /.*\/backoffice\/.*/;

    var newpage = document.createElement("a");
    newpage.innerHTML = '<i title="New page" class="fa fa-file-o" aria-hidden="true"></i>';
    newpage.id = "hw-helper-list-newpage"
    newpage.href = "/backoffice/pages/new/";
    list.appendChild(newpage);

    var newds = document.createElement("a");
    newds.innerHTML = '<i title="New dataset" class="fa fa-database" aria-hidden="true"></i>';
    newds.id = "hw-helper-list-newds"
    newds.href = "/backoffice/catalog/datasets/new/";
    list.appendChild(newds);

    list.appendChild(document.createElement("hr"));

    var switchside = document.createElement("a");
    switchside.id = "hw-helper-list-switch"
    if (window.location.pathname.search(re) >= 0) { // if on backoffice side, go back to front
        switchside.innerHTML = '<i title="Go back to the frontoffice" class="fa fa-reply" aria-hidden="true"></i>';
        switchside.href = "/";
    } else { // front to back
        switchside.innerHTML = '<i title="Go to the backoffice" class="fa fa-reply" aria-hidden="true"></i>';
        switchside.href = "/login/?next=/backoffice/";
    }

    list.appendChild(switchside);


    document.body.appendChild(list);
}