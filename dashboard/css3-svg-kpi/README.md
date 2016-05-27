### How to reproduce the [MaVille](http://castres.data.opendatasoft.com) KPIs

#### Datasets to add to your domain

First you need to add this dataset on your domain:

* resume-statistique-communes-departements-et-regions-france-2012-2013-2014

You can simply use the `Add a dataset from the OpenDataSoft network` button when you add a new source of data.

#### Page / Dashboard

Then you can create a page from the administration panel, and, when editing in expert mode, paste the following code.

HTML code:

```html

<ods-dataset-context context="resumestatistiquecommunesdepartementsetregionsfrance201220132014" 
                     resumestatistiquecommunesdepartementsetregionsfrance201220132014-dataset="resume-statistique-communes-departements-et-regions-france-2012-2013-2014" 
                     resumestatistiquecommunesdepartementsetregionsfrance201220132014-parameters="{}">
    <div class="row">

        <div class="col-md-4 col-sm-6">
            <div class="ods-box" 
                 ods-results="items" 
                 ods-results-context="resumestatistiquecommunesdepartementsetregionsfrance201220132014">
                <div class="datafact" ng-if="items" ng-init="base = (items[0].fields.chomeurs_15_64_ans_en_2012 * 100) / items[0].fields.pop_15_64_ans_en_2012; calc = 439.8 - (439.8 * base/100)">
                    <h3>Taux de Chômage</h3>
                    <div class="progress" ng-if="calc"> 
                        <svg viewBox="0 0 200 200">
                            <circle cx="100" cy="100" r="70" />
                        </svg> 
                        <svg viewBox="0 0 200 200">
                            <circle cx="100" cy="100" r="70" stroke-dashoffset="{{ calc }}" />
                        </svg> 
                        <h2 class="datapourcent">
                            <a href="/explore/dataset/resume-statistique-communes-departements-et-regions-france-2012-2013-2014/">{{ (items[0].fields.chomeurs_15_64_ans_en_2012 * 100) / items[0].fields.pop_15_64_ans_en_2012 | number:2 }} %</a>
                        </h2>
                    </div>
                    <h4 class="center">Insee 2012</h4>
                </div>
            </div>    
        </div>

        <div class="col-md-4 col-sm-6">
            <div class="ods-box" 
                 ods-results="items" 
                 ods-results-context="resumestatistiquecommunesdepartementsetregionsfrance201220132014">
                <div class="datafact" ng-if="items" ng-init="base = items[0].fields.part_des_menages_fiscaux_imposes_en_2012; calc = 439.8 - (439.8 * base/100)">
                    <h3>Part des ménages fiscaux imposés</h3>
                    <div class="progress progresssmall" ng-if="calc"> 
                        <svg viewBox="0 0 200 200">
                            <circle cx="100" cy="100" r="70" />
                        </svg> 
                        <svg viewBox="0 0 200 200">
                            <circle cx="100" cy="100" r="70" stroke-dashoffset="{{ calc }}" />
                        </svg> 
                        <h2 class="datapourcent">
                            <a href="/explore/dataset/resume-statistique-communes-departements-et-regions-france-2012-2013-2014/">{{ items[0].fields.part_des_menages_fiscaux_imposes_en_2012 | number:0 }} %</a>
                        </h2>
                    </div>
                    <h4 class="center">Insee 2012</h4>
                </div>                
            </div>
        </div>

        <div class="col-md-4 col-sm-6">
            <div class="ods-box" 
                 ods-results="items" 
                 ods-results-context="resumestatistiquecommunesdepartementsetregionsfrance201220132014">
                <div class="datafact">
                    <h3>Population</h3>
                    <h2><a href="/explore/dataset/resume-statistique-communes-departements-et-regions-france-2012-2013-2014/">{{ items[0].fields.population_en_2012 | number }}</a></h2>
                    <h4>Insee 2012</h4>
                </div>
            </div>
        </div>
    </div>
</ods-dataset-context>

	
	
```

CSS code:

```css

.datafact {
    text-align: center;
}
.datafact {
    height: 210px;
    width: 250px;
    margin: 0em auto;
    padding: 0.5em 0 0 0;
}
.datafact h2 {
    border: 0;
    font-size: 180%;
    margin: 0;
}
.datafact h3 {
    color: #aa3c44;
    border: 0;
    font-size: 100%;    
}
.datafact h4 {
    color: #aa3c44;
    border: 0;
    font-size: 70%;
    margin: 0;
}


.datapourcent {
    position: absolute;
    top: 3.7rem;
    width: 100%;
}

@-webkit-keyframes 
load { 0% {
    stroke-dashoffset:0
}
}
@-moz-keyframes 
load { 0% {
    stroke-dashoffset:0
}
}
@keyframes 
load { 0% {
    /* empty circle to the value */
    stroke-dashoffset:439.8;
    /* full to circle to the value */
    /*stroke-dashoffset:0;*/
}
}

.progress, .progressline {
    display: inline-block;
    position: relative;
}
.progress svg {
    width: 10rem;
    height: 10rem;
}
.progress svg:nth-child(1) circle {
    fill: none;
    stroke-width: 9;
    stroke-dasharray: 439.8;
    stroke: rgba(128, 128, 128, 0.3);
}
.progress svg:nth-child(2) {
    position: absolute;
    left: 0;
    top: 0;
    transform: rotate(-90deg);
    -webkit-transform: rotate(-90deg);
    -moz-transform: rotate(-90deg);
    -ms-transform: rotate(-90deg);
}
.progress svg:nth-child(2) circle {
    fill: none;
    stroke-width: 6;
    stroke-dasharray: 439.8;
    stroke: rgba(255, 155, 0, 0.9);
    -webkit-animation: load 1.5s;
    -moz-animation: load 1.5s;
    -o-animation: load 1.5s;
    animation: load 1.5s;
}

.progresssmall svg {
    width: 7rem;
    height: 7rem;
}
.progresssmall .datapourcent {
    top: 2.3rem;
}
.progresssmall .datafact h2 {
    font-size: 160%;
}

```