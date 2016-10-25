# How to create a simple dashboard - Step by step !

#### Live result

[Please find the live dashboard on Discovery](https://discovery.opendatasoft.com/pages/doc-dashboard-stepbystep/)

#### Documentation

[Please find this dashboard documentation here](https://docs.opendatasoft.com/)

#### Code

```html
<div class="container-fluid">
    <div class="ods-box">
        <ods-dataset-context  
                             context="entreprisesimmatriculeesen2015" 
                             entreprisesimmatriculeesen2015-dataset="entreprises-immatriculees-en-2015" 
                             entreprisesimmatriculeesen2015-parameters="{}">

            <h1>
                {{ entreprisesimmatriculeesen2015.dataset.metas.title }}
            </h1>

            <div class="row">

                <!-- NAVIGATION BAR -->
                <div class="col-md-3">
                    <div class="ods-box">

                        <h3>
                            {{  entreprisesimmatriculeesen2015.nhits | number }} records
                        </h3>
                        <h5>
                            <i>
                                out of a total of {{  entreprisesimmatriculeesen2015.dataset.metas.records_count | number }} records in the dataset
                            </i>
                        </h5>

                        <ods-text-search context="entreprisesimmatriculeesen2015"></ods-text-search>
                        <ods-facets context="entreprisesimmatriculeesen2015">
                            <h3>Activity</h3>
                            <ods-facet name="libelle"></ods-facet>
                            <h3>City</h3>
                            <ods-facet name="ville"></ods-facet>
                        </ods-facets>

                        <h5>
                            <i>
                                Last modified date : {{  entreprisesimmatriculeesen2015.dataset.metas.data_processed | date : 'medium' }}                            
                            </i>
                        </h5>

                        <a ng-if="entreprisesimmatriculeesen2015.parameters['q'] || entreprisesimmatriculeesen2015.parameters['refine.ville'] || entreprisesimmatriculeesen2015.parameters['refine.libelle']"
                           href="{{ entreprisesimmatriculeesen2015.getDownloadURL('csv') }}" 
                           class="ods-button ods-button--primary">
                            Download this selection
                        </a>

                    </div>
                </div>

                <!-- MAIN CONTENT -->            
                <div class="col-md-9">

                    <!-- ROW 1 : The Map -->
                    <div class="row">
                        <div class="ods-box">
                            <ods-map context="entreprisesimmatriculeesen2015" location="2,18.59479,25.24143" basemap="mapbox.light">
                            </ods-map>
                        </div>
                    </div>

                    <!-- ROW 2 : Chart and table -->
                    <div class="row items-row">
                        <ul class="items" ng-init="tab='first'">
                            <li class="item ods-button ods-button--primary" ng-class="{'ods-button--danger': tab == 'first'}" ng-click="tab='first'">
                                Table
                            </li>
                            <li class="item ods-button ods-button--primary" ng-class="{'ods-button--danger': tab == 'second'}" ng-click="tab='second'">
                                Region chart
                            </li>
                            <li class="item ods-button ods-button--primary" ng-class="{'ods-button--danger': tab == 'third'}" ng-click="tab='third'">
                                Time serie
                            </li>
                        </ul>
                    </div>

                    <div class="row">
                        <div ng-if="tab=='first'" class="block">
                            <div class="ods-box">
                                <ods-table context="entreprisesimmatriculeesen2015">
                                </ods-table>
                            </div>
                        </div>
                        <div ng-if="tab=='second'" class="block">
                            <div class="ods-box" ng-if="! entreprisesimmatriculeesen2015.parameters['refine.ville']">
                                <ods-chart>
                                    <ods-chart-query context="entreprisesimmatriculeesen2015" field-x="region">
                                        <ods-chart-serie expression-y="siren" chart-type="line" function-y="COUNT" color="#66c2a5" scientific-display="true">
                                        </ods-chart-serie>
                                    </ods-chart-query>
                                </ods-chart>
                            </div>
                            <div class="ods-box" ng-if="entreprisesimmatriculeesen2015.parameters['refine.ville']">
                                <ods-chart>
                                    <ods-chart-query context="entreprisesimmatriculeesen2015" field-x="date_d_immatriculation" maxpoints="20" timescale="month" sort="serie1-1">
                                        <ods-chart-serie expression-y="siren" chart-type="pie" function-y="COUNT" color="range-custom" scientific-display="true">
                                        </ods-chart-serie>
                                    </ods-chart-query>
                                </ods-chart>
                            </div>
                        </div>
                        <div ng-if="tab=='third'" class="block">
                            <ods-chart timescale="year">
                                <ods-chart-query context="entreprisesimmatriculeesen2015" field-x="date_d_immatriculation" timescale="day">
                                    <ods-chart-serie expression-y="siren" chart-type="spline" function-y="COUNT" color="#ff0000" scientific-display="true">
                                    </ods-chart-serie>
                                </ods-chart-query>
                            </ods-chart>

                        </div>
                    </div>
                </div>

            </div>
        </ods-dataset-context>
    </div>
</div>
```

```css
.items-row {
    text-align: center; /* center all buttons */
}

.items {
    display: inline-flex; /* Display in line */
    list-style-type: none; /* Remove the list bullet */
}

.item {
    margin: 0 20px; /* give some space left and right */
}
```