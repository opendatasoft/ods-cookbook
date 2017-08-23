### Ods-Map Tips&Tricks

#### Refine-On-Click - Simple usage

How to refine on a context based on another one displayed on a map :

```html
<ods-dataset-context context="regions,depts" 
                                     regions-dataset="contours-geographiques-simplifies-des-nouvelles-regions-metropole"
                                     depts-dataset="contours-simplifies-des-departements-francais-2015">
                    <div class="col-md-8">

                        <ods-map style="height:560px" scroll-wheel-zoom="false">
                            <ods-map-layer context="regions"
                                           refine-on-click-context="depts"
                                           refine-on-click-depts-map-field="new_code"
                                           refine-on-click-depts-context-field="code_reg"
                                           refine-on-click-depts-replace-refine="true"
                                           color="#3D3D3D">
                            </ods-map-layer>
                        </ods-map>
                    </div>

                    <div class="col-md-4">
                        <div ng-if="!depts.parameters['refine.code_reg']">
                            <h3 style="font-weight:600; margin-top: 40px">
                                Selectionnez une région sur la carte
                            </h3>
                        </div>
                        <div ng-if="depts.parameters['refine.code_reg']">
                            <span class="ods-button" ng-click="depts.parameters = {};">
                                Supprimer le filtre
                            </span>
                            <h3>Filtre actif: code_reg = {{ depts.parameters['refine.code_reg'] }}
                            </h3>
                            <h2>
                                Liste des départements
                            </h2>
                            <h4 ng-repeat="item in items" ods-results="items" ods-results-context="depts">
                                {{ item.fields.nom_dept }}
                            </h4>
                        </div>
                    </div>
                </ods-dataset-context>
```


#### Refine-On-Click - Advanced usage

How to refine on several context, displayed differently depending on the filters :

```html
<ods-dataset-context context="regions,depts,comm" 
                                     regions-dataset="contours-geographiques-simplifies-des-nouvelles-regions-metropole"
                                     depts-dataset="contours-simplifies-des-departements-francais-2015"
                                     comm-dataset="geoflar-communes-2015">
                    <div class="col-md-8">

                        <ods-map style="height:560px" scroll-wheel-zoom="false">
                            <ods-map-layer context="regions"
                                           refine-on-click-context="[regions,depts]"
                                           refine-on-click-regions-map-field="new_code"
                                           refine-on-click-regions-context-field="new_code"
                                           refine-on-click-depts-map-field="new_code"
                                           refine-on-click-depts-context-field="code_reg"  
                                           color="#3D3D3D"
                                           show-if="!regions.parameters['refine.new_code']">
                            </ods-map-layer>
                            <ods-map-layer context="depts"
                                           refine-on-click-context="[depts,comm]"
                                           refine-on-click-depts-map-field="code_dept"
                                           refine-on-click-depts-context-field="code_dept" 
                                           refine-on-click-comm-map-field="code_dept"
                                           refine-on-click-comm-context-field="code_dept"
                                           color="#3D3D3D"
                                           show-if="depts.parameters['refine.code_reg'] && !comm.parameters['refine.code_dept']">
                            </ods-map-layer>
                            <ods-map-layer context="comm"
                                           show-if="comm.parameters['refine.code_dept']"
                                           display="raw"
                                           color-ranges="#c0c0c0;500;#666666;3500;#3D3D3D" 
                                           color-by-field="population">
                            </ods-map-layer>
                        </ods-map>
                    </div>

                    <div class="col-md-4">
                        <span class="ods-button" ng-click="comm.parameters = {}; depts.parameters = {}; regions.parameters = {};">
                            Clear all filters    
                        </span>
                        <h2>
                            Region dataset
                        </h2>
                        <h4>
                            <span ng-if="!regions.parameters['refine.new_code']">No active filter</span>
                            <span ng-if="regions.parameters['refine.new_code']">Active filter: new_code = {{ regions.parameters['refine.new_code'] }}</span>
                        </h4>
                        <h2>
                            Department dataset
                        </h2>
                        <h4>
                            <span ng-if="!(depts.parameters['refine.code_dept'] || depts.parameters['refine.code_reg'])">No active filter</span>
                            <span ng-if="depts.parameters['refine.code_reg']">Active filter: code_reg = {{ depts.parameters['refine.code_reg'] }}</span>
                            <span ng-if="depts.parameters['refine.code_dept']"><br/>Filtre actif: code_dept = {{ depts.parameters['refine.code_dept'] }}</span>
                        </h4>
                        <h2>
                            City dataset
                        </h2>
                        <h4>
                            <span ng-if="!comm.parameters['refine.code_dept']">No active filter</span>
                            <span ng-if="comm.parameters['refine.code_dept']">Active filter: code_dept = {{ comm.parameters['refine.code_dept'] }}</span>
                        </h4>
                    </div>
                </ods-dataset-context>
```

#### Show-zoom-min/max

Configure layers to only be visible between certain zoom levels, using show-zoom-min, show-zoom-max, or both.


```html
<ods-dataset-context context="regions,depts,comm" 
                                     regions-dataset="contours-geographiques-simplifies-des-nouvelles-regions-metropole"
                                     depts-dataset="contours-simplifies-des-departements-francais-2015"
                                     comm-dataset="geoflar-communes-2015">

                    <ods-map location="5,44.73113,4.21875" style="height:560px">
                        <ods-map-layer context="regions"
                                       color="#3D3D3D"
                                       show-zoom-max="6">
                        </ods-map-layer>
                        <ods-map-layer context="depts"
                                       color="#3D3D3D"
                                       show-zoom-min="7"
                                       show-zoom-max="8">
                        </ods-map-layer>
                        <ods-map-layer context="comm"
                                       display="raw"
                                       color-ranges="#c0c0c0;500;#666666;3500;#3D3D3D" 
                                       color-by-field="population"
                                       show-zoom-min="9">
                        </ods-map-layer>
                    </ods-map>
                </ods-dataset-context>
```





