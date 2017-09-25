### Play Button example

This is a quick and dirty example of how to automatically change facets at a regular interval


```html
<html>
<body>
    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.22/angular.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.22/angular-sanitize.js"></script>
    <script src="https://opendatasoft.github.io/ods-widgets/dist/ods-widgets.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://opendatasoft.github.io/ods-widgets/dist/ods-widgets.css">

    <div class="container" style="padding-top: 3em; height: 800px">

        <div ng-app="ods-widgets">

            <ods-dataset-context 
                context="ctx" 
                ctx-domain="kapsarc.opendatasoft.com"
                ctx-dataset="capacity-of-power-generation-by-power-source-and-region" 
                ctx-parameters="{'disjunctive.region':true,'disjunctive.power_source':true,'disjunctive.statistical_year':true,'refine.power_source':'Hydro','refine.statistical_year':'2006'}">


                <script>
                    var interval_id;
                    function play() {
                        var current_year = parseInt(angular.element('ods-dataset-context')
                                .scope().ctx.parameters['refine.statistical_year']);
                        interval_id = setInterval(function() {
                            if (current_year > 2017) {
                                current_year = 2005;
                            }
                            angular.element('ods-dataset-context')
                                .scope().ctx.parameters['refine.statistical_year'] = current_year;
                            angular.element('ods-dataset-context')
                                .scope().playing = true;
                            angular.element('ods-dataset-context')
                                .scope().$apply();

                            current_year += 1;
                        }, 1000);
                    }

                    function stop() {
                        clearInterval(interval_id);
                        angular.element('ods-dataset-context')
                            .scope().playing = false;
                        angular.element('ods-dataset-context')
                            .scope().$apply();                        
                    }                    
                </script>


                <div class="row">
                    <div class="col-md-3">
                        <ods-facets context="ctx">
                            <h3>Power Source</h3>
                            <ods-facet name="power_source"></ods-facet>
                        </ods-facets>
                    </div>

                    <div class="col-md-9">
                        <ods-map style="height: 500px" scroll-wheel-zoom="false">
                            <ods-map-layer context="ctx" 
                                color="#C32D1C" show-marker="true" 
                                display="clusters" function="SUM" expression="capacity_mw" 
                                shape-opacity="0.5" point-opacity="1" 
                                border-color="#FFFFFF" border-opacity="1" border-size="1" 
                                border-pattern="solid"
                                size-min="3" size-max="5" size-function="linear">
                            </ods-map-layer>
                        </ods-map>

                        <h3 style="text-align: center" ng-init="playing = false">
                            <span class="glyphicon glyphicon-play" onclick="play()" ng-if="!playing"></span>
                            <span class="glyphicon glyphicon-pause" onclick="stop()" ng-if="playing"></span>
                            {{ctx.parameters['refine.statistical_year']}}
                        </h3>
                        <div style="white-space: nowrap">
                            2005 <input ng-model="ctx.parameters['refine.statistical_year']" 
                                    style="display: inline-block"
                                    type="range" min="2005" max="2017" step="1"> 2017
                        </div>
                    </div>
                </div>
            </ods-dataset-context>
        </div>
    </div>
</body>
</html>
```