### Template bar - Light dashboard !

#### Code 

```html
<div class="container">

    <ods-dataset-context context="recordstores" recordstores-dataset="record-stores">

        <div class="row chart-space chart-bottom-line">
            <div class="col-md-offset-3 col-md-6 title">
                <h2>
                    !!! TITLE HERE !!!
                </h2>
            </div>
            <div class="col-md-offset-2 col-md-8 title">
                <p>
                    !!! DESCRIPTION HERE !!!  <span class="brand">!!! BRAND STYLE HERE !!! </span>.
                </p>
            </div>
        </div>

        <div class="row chart-space">
            <div class="col-md-6 chart-block">
                <div class="chart-inner-block">

        <ods-chart>
        <ods-chart-query context="recordstores" field-x="city" maxpoints="20" sort="serie1-1">
            <ods-chart-serie chart-type="bar" function-y="COUNT" label-y="Top 20 cities" color="#2C3F56" scientific-display="true">
            </ods-chart-serie>
        </ods-chart-query>
    </ods-chart>


                </div>
            </div>

            <div class="col-md-6 chart-text">
                <h2>
                    !!! TITLE HERE !!!
                </h2>
                <p>
                    !!! DESCRIPTION HERE !!!
                </p>
                <a class="access" href="#">!!! LINK HERE !!!</a>
            </div>
        </div>

        <div class="row chart-space">
            <div class="col-md-7 chart-text">
                <h2>
                    !!! TITLE HERE !!!
                </h2>
                <p>
                    !!! DESCRIPTION HERE !!!
                    <br/><span class="code">code style</span>
                    <br/><a target="_blanck" href="#">link style</a> 
                </p>
                <a class="access" href="#">!!! LINK HERE !!!</a>
            </div>

            <div class="col-md-5 chart-block">
                <div class="chart-inner-block">

                    <ods-chart>
                        <ods-chart-query context="recordstores" field-x="city" maxpoints="10" sort="serie1-1">
                            <ods-chart-serie chart-type="pie" function-y="COUNT" color="range-custom" scientific-display="true">
                            </ods-chart-serie>
                        </ods-chart-query>
                    </ods-chart>

                </div>
            </div>
        </div>

        <div class="row chart-space chart-bottom-line">
            <div class="col-md-4 chart-text">
                <h2>
                    !!! TITLE HERE !!!
                </h2>
                <p>
                    !!! DESCRIPTION HERE !!!
                </p>
                <div class="chart-inner-block chart-inner-block__kpi">
                    <div ods-aggregation="cnt"
                         ods-aggregation-context="recordstores"
                         ods-aggregation-function="COUNT">
                        {{ cnt | number }}
                    </div>
                    <div class="chart-inner-block__kpi-legend">
                        Aggregation
                    </div>
                </div>
                <a class="access" href="#">!!! LINK HERE !!!</a>
            </div>

            <div class="col-md-8 chart-block">
                <div id="table1" class="chart-inner-block">

                    <ods-table context="recordstores"></ods-table>

                </div>
            </div>
        </div>

        <div class="row chart-space">
            <div class="col-md-offset-2 col-md-8 chart-text chart-text__announcement">
                <h2>
                    !!! TITLE HERE !!!
                </h2>
                
                <p>
                    !!! DESCRIPTION HERE !!! <span class="brand">your PROJECT</span> or <span class="brand">your APP</span>.
                </p>
                <a target="_blanck" href="#"><i class="fa fa-hand-o-right" aria-hidden="true"></i>!!! LINK HERE !!!</a>
            </div>
        </div>
    </ods-dataset-context>
</div>
```

```css
/* PAGE LAYOUT AND OVERALL STYLE */

.title {
    text-align: center;
}
.title h2 {
    font-size: 2.3em;
    font-weight: 300;
}
.title p {
    margin-top: 20px;
    font-size: 1.3em;
    font-weight: 300;
}
.chart-space {
    padding-bottom: 60px;
    padding-top: 60px;
}
.chart-bottom-line {
    border-bottom: 1px solid #cecece7d;
}
.chart-inner-block {
    box-shadow: 9px 17px 60px #afafaf;
    padding: 50px 50px 20px 27px;
}

.chart-text {
    padding-left: 50px;
    padding-right: 40px;
}
.chart-text h2 {
    font-size: 2em;
    font-weight: 300;
}
.chart-text p {
    font-size: 1.3em;
    font-weight: 300;
}
.chart-text__announcement {
    text-align: center;
}
.chart-text__announcement p {
    border-left: none;
    padding-left: inherit;
}
.chart-text__announcement a {
    font-size: 1.4em;
    text-transform: uppercase;
}

/* TEXT AND SPECIFIC ELEMENT STYLE */
.chart-inner-block__kpi {
    margin: 50px;
    padding: 25px 50px;
    text-align: center;
    font-size: 2.5em;
    font-weight: 500;
}
.chart-inner-block__kpi-legend {
    font-size: 0.4em;
    font-weight: 100;
}
.access {
    text-transform: uppercase;
}
.code {
    color: #e26f27;
    font-family: monospace;
    font-size: 0.95em;
}
.brand {
    font-weight: 400;
}

/* CHART GLOBAL OVERRIDE */
rect.highcharts-background {
    fill: transparent !important;
}

/* SPECIFIC WIDGET OVERRIDE */
#chart1 text.highcharts-axis-title {
    display: none;
}
#table1 {
    padding: 0px;
}
```

#### Result

[See it here !](https://template-discovery.opendatasoft.com/pages/light-dashboard/)