# Advanced Dashboard !

#### Live result

[Please find the live dashboard on Discovery](https://discovery.opendatasoft.com/pages/doc-regularite-mensuelle-tgv/)

#### Documentation

[Please find this dashboard documentation here](http://docs.opendatasoft.com/en/editing_pages/dashboard/advanced_dashboard.html)

#### Code

```html
<div class="container">

    <ods-dataset-context 
                         context="regularitemensuelletgv,regularitemensuelletgvfiltered" 
                         regularitemensuelletgv-dataset="regularite-mensuelle-tgv"
                         regularitemensuelletgvfiltered-dataset="regularite-mensuelle-tgv">

        <div class="row">
            <div ods-aggregation="total"
                 ods-aggregation-context="regularitemensuelletgv"
                 ods-aggregation-function="SUM"
                 ods-aggregation-expression="nombre_de_trains_programmes">
                <div ods-aggregation="canceled"
                     ods-aggregation-context="regularitemensuelletgv"
                     ods-aggregation-function="SUM"
                     ods-aggregation-expression="nombre_de_trains_annules">
                    <div ods-aggregation="delayed"
                         ods-aggregation-context="regularitemensuelletgv"
                         ods-aggregation-function="SUM"
                         ods-aggregation-expression="nombre_de_trains_en_retard_a_l_arrivee">

                        <div ods-aggregation="totalfiltered"
                             ods-aggregation-context="regularitemensuelletgvfiltered"
                             ods-aggregation-function="SUM"
                             ods-aggregation-expression="nombre_de_trains_programmes">
                            <div ods-aggregation="canceledfiltered"
                                 ods-aggregation-context="regularitemensuelletgvfiltered"
                                 ods-aggregation-function="SUM"
                                 ods-aggregation-expression="nombre_de_trains_annules">
                                <div ods-aggregation="delayedfiltered"
                                     ods-aggregation-context="regularitemensuelletgvfiltered"
                                     ods-aggregation-function="SUM"
                                     ods-aggregation-expression="nombre_de_trains_en_retard_a_l_arrivee">

                                    <div class="row">
                                        <div class="col-md-2 col-sm-3 col-xs-4">
                                            <div class="kpi">
                                                <div class="kpi-title">
                                                    Scheduled
                                                </div>
                                                <div class="kpi-value">
                                                    {{ totalfiltered | number }}
                                                </div>
                                                <div class="kpi-value-reference">
                                                    ({{ total | number }})
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-md-2 col-sm-3 col-xs-4">
                                            <div class="kpi">
                                                <div class="kpi-title">
                                                    Canceled
                                                </div>
                                                <div class="kpi-value">
                                                    {{ canceledfiltered | number }}
                                                </div>
                                                <div class="kpi-value-reference">
                                                    ({{ canceled | number }})
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-md-2 col-sm-3 col-xs-4">
                                            <div class="kpi">
                                                <div class="kpi-title">
                                                    Delayed
                                                </div>
                                                <div class="kpi-value">
                                                    {{ delayedfiltered | number }}
                                                </div>
                                                <div class="kpi-value-reference">
                                                    ({{ delayed | number }})
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-md-2 col-sm-3 col-xs-4">
                                            <div class="kpi" ng-class="{
                                                                       'good': (canceledfiltered / totalfiltered * 100) < (canceled / total * 100),
                                                                       'bad': (canceledfiltered / totalfiltered * 100) > (canceled / total * 100),
                                                                       }">
                                                <div class="kpi-title">
                                                    % Canceled
                                                </div>
                                                <div class="kpi-value">
                                                    {{ canceledfiltered / totalfiltered * 100 | number : 2 }}<span class="kpi-value-unit"> %</span>
                                                </div>
                                                <div class="kpi-value-reference">
                                                    ({{ canceled / total * 100 | number : 2 }}<span class="kpi-value-unit"> %</span>)
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-md-2 col-sm-3 col-xs-4">
                                            <div class="kpi" ng-class="{
                                                                       'good': (delayedfiltered / totalfiltered * 100) < (delayed / total * 100),
                                                                       'bad': (delayedfiltered / totalfiltered * 100) > (delayed / total * 100),
                                                                       }">
                                                <div class="kpi-title">
                                                    % Delayed

                                                </div>
                                                <div class="kpi-value">
                                                    {{ delayedfiltered / totalfiltered * 100 | number : 2 }}<span class="kpi-value-unit"> %</span>
                                                </div>
                                                <div class="kpi-value-reference">
                                                    ({{ delayed / total * 100 | number : 2 }}<span class="kpi-value-unit"> %</span>)
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-md-2 col-sm-3 col-xs-4">
                                            <div class="kpi">
                                                <div class="kpi-title">
                                                    On time
                                                </div>
                                                <div class="kpi-value">
                                                    {{ totalfiltered - delayedfiltered - canceledfiltered | number }}
                                                </div>
                                                <div class="kpi-value-reference">
                                                    ({{ total - delayed - canceled | number }})
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br/>

        <div class="row">
            <div class="col-md-3">
                <div class="ods-box">
                    <ods-facets context="regularitemensuelletgvfiltered">
                        <h2>
                            Date
                        </h2>
                        <ods-facet name="date"></ods-facet>
                        <h2>
                            Origin station
                        </h2>
                        <ods-facet name="depart"></ods-facet>
                    </ods-facets>
                </div>
            </div>
            <div class="col-md-9">
                <div class="ods-box">
                    <h3>
                        Top 10 train station by regularity
                    </h3>
                    <div ods-analysis="tgvanalysis"
                         ods-analysis-context="regularitemensuelletgvfiltered"
                         ods-analysis-max="10"
                         ods-analysis-x="depart"
                         ods-analysis-serie-regularity="AVG(regularite)"
                         ods-analysis-serie-scheduled="AVG(nombre_de_trains_programmes)"
                         ods-analysis-serie-canceled="AVG(nombre_de_trains_annules)"
                         ods-analysis-serie-delayed="AVG(nombre_de_trains_en_retard_a_l_arrivee)"
                         ods-analysis-sort="regularity"
                         >
                        <table id="top10">
                            <thead>
                                <tr>
                                    <td>Position</td>
                                    <td>Train station</td>
                                    <td>Regularity</td>
                                    <td>Scheduled</td>
                                    <td>Canceled</td>
                                    <td>Delayed</td>
                                </tr>
                            </thead>
                            <tbody>
                                <tr ng-repeat="(i, result) in tgvanalysis.results">
                                    <td>
                                        {{ i + 1 }}
                                    </td>
                                    <td>
                                        {{ result.x }}
                                    </td>
                                    <td>
                                        {{ result.regularity | number : 2 }}
                                    </td>
                                    <td>
                                        {{ result.scheduled | number : 2 }}
                                    </td>
                                    <td>
                                        {{ result.canceled | number : 2 }}
                                    </td>
                                    <td>
                                        {{ result.delayed | number : 2 }}
                                    </td>
                                </tr>
                            </tbody>  
                        </table>
                    </div>
                </div>
                
                <div class="ods-box">
                    <ods-table context="regularitemensuelletgvfiltered"></ods-table>               
                </div>
            </div>
        </div>


    </ods-dataset-context>

</div>
```

```css
/* KPIs */

.kpis {
    display: inline-flex;
}

.kpi {
    text-align: center;

    padding: 5px 0px;
    margin-bottom: 10px;
    height: 90px;
    
    border: 1.5px solid #010201; /* the border */
    border-radius: 5px; /* rounded corners */
}

.kpi-title {
    font-size: 1em; /* bigger font */
    font-weight: 400; /* thicker font */
}

.kpi-value {
    font-size: 2em; /* bigger font */
    font-weight: 500; /* thicker font */
}

.kpi-value-reference {
    font-size: 1em; /* bigger font */
    font-weight: 400; /* thicker font */
}

.kpi-value-unit {
    font-size: 0.7em; /* bigger font */
    font-weight: 400; /* thicker font */
}

.good {
    color: #55cd61;
    border-color: #55cd61;
}

.medium {
    color: #ff9c22;
    border-color: #ff9c22;
}

.bad {
    color: #e50000;
    border-color: #e50000;
}


/* TABLE */
#top10 {
    margin: 20px auto;
}

#top10 thead > tr {
    background-color: #007396;
    color: white;
}

#top10 td {
    min-width: 100px;
    padding: 3px 10px;
    text-align: center;
}

#top10 tr:nth-child(even) {
    background-color: #ededed;
}

#top10 tr:hover{
    background-color:#ccc;
}

```