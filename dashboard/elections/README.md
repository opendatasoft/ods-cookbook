### Election dashboard !

 - [Election dashboard here] (https://discovery.opendatasoft.com/pages/apps-elections/)
 
Please find the 2 datasets here :

 - [Main dataset] (https://discovery.opendatasoft.com/explore/dataset/resultats-elections/)
 - [Same dataset with election connector] (https://discovery.opendatasoft.com/explore/dataset/resultats-elections-transpose/)

```html
<div class="container">


    <ods-dataset-context context="resultats,resultats2,resultatsbureau,resultatsrennes"
                         resultatsrennes-dataset="resultats-elections"
                         resultatsrennes-parameters="{'refine.numero_tour': '1','refine.niveau_detail' : 'vi'}"
                         resultats-dataset="resultats-elections"
                         resultats-parameters="{'refine.numero_tour': '1','refine.niveau_detail' : 'li'}"
                         resultats2-dataset="resultats-elections"
                         resultats2-parameters="{'refine.numero_tour': '1','refine.niveau_detail' : 'li'}"
                         resultatsbureau-dataset="resultats-elections"
                         resultatsbureau-parameters="{'refine.numero_tour': '1','refine.niveau_detail' : 'bu','sort':'numero_lieu'}"
                         >

        <div class="row ods-box">

            <div class="col-md-7">

                <h1>
                    Présidentielle 2017 - 1ER tour à Rennes   
                </h1>

                <ods-map style="height:600px"
                         scroll-wheel-zoom="false"
                         basemap="jawg.light">
                    <ods-map-layer context="resultats"
                                   refine-on-click-context="[resultats2,resultatsbureau]"
                                   refine-on-click-resultats2-map-field="nom_lieu"
                                   refine-on-click-resultats2-context-field="nom_lieu"
                                   refine-on-click-resultats2-replace-refine="true"
                                   refine-on-click-resultatsbureau-map-field="nom_lieu"
                                   refine-on-click-resultatsbureau-context-field="nom_lieu"
                                   refine-on-click-resultatsbureau-replace-refine="true"
                                   color="#1E0C33" 
                                   picto="dot" 
                                   show-marker="false"
                                   size="7">
                    </ods-map-layer>
                </ods-map>
            </div>

            <div class="col-md-5">

                <div ng-if="!resultats2.parameters['refine.nom_lieu']">
                    <div class="row">
                        <div class="col-md-12">

                            <div ods-results="items" ods-results-context="resultatsrennes" max="1" ng-repeat="item in items">
                                <h2>
                                    Rennes
                                </h2> 
                                <div class="participation"><span class="metric_name">Participation</span>
                                    <div class="fond_bar" style="width : 100%"><div class="bar" style="width : {{ item.fields.pourcentage_participation }}%"><span class="metric_chiffre "> {{ item.fields.pourcentage_participation }}%</span></div></div>
                                </div>
                                <div class="metrics row">
                                    <div class="metric col-sm-3 col-xs-6">
                                        <span class="metric_chiffre ">{{ item.fields.nb_inscrits | number }}</span>
                                        <span class="metric_name">inscrits</span>
                                    </div>
                                    <div class="metric col-sm-3 col-xs-6">
                                        <span class="metric_chiffre ">{{ item.fields.nb_blanc | number }}</span>
                                        <span class="metric_name">blancs</span>
                                    </div>
                                    <div class="metric col-sm-3 col-xs-6">
                                        <span class="metric_chiffre ">{{ item.fields.nb_nuls | number }}</span>
                                        <span class="metric_name">nuls</span>
                                    </div>
                                    <div class="metric col-sm-3 col-xs-6">
                                        <span class="metric_chiffre ">{{ item.fields.nb_exprimes | number }}</span>
                                        <span class="metric_name">exprimés</span>
                                    </div>

                                </div>   

                            </div>
                        </div>

                        <div class="col-md-12">
                            <ods-dataset-context context="resultatstrirennes"
                                                 resultatstrirennes-dataset="resultats-elections-transpose"
                                                 resultatstrirennes-parameters="{
                                                                                'sort':'nb_voix',
                                                                                'refine.numero_tour': '1',
                                                                                'refine.niveau_detail' : 'vi'
                                                                                }">

                                <div class="col-md-12">

                                    <ods-result-enumerator context="resultatstrirennes" max="20" show-pagination="false">
                                        <div class="candidat">
                                            <span class="name">{{item.fields.candidat}}</span> :<span class="result"> <span class="voix">{{item.fields.nb_voix}} voix </span>/<span class="pourcent"> {{item.fields.pourcentage}}%</span></span>

                                            <div class="fond_bar" style="width : 100%"> <div class="bar" style="width : {{item.fields.pourcentage}}%"></div></div>
                                        </div>   
                                    </ods-result-enumerator>
                                </div>
                            </ods-dataset-context>


                        </div>



                    </div> <div class="alert">  <div>Cliquez sur un lieu de vote pour afficher les résultats par centre de vote !</div></div>


                </div>
                <div ng-if="resultats2.parameters['refine.nom_lieu']">
                    <ods-result-enumerator context="resultats2" max="1" show-pagination="false">
                        Centre de vote : 
                        <h2>
                            {{item.fields.nom_lieu}}
                        </h2> 
                        <adress>
                            <div>{{item.fields.adresse_lieu}}</div>
                            <div>35000 Rennes </div>
                        </adress>
                        <div  class="row">

                            <div class="participation"><span class="metric_name">Participation</span>
                                <div class="fond_bar" style="width : 100%"><div class="bar" style="width : {{ item.fields.pourcentage_participation }}%"><span class="metric_chiffre "> {{ item.fields.pourcentage_participation }}%</span></div></div>
                            </div>

                            <div class="metrics">

                                <div class="metric col-sm-3 col-xs-6">
                                    <span class="metric_chiffre ">{{ item.fields.nb_inscrits | number }}</span>
                                    <span class="metric_name">inscrits</span>
                                </div>
                                <div class="metric col-sm-3 col-xs-6">
                                    <span class="metric_chiffre ">{{ item.fields.nb_blanc | number }}</span>
                                    <span class="metric_name">blancs</span>
                                </div>
                                <div class="metric col-sm-3 col-xs-6">
                                    <span class="metric_chiffre ">{{ item.fields.nb_nuls | number }}</span>
                                    <span class="metric_name">nuls</span>
                                </div>
                                <div class="metric col-sm-3 col-xs-6">
                                    <span class="metric_chiffre ">{{ item.fields.nb_exprimes | number }}</span>
                                    <span class="metric_name">exprimés</span>
                                </div>
                            </div>   
                        </div>

                        <div ng-if="item.fields.nom_lieu">
                            <ods-dataset-context context="resultatstri"
                                                 resultatstri-dataset="resultats-elections-transpose"
                                                 resultatstri-parameters="{
                                                                          'sort':'nb_voix',
                                                                          'refine.numero_tour':'1',
                                                                          'refine.niveau_detail':'li',
                                                                          'refine.nom_lieu':''+item.fields.nom_lieu}">

                                <ods-result-enumerator context="resultatstri" max="20" show-pagination="false">
                                    <div class="candidat">
                                        <span class="name">{{item.fields.candidat}}</span> :<span class="result"> <span class="voix">{{item.fields.nb_voix}} voix </span>/<span class="pourcent"> {{item.fields.pourcentage}}%</span></span>

                                        <div class="fond_bar" style="width : 100%"> <div class="bar" style="width : {{item.fields.pourcentage}}%"></div></div>
                                    </div>    
                                </ods-result-enumerator>
                            </ods-dataset-context>
                        </div>

                    </ods-result-enumerator> <div class="alert_bis">  <div>Les résultats par bureau s'affichent en dessous!</div></div>
                </div>

            </div>
        </div>

        <div class="ods-box row bloc_bureau" ng-init="tab={'numbureau':'toutRennes'}">


            <div ng-if="!resultatsbureau.parameters['refine.nom_lieu']">
                <h3>
                    Cliquez sur un lieu de vote pour afficher les résultats !
                </h3>
            </div>

            <div ng-if="resultatsbureau.parameters['refine.nom_lieu']">   
                <ods-result-enumerator context="resultats2" max="1" show-pagination="false">
                    <h2>
                        Centre de vote : {{item.fields.nom_lieu}}
                    </h2> 
                </ods-result-enumerator>

                <div ods-results="items" ods-results-context="resultatsbureau">

                    <ul class="items tab-links">
                        <li ng-repeat="item in items"
                            class="item ods-button ods-button--primary" ng-class="{'ods-button--custom': tab.numbureau == item.fields.numero_lieu}" 
                            ng-click="tab.numbureau=item.fields.numero_lieu">

                            Bureau N° {{item.fields.numero_lieu}}

                        </li>
                    </ul>


                    <div ng-repeat="item in items" class=" col-md-12 ">          

                        <div ng-if="tab.numbureau == item.fields.numero_lieu" class="row" ng-class="item.fields.numero_lieu">

                            <div class="participation"><span class="metric_name">Participation</span>
                                <div class="fond_bar" style="width : 100%"><div class="bar" style="width : {{ item.fields.pourcentage_participation }}%"><span class="metric_chiffre "> {{ item.fields.pourcentage_participation }}%</span></div></div>
                            </div>

                            <div class="metrics col-md-6">

                                <div class="metric col-sm-3 col-xs-6">
                                    <span class="metric_chiffre ">{{ item.fields.nb_inscrits | number }}</span>
                                    <span class="metric_name">inscrits</span>
                                </div>
                                <div class="metric col-sm-3 col-xs-6">
                                    <span class="metric_chiffre ">{{ item.fields.nb_blanc | number }}</span>
                                    <span class="metric_name">blancs</span>
                                </div>
                                <div class="metric col-sm-3 col-xs-6">
                                    <span class="metric_chiffre ">{{ item.fields.nb_nuls | number }}</span>
                                    <span class="metric_name">nuls</span>
                                </div>
                                <div class="metric col-sm-3 col-xs-6">
                                    <span class="metric_chiffre ">{{ item.fields.nb_exprimes | number }}</span>
                                    <span class="metric_name">exprimés</span>
                                </div>

                            </div>   


                            <div class="candidat_first col-md-6">
                                <ods-dataset-context context="resultatstribureau"
                                                     resultatstribureau-dataset="resultats-elections-transpose"
                                                     resultatstribureau-parameters="{
                                                                                    'sort':'nb_voix',
                                                                                    'refine.numero_tour': '1',
                                                                                    'refine.niveau_detail' : 'bu',
                                                                                    'refine.nom_lieu':''+resultats2.parameters['refine.nom_lieu'],
                                                                                    'refine.numero_lieu':''+item.fields.numero_lieu
                                                                                    }">
                                    <h3>
                                        Candidats
                                    </h3> 
                                    <ods-result-enumerator context="resultatstribureau" max="20" show-pagination="false">
                                        <div class="candidat">
                                            <span class="name">{{item.fields.candidat}}</span> :<span class="result"> <span class="voix">{{item.fields.nb_voix}} voix </span>/<span class="pourcent"> {{item.fields.pourcentage}}%</span></span>

                                            <div class="fond_bar" style="width : 100%"> <div class="bar" style="width : {{item.fields.pourcentage}}%"></div></div>
                                        </div>   
                                    </ods-result-enumerator>
                                </ods-dataset-context>

                            </div>
                        </div>   
                    </div>

                </div>


            </div>
        </div>



    </ods-dataset-context>
</div>
```

```css
.bureau_title {
    text-align:center;
    font-size: 1.4em;
    margin-top: 10px;
}
.metrics {
    border-radius: 3px;
    text-align: center;
}
.metric {
    padding: 2px 5px;
    text-align: center;
    font-size: 1.2em;
    font-weight: 600;
    line-height: 1em;
    display: inline-block;
    float : left;
    margin-bottom : 30px
}
span.metric_name {
    display: block;
    font-size: 0.8em;
    font-weight: 600;
    font-family: "archive", verdana;
    border-bottom : 1px solid #E6174E;
    padding : 1px;

}
span.metric_chiffre {
    font-weight: 600;
    color: #E6174E;
    font-size : 1.2em;
    font-family: "archive", verdana;
}
div.fond_bar{
    background-color : #cecece;

    height : 5px;

}
div.bar{
    background-color : #000;
    height : 5px;
}
.participation div.fond_bar{
    background-color : #cecece;
    height : 25px;
    border-radius : 2px;

}
.participation {
    margin-bottom : 10px;
}
.participation div.bar{
    background-color : #E6174E;
    height : 25px;
    border-radius : 2px 0 0 2px;
}
span.name{
    margin-top : 20px;

    font-family: "archive", verdana;
}
span.result{
    float : right ;
    color : #000;
    font-weight : bold;
    font-size : 1.0em;
}
.bloc_bureau{
    min-height: 485px;
}
.candidat{
    padding-bottom : 7px;
    line-height: 1.1em;
}
adress {
    font-weight: 600;
    width: 300px;
    height: 80px;
    display: inline-block;
    background: url("/assets/theme_image/geoloc.png") no-repeat;
    text-indent : 60px;
}

ul.tab-links{
    padding-left : 0px !important;
    margin-left : 0px !important;

}
ul.tab-links li{
    margin : 0px !important;

}
.ods-button--primary {
    background-color : #cecece;
    border : 1px solid #fff;
    border-bottom : none;
    color : #000000;
    border-radius : 3px 3px 0 0;
}
.ods-button--custom {
    background-color: #1e0c33;
    color: white;
}

.participation .metric_chiffre{
    color : #fff; float : right;padding-right : 5px;font-weight : normal !important;
}
.participation .metric_name{
    text-align : left;
}

.bureau {
    border : 1px solid  rgba(0,0,0,0.15);
    border-radius: 3px;

}
h2 {
    margin-top: 0;
}

.pourcent { 
    color: #E6174E; 
    font-weight : 1.2em;
}

.alert{
    margin-top : 20px;
    height: 66px;
    display: inline-block;
    background: url("/assets/theme_image/fleche.png") 5px 18px no-repeat ;
    font-family: "archive", verdana;

    background-color : #f5f5f5;
    padding :7px  17px;

}
.alert_bis{
    margin-top : 20px;
    height: 66px;
    display: inline-block;
    background: url("/assets/theme_image/fleche_bis.png") 15px 2px no-repeat ;
    font-family: "archive", verdana;

    background-color : #f5f5f5;
    padding :7px  17px;

}
.alert div, .alert_bis div {padding-left : 88px; padding-top : 7px; }

```
