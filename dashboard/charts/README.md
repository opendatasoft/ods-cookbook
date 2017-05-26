### ODS-Widgets Charts !

 - [ODS-Widgets chart page here] (https://discovery.opendatasoft.com/pages/demo-charts-widgets/)
 

```html
<div class="container">
    <div class="ods-box">

        <h1>
            ODS-Widgets Charts
        </h1>

        <div class="row items-row">
            <ul class="items" ng-init="tab='one'">
                <li class="item ods-button ods-button--primary" ng-class="{'ods-button--danger': tab == 'one'}" ng-click="tab='one'">
                    Bar, Column
                </li>
                <li class="item ods-button ods-button--primary" ng-class="{'ods-button--danger': tab == 'two'}" ng-click="tab='two'">
                    Spline, Range, Boxplot
                </li>
                <li class="item ods-button ods-button--primary" ng-class="{'ods-button--danger': tab == 'three'}" ng-click="tab='three'">
                    Gauge, Tree, Pie
                </li>
                <li class="item ods-button ods-button--primary" ng-class="{'ods-button--danger': tab == 'four'}" ng-click="tab='four'">
                    Polar, Spider
                </li>
            </ul>
        </div>

        <!-- BAR COLMUN --> 
        <div class="row" ng-if="tab=='one'" >

            <div class="row">
                <div class="col-md-9">
                    <h3>
                        To see order of magnitude
                    </h3>
                    <div class="chart-title">
                        <b>Sum of available beds</b> for each types of hospital.
                    </div>
                    <ods-dataset-context context="ushospitals" ushospitals-dataset="us-hospitals">
                        <ods-chart label-x="Hospital types">
                            <ods-chart-query context="ushospitals" field-x="type" sort="serie1-1">
                                <ods-chart-serie expression-y="beds" chart-type="bar" function-y="SUM" logarithmic="true" label-y="Number of beds" color="#1E0C33" scientific-display="true">
                                </ods-chart-serie>
                            </ods-chart-query>
                        </ods-chart>
                    </ods-dataset-context>
                </div>

                <div class="col-md-3">
                    <h5>
                        Bar chart with logarithmic scale
                    </h5>
                </div>
            </div>
            
            <div class="spacer"/>
            
            <div class="row">
                <div class="col-md-9">
                    <h3>
                        To see distribution by columns with one or more series
                    </h3>
                    <div class="chart-title">
                        <b>Number of winning</b> or <b>losing</b> points for <b>Super Bowl</b> events since 1967.
                    </div>

                    <ods-dataset-context context="superbowlpublic" superbowlpublic-dataset="super-bowl@public">
                        <ods-chart single-y-axis="true">
                            <ods-chart-query context="superbowlpublic" field-x="date" timescale="year" stacked="normal">
                                <ods-chart-serie expression-y="winning_pts" 
                                                 label-y="Winning points"
                                                 chart-type="column" function-y="SUM" color="#4F8F55" scientific-display="true">
                                </ods-chart-serie>
                                <ods-chart-serie expression-y="losing_pts" 
                                                 label-y="Losing points"
                                                 chart-type="column" function-y="SUM" color="#EC643C" scientific-display="true">
                                </ods-chart-serie>
                            </ods-chart-query>
                        </ods-chart>
                    </ods-dataset-context>

                </div>

                <div class="col-md-3">
                    <h5>
                        Colmumn chart with 1 axis
                    </h5>
                    <h5>
                        Stacked view
                    </h5>
                    <h5>
                        1 serie : SUM (winning points)
                    </h5>
                    <h5>
                        1 serie : SUM (losing points)
                    </h5>
                </div>
            </div>


            

        </div>


        <!-- SPLINE RANGE BOXPLOT -->
        <div class="row" ng-if="tab=='two'" >

            <div class="row">
                <div class="col-md-9">
                    <h3>
                        To express fickleness
                    </h3>
                    <div class="chart-title">
                        <b>Gazoline (all types) consumer price index</b> fluctuation over years.
                    </div>
                    <ods-dataset-context context="cpigasoline"
                                         cpigasoline-dataset="consumer-price-index-all-urban-consumers"
                                         cpigasoline-parameters="{'refine.area_name':'U.S. city average','refine.item_name':'Gasoline (all types)'}">
                        <ods-chart timescale="year" single-y-axis="true" single-y-axis-label="Base 100 : 1982/1984" scientific-display="false" label-x="All types of Gazoline">
                            <ods-chart-query context="cpigasoline" field-x="date" timescale="year" >
                                <ods-chart-serie expression-y="value" chart-type="areasplinerange" function-y="COUNT"
                                                 label-y="MIN MAX" color="#0B72B5"
                                                 scientific-display="true"
                                                 subseries='[{"func":"MIN","yAxis":"value"},{"func":"MAX","yAxis":"value"}]'>
                                </ods-chart-serie>
                                <ods-chart-serie expression-y="value" chart-type="spline" function-y="AVG"
                                                 label-y="AVG" color="#2C3F56"
                                                 display-units="false" display-values="false" scientific-display="true">
                                </ods-chart-serie>
                            </ods-chart-query>
                        </ods-chart>
                    </ods-dataset-context>
                </div>
                <div class="col-md-3">
                    <h5>
                        Range spline : MIN and MAX of the consumer price index
                    </h5>
                    <h5>
                        Spline : AVG of the consumer price index 
                    </h5>
                </div>
            </div>

            <div class="spacer"/>

            <div class="row">
                <div class="col-md-9">
                    <div class="chart-title">
                        Same chart with boxplot.
                    </div>
                    <ods-dataset-context context="consumerpriceindexallurbanconsumers" 
                                         consumerpriceindexallurbanconsumers-dataset="consumer-price-index-all-urban-consumers" 
                                         consumerpriceindexallurbanconsumers-parameters="{'refine.area_name':'U.S. city average','refine.item_name':'Gasoline (all types)'}">
                        <ods-chart timescale="month" scientific-display="true">
                            <ods-chart-query context="consumerpriceindexallurbanconsumers" field-x="date" timescale="year">
                                <ods-chart-serie expression-y="value" 
                                                 chart-type="boxplot" 
                                                 function-y="COUNT" 
                                                 label-y="All types of gazoline versatility over years" 
                                                 color="#00757E" 
                                                 display-values="false" 
                                                 scientific-display="true" 
                                                 subseries='[{"func":"MIN","yAxis":"value"},{"func":"QUANTILES","yAxis":"value","subsets":25},{"func":"QUANTILES","yAxis":"value","subsets":50},{"func":"QUANTILES","yAxis":"value","subsets":75},{"func":"MAX","yAxis":"value"}]'>
                                </ods-chart-serie>
                            </ods-chart-query>
                        </ods-chart>

                    </ods-dataset-context>
                </div>
                <div class="col-md-3">
                    <h5>
                        Box plot of the consumer price index
                    </h5>
                    <h5>
                        Minimum, Lower quartile at percentile 25, Median at percentile 50, Upper quartile at percentile 75, Maximum
                    </h5>
                </div>
            </div>

            <div class="spacer"/>

            <div class="row">
                <div class="col-md-9">
                    <h3>
                        To express stability
                    </h3>
                    <div class="chart-title">
                        Comparison of <b>alcoholic beverages consumer price index</b>, <b>at home</b> or <b>away from home</b>.
                    </div>
                    <ods-dataset-context context="cpialcoholicawayfromhome,cpialcoholicathome"
                                         cpialcoholicawayfromhome-dataset="consumer-price-index-all-urban-consumers"
                                         cpialcoholicawayfromhome-parameters="{'refine.area_name':'U.S. city average','refine.item_name':'Alcoholic beverages away from home'}"
                                         cpialcoholicathome-dataset="consumer-price-index-all-urban-consumers"
                                         cpialcoholicathome-parameters="{'refine.area_name':'U.S. city average','refine.item_name':'Alcoholic beverages at home'}">
                        <ods-chart timescale="year" single-y-axis="true" single-y-axis-label="Base 100 : 1982/1984" min="125"
                                   step="25" scientific-display="false">
                            <ods-chart-query context="cpialcoholicawayfromhome" field-x="date" timescale="year">
                                <ods-chart-serie expression-y="value" chart-type="areasplinerange" function-y="COUNT"
                                                 label-y="Alcoholic beverages away from home(MIN MAX)" color="#0B72B5"
                                                 scientific-display="true"
                                                 subseries='[{"func":"MIN","yAxis":"value"},{"func":"MAX","yAxis":"value"}]'>
                                </ods-chart-serie>
                                <ods-chart-serie expression-y="value" chart-type="spline" function-y="AVG"
                                                 label-y="Alcoholic beverages away from home(AVG)" color="#2C3F56"
                                                 display-units="false" display-values="true" scientific-display="true">
                                </ods-chart-serie>
                            </ods-chart-query>
                            <ods-chart-query context="cpialcoholicathome" field-x="date" timescale="year">
                                <ods-chart-serie expression-y="value" chart-type="areasplinerange" function-y="COUNT"
                                                 label-y="Alcoholic beverages at home(MIN MAX)" color="#FA8C44"
                                                 scientific-display="true"
                                                 subseries='[{"func":"MIN","yAxis":"value"},{"func":"MAX","yAxis":"value"}]'>
                                </ods-chart-serie>
                                <ods-chart-serie expression-y="value" chart-type="spline" function-y="AVG"
                                                 label-y="Alcoholic beverages at home(AVG)" color="#BA022A"
                                                 display-units="false" display-values="true" scientific-display="true">
                                </ods-chart-serie>
                            </ods-chart-query>
                        </ods-chart>
                    </ods-dataset-context>
                </div>
                <div class="col-md-3">
                    <h5>
                        2 x Range spline : MIN and MAX of the consumer price index
                    </h5>
                    <h5>
                        2 x spline : AVG of the consumer price index 
                    </h5>
                </div>
            </div>

        </div>


        <!-- TREE PIE GAUGE -->
        <div class="row" ng-if="tab=='three'" >

            <div class="row">
                <div class="col-md-9">
                    <h3>
                        To simply show a progress or percentage
                    </h3>
                    <div class="row">
                        <div class="col-md-6">
                            <ods-gauge id="circle-gauge"
                                       display-mode="circle"
                                       max="100"
                                       value="73">
                            </ods-gauge>
                        </div>
                        <div class="col-md-6">
                            <ods-gauge id="red-gauge"
                                       display-mode="bar"
                                       max="100"
                                       value="12">
                            </ods-gauge>
                            <ods-gauge id="orange-gauge"
                                       display-mode="bar"
                                       max="100"
                                       value="18">
                            </ods-gauge>
                            <ods-gauge id="green-gauge"
                                       display-mode="bar"
                                       max="100"
                                       value="56">
                            </ods-gauge>
                        </div>
                    </div>
                </div>

                <div class="col-md-3">
                    <h5>
                        Jauge
                    </h5>
                    <h5>
                        Circle and bar display
                    </h5>
                </div>
            </div>

            <div class="spacer"/>            
            
            <div class="row">
                <div class="col-md-9">
                    <h3>
                        To see distribution
                    </h3>
                    <div class="chart-title">
                        <b>Number of sport equipment</b> in <b>Paris and suburbs area</b> by <b>familly</b>.
                    </div>

                    <ods-dataset-context context="ensembledesequipementssportifsdiledefranceen2016" 
                                         ensembledesequipementssportifsdiledefranceen2016-dataset="ensemble-des-equipements-sportifs-dile-de-france-en-2016">
                        <ods-chart>
                            <ods-chart-query context="ensembledesequipementssportifsdiledefranceen2016" field-x="eqt_fam" maxpoints="50" sort="serie1-1">
                                <ods-chart-serie chart-type="treemap" function-y="COUNT" color="range-custom" scientific-display="true">
                                </ods-chart-serie>
                            </ods-chart-query>
                        </ods-chart>

                    </ods-dataset-context>
                </div>

                <div class="col-md-3">
                    <h5>
                        Treemap
                    </h5>
                </div>
            </div>

            <div class="spacer"/>

            <div class="row">
                <div class="col-md-9">
                    <div class="chart-title">
                        <b>Population</b> distribution by region.
                    </div>
                    <ods-dataset-context context="geoflarcommunes2015" geoflarcommunes2015-dataset="geoflar-communes-2015" geoflarcommunes2015-parameters="{'geofilter.polygon':'(37.50972584293751,-16.171875),(55.32914440840507,-16.171875),(55.32914440840507,22.148437499999996),(37.50972584293751,22.148437499999996),(37.50972584293751,-16.171875)'}">
                        <ods-chart>
                            <ods-chart-query context="geoflarcommunes2015" field-x="nom_reg" label-x="Population" maxpoints="20" sort="serie1-1">
                                <ods-chart-serie expression-y="population" chart-type="pie" function-y="SUM" label-y="Population" color="range-custom" scientific-display="true">
                                </ods-chart-serie>
                            </ods-chart-query>
                        </ods-chart>
                    </ods-dataset-context>
                </div>

                <div class="col-md-3">
                    <h5>
                        Pie chart : Sum of the population
                    </h5>
                </div>
            </div>

        </div>


        <!-- POLAR SPIDER -->
        <div class="row" ng-if="tab=='four'" >

            <div class="row">
                <div class="col-md-9">
                    <h3>
                        To see distribution
                    </h3>
                    <div class="chart-title">
                        <b>Population</b> distribution by region + average surface area of cities in this region
                    </div>
                    <ods-dataset-context context="geoflarcommunes2015" geoflarcommunes2015-dataset="geoflar-communes-2015" geoflarcommunes2015-parameters="{'geofilter.polygon':'(37.50972584293751,-16.171875),(55.32914440840507,-16.171875),(55.32914440840507,22.148437499999996),(37.50972584293751,22.148437499999996),(37.50972584293751,-16.171875)'}">
                        <ods-chart>
                            <ods-chart-query context="geoflarcommunes2015" field-x="nom_reg" maxpoints="20" sort="serie1-1">
                                <ods-chart-serie expression-y="population" chart-type="spiderweb" function-y="SUM" label-y="Population (SUM)" color="#BA022A" scientific-display="true">
                                </ods-chart-serie>
                                <ods-chart-serie expression-y="superficie" chart-type="spiderweb" function-y="AVG" label-y="Surface area (AVG)" color="#19630A" scientific-display="true">
                                </ods-chart-serie>
                            </ods-chart-query>
                        </ods-chart>

                    </ods-dataset-context>
                </div>

                <div class="col-md-3">
                    <h5>
                        Spiderweb chart, sorted by serie 1 : Sum of the population
                    </h5>
                    <h5>
                        Serie 2 : Average of the surface area
                    </h5>
                </div>
            </div>

            <div class="spacer"/>

            <div class="row">
                <div class="col-md-9">
                    <div class="chart-title">
                        <b>Population</b>, <b>surface area</b> and <b>average high (Z axis)</b> by region.
                    </div>

                    <ods-dataset-context context="geoflarcommunes2015" geoflarcommunes2015-dataset="geoflar-communes-2015">

                        <ods-chart style="height:550px" scientific-display="true">
                            <ods-chart-query context="geoflarcommunes2015" field-x="nom_reg">
                                <ods-chart-serie expression-y="population" chart-type="polar" function-y="SUM" label-y="Population" color="#000000" display-units="false" display-values="false" scientific-display="true">
                                </ods-chart-serie>
                                <ods-chart-serie expression-y="superficie" chart-type="polar" function-y="SUM" label-y="Surface area" color="#F8B334" display-values="false" scientific-display="true">
                                </ods-chart-serie>
                                <ods-chart-serie expression-y="z_moyen" chart-type="column" function-y="AVG" label-y="Average high (Z)" color="#00757E" scientific-display="true">
                                </ods-chart-serie>
                            </ods-chart-query>
                        </ods-chart>

                    </ods-dataset-context>
                </div>

                <div class="col-md-3">
                    <h5>
                        Polar chart with 3 series
                    </h5>
                    <h5>
                        Serie 1 : SUM of city population
                    </h5>
                    <h5>
                        Serie 2 : SUM of city surface area
                    </h5>
                    <h5>
                        Serie 3 : AVG Z (third axis coordinate)
                    </h5>
                </div>
            </div>

        </div>

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

.ods-button {
    font-weight: 500;
}
.ods-button--primary {
    border: solid 1px #1E0C33;
    background-color: #1E0C33;
}
.ods-button--danger {
    border: solid 1px #a94442;
    background-color: #a94442;
}

.chart-title, .hint {
    text-align: center;
    font-style: italic;
    color: darkgrey;
    font-weight: 300;
}
.chart-title b {
    font-weight: 500;
}
tspan.highcharts-text-outline {
    display: none;
}
.spacer {
        margin-bottom: 20px;
    width: 90%;
    border-top: 1px solid rgba(30, 12, 51, 0.53);
    margin-left: auto;
    margin-right: auto;
}

#circle-gauge {
    max-width: 300px;
    margin: auto;
}
#red-gauge .odswidget-gauge__svg-filler {
    stroke: red;
}
#orange-gauge .odswidget-gauge__svg-filler {
    stroke: orange;
}
#green-gauge .odswidget-gauge__svg-filler {
    stroke: green;
}

#red-gauge .odswidget-gauge__value {
    color: red;
}
#orange-gauge .odswidget-gauge__value {
    color: orange;
}
#green-gauge .odswidget-gauge__value {
    color: green;
}
```
