if (document.querySelector("[ng-app=\"ods.frontend\"]") != undefined) {
    add_page_links();
}

function add_page_links() {
    window.setTimeout(function () {
        var list = document.getElementById("hw-helper-list");
        if (list == null) {
            list = document.createElement("div");
            list.id = "hw-helper-list";
        } else {
            list.appendChild(document.createElement("hr"));
        }

        re = /\/page[s]?\/([^/]*)\//;

        var edit = document.createElement("a");
        edit.innerHTML = '<i title="Edit page" class="fa fa-pencil" aria-hidden="true"></i>';
        edit.id = "hw-helper-list-edit"
        edit.href = "/backoffice/pages/" + window.location.pathname.replace(re, '$1') + "/content/";
        list.appendChild(edit);

        var monitor = document.createElement("a");
        monitor.innerHTML = '<i title="See page statistics" class="fa fa-pie-chart" aria-hidden="true"></i>';
        monitor.id = "hw-helper-list-monitor"
        monitor.href = "/explore/dataset/ods-api-monitoring/analyze/?" +
            "source=monitoring&sort=timestamp&" +
            "refine.custom_attributes=APP%2Fpage-" + window.location.pathname.replace(re, '$1') +
            "&dataChart=eyJxdWVyaWVzIjpbeyJzb3J0IjoiIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoibW9udGgiLCJjaGFydHMiOlt7ImNvbG9yIjoiIzY2YzJhNSIsInR5cGUiOiJjb2x1bW4iLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiZnVuYyI6IkNPVU5UIn1dLCJ4QXhpcyI6InRpbWVzdGFtcCIsImNvbmZpZyI6eyJkYXRhc2V0Ijoib2RzLWFwaS1tb25pdG9yaW5nIiwib3B0aW9ucyI6eyJzb3VyY2UiOiJtb25pdG9yaW5nIiwiZGlzanVuY3RpdmUuZGF0YXNldF9pZCI6dHJ1ZSwic29ydCI6InRpbWVzdGFtcCIsInJlZmluZS5jdXN0b21fYXR0cmlidXRlcyI6IkFQUC9wYWdlLWhvbWUifX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZX0%3D"
        list.appendChild(monitor);

        var datasetids = {}

        var contexts = document.getElementsByTagName("ods-dataset-context");
        for (var i = 0; i < contexts.length; i++) {
            var attributes = Object.values(contexts[i].attributes);
            attributes.forEach(function (attr) {
                if (attr.name.endsWith("-dataset")) {
                    datasetids[attr.value] = undefined;
                }
            });
        }

        if (Object.keys(datasetids).length > 0) {
            var introspect = document.createElement("a");
            introspect.innerHTML = '<i title="See datasets used in this page" class="fa fa-link" aria-hidden="true"></i>';
            introspect.id = "hw-helper-list-introspect"
            introspect.href = "/explore/?q=datasetid:" + Object.keys(datasetids).join(' OR datasetid:')
            list.appendChild(introspect);
        }


        document.body.appendChild(list);
    }, 1500);
}