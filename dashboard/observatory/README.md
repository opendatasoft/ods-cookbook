# The observatory by OpenDataSoft !

#### Live result

[Please find the live exemple on Discovery](https://discovery.opendatasoft.com/pages/apps-observatory/)

#### Code

```html
<ods-dataset-context context="limitecommune"
                     limitecommune-dataset="geoflar-communes-2015"
                     limitecommune-domain="public">

    <div class="container">

        <h1 class="titre">
            L'observatoire <span class="smaller">by OpenDataSoft</span>
        </h1>

        <div class="recherche">
            <div class="recherche-titre">
                <h3>Recherchez votre commune pour affiner les données</h3> 
            </div>


            <div ng-if="limitecommune.parameters['refine.insee_com']">
                <i><a href="#" ng-click="
                    limitecommune.parameters['refine.insee_com'] = undefined;
                    limitecommune.parameters['refine.nom_com'] = undefined;
                    limitecommune.parameters['q'] = undefined">Supprimer le filtre</a></i>
            </div>        
            <ods-text-search
                             placeholder="Nom de la commune"
                             button="Rechercher"
                             field="nom_com"
                             context="limitecommune"
                             ng-if="!limitecommune.parameters['refine.insee_com']">
            </ods-text-search>
            <div ng-if="limitecommune.parameters['q'] || limitecommune.parameters['refine.insee_com']">
                <ods-result-enumerator
                                       context="limitecommune"
                                       max="10"
                                       show-pagination="false">
                    <div>
                        <div ng-if="!context.parameters['refine.insee_com']">
                            <a href="#" ng-click="context.parameters['refine.insee_com'] = item.fields.insee_com;
                                                  context.parameters['refine.nom_com'] = item.fields.nom_com">
                                {{item.fields.nom_com}} <small>({{item.fields.nom_dept}}, {{item.fields.nom_reg}})</small>
                            </a>
                        </div>
                        <div ng-if="context.parameters['refine.insee_com']">
                            {{item.fields.nom_com}} <small>({{item.fields.nom_dept}}, {{item.fields.nom_reg}})</small>
                        </div>
                    </div>
                </ods-result-enumerator>                   
            </div>

            <ods-tabs>

                <ods-pane title="Vue analytique" icon="pie-chart" pane-auto-unload="true">

                    <ods-dataset-context context="ctx1,ctx2,ctx3,ctx4a,ctx4b,ctx5,stats" 
                                         ctx1-dataset="evolution-et-structure-de-la-population-france-2012-categories-socio-professionn" 
                                         ctx1-domain="public"
                                         ctx1-parameters="{'q':'NOT csp:total','refine.sexe':'Total'}"

                                         ctx2-dataset="couverture-2g-3g-4g-en-france-par-operateur-juillet-2015"
                                         ctx2-domain="public"

                                         ctx3-domain="public"
                                         ctx3-dataset="population-active-25-54-ans-par-sexe-et-activite-1968-2011"

                                         ctx4a-dataset="deces-par-commune-departement-et-region-de-2003-a-2013" 
                                         ctx4b-dataset="naissances-par-commune-departement-et-region-de-2003-a-2013"

                                         ctx5-dataset="sirene" 
                                         ctx5-domain="public"
                                         ctx5-parameters="{'q.code':'9311Z OR 9312Z OR 9313Z OR 9319Z OR 9321 OR 9329Z OR 4764Z OR 8551Z OR 7721Z OR 5010Z OR 5030Z',
                                                          'q.date':'date_deb_etat_adm_et >= 1920'}"

                                         stats-dataset="resume-statistique-communes-departements-et-regions-france-2012-2013-2014" 
                                         stats-domain="public">


                        {{ 
                        ctx1.parameters['refine.code_geographique'] = limitecommune.parameters['refine.insee_com'] ;
                        ctx2.parameters['refine.code_insee'] = limitecommune.parameters['refine.insee_com'] ;
                        ctx3.parameters['refine.code_commune'] = limitecommune.parameters['refine.insee_com'] ;
                        ctx4a.parameters['refine.depcom'] = limitecommune.parameters['refine.insee_com'] ;
                        ctx4b.parameters['refine.depcom'] = limitecommune.parameters['refine.insee_com'] ;
                        ctx5.parameters['q'] = limitecommune.parameters['refine.insee_com']?'depcomen:'+limitecommune.parameters['refine.insee_com']:undefined ;
                        stats.parameters['refine.codgeo'] = limitecommune.parameters['refine.insee_com'] ;
                        ""
                        }}


                        <div class="row">
                            <div class="box col-md-4">
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Population
                                    </h2>
                                    <h3 class="description">
                                        en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="population_en_2012">
                                        {{ agg | number }}
                                    </p>
                                </div>
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Nombre de ménages
                                    </h2>
                                    <h3 class="description">
                                        en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="menages_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                            </div>

                            <div class="box col-md-8">
                                <div class="grey-box">
                                    <h2 class="title">
                                        Evolution et structure de la population
                                    </h2>
                                    <h3 class="description">
                                        France 2012 - Catégories socio-professionnelles
                                    </h3>
                                    <ods-chart>
                                        <ods-chart-query context="ctx1" field-x="csp" series-breakdown="tranche_dage">
                                            <ods-chart-serie expression-y="value" chart-type="column" function-y="SUM" color="range-custom" scientific-display="true">
                                            </ods-chart-serie>
                                        </ods-chart-query>
                                    </ods-chart>
                                </div>
                            </div>
                        </div>

                        <div class="row">

                            <div class="box col-md-6">
                                <div class="grey-box">
                                    <h2 class="title">
                                        Couverture 2G, 3G, 4G
                                    </h2>
                                    <h3 class="description">
                                        Couverture en France par opérateur - Juillet 2015
                                    </h3>
                                    <ods-chart>
                                        <ods-chart-query context="ctx2" field-x="operateur" maxpoints="50" series-breakdown="reseau">
                                            <ods-chart-serie expression-y="couverture" chart-type="column" function-y="AVG" color="range-custom" scientific-display="true">
                                            </ods-chart-serie>
                                        </ods-chart-query>
                                    </ods-chart>
                                </div>
                            </div>
                            <div class="box col-md-6">
                                <div class="grey-box">
                                    <h2 class="title">
                                        Naissances et Décès
                                    </h2>
                                    <h3 class="description">
                                        de 2003 à 2013
                                    </h3>
                                    <ods-chart timescale="year" single-y-axis="true" single-y-axis-label="Comparaison naissances et décès">
                                        <ods-chart-query context="ctx4a" field-x="annee" timescale="year">
                                            <ods-chart-serie expression-y="nombre_deces" chart-type="areaspline" function-y="SUM" label-y="Décès" color="#16212B" scientific-display="true">
                                            </ods-chart-serie>
                                        </ods-chart-query>
                                        <ods-chart-query context="ctx4b" field-x="annee" timescale="year">
                                            <ods-chart-serie expression-y="naissances" chart-type="areaspline" function-y="SUM" label-y="Naissances" color="#1AA6C4" scientific-display="true">
                                            </ods-chart-serie>
                                        </ods-chart-query>
                                    </ods-chart>
                                </div>
                            </div>

                        </div>


                        <div class="row">

                            <div class="box col-md-8">
                                <div class="grey-box">
                                    <h2 class="title">
                                        Population active
                                    </h2>
                                    <h3 class="description">
                                        Tranche 25-54 ans par sexe et activité 1968 - 2011
                                    </h3>

                                    <ods-chart single-y-axis="true">
                                        <ods-chart-query context="ctx3" field-x="annee" maxpoints="50">
                                            <ods-chart-serie expression-y="hommes_actifs_ayant_un_emploi" chart-type="column" function-y="SUM" color="#EC643C" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="hommes_chomeurs" chart-type="column" function-y="SUM" color="#AA3C44" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="femmes_actifs_ayant_un_emploi" chart-type="column" function-y="SUM" color="#1B6698" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="femmes_chomeurs" chart-type="column" function-y="SUM" color="#17A2A2" scientific-display="true">
                                            </ods-chart-serie>
                                        </ods-chart-query>
                                    </ods-chart>
                                </div>
                            </div>
                            <div class="box col-md-4">
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Actifs
                                    </h2>
                                    <h3 class="description">
                                        15 - 64 ans en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="actifs_15_64_ans_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Chomeurs
                                    </h2>
                                    <h3 class="description">
                                        15 - 64 ans en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="chomeurs_15_64_ans_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                            </div>
                        </div>



                        <div class="row">

                            <div class="box col-md-12">
                                <div class="grey-box">
                                    <h2 class="title">
                                        Base SIRENE
                                    </h2>
                                    <h3 class="description">
                                        Création d'entreprise en France par année (à partir de 1920)
                                    </h3>
                                    <ods-chart timescale="year">
                                        <ods-chart-query context="ctx5" field-x="date_deb_etat_adm_et" timescale="year">
                                            <ods-chart-serie chart-type="column" label-y="Nombre d'entreprise" function-y="COUNT" color="#1B6698" scientific-display="true">
                                            </ods-chart-serie>
                                        </ods-chart-query>
                                    </ods-chart>
                                </div>
                            </div>
                        </div>


                        <div class="row">
                            <div class="box col-md-12">
                                <h2 class="grey-box">
                                    Logements
                                </h2>
                            </div>
                        </div>

                        <div class="row">

                            <div class="box col-md-4">
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Nombre de logements
                                    </h2>
                                    <h3 class="description">
                                        en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="logements_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                            </div>
                            <div class="box col-md-4">
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Résidences principales
                                    </h2>
                                    <h3 class="description">
                                        en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="residences_principales_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                            </div>
                            <div class="box col-md-4">
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Résidences secondaires et logts occasionnels
                                    </h2>
                                    <h3 class="description">
                                        en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="res_secondaires_et_logts_occasionnels_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="box col-md-12">
                                <h2 class="grey-box">
                                    Ménages fiscaux
                                </h2>
                            </div>
                        </div>

                        <div class="row">

                            <div class="box col-md-4">
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Nombre de ménages fiscaux
                                    </h2>
                                    <h3 class="description">
                                        en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="nombre_de_menages_fiscaux_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                            </div>
                            <div class="box col-md-4">
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Part des ménages fiscaux imposés
                                    </h2>
                                    <h3 class="description">
                                        en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="part_des_menages_fiscaux_imposes_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                            </div>
                            <div class="box col-md-4">
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Mediane du revenu disponible par US
                                    </h2>
                                    <h3 class="description">
                                        en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="AVG" 
                                       ods-aggregation-expression="mediane_du_revenu_disponible_par_uc_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                            </div>
                        </div>


                        <div class="row">
                            <div class="box col-md-12">
                                <h2 class="grey-box">
                                    Divers
                                </h2>
                            </div>
                        </div>

                        <div class="row">

                            <div class="box col-md-4">
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Taux de pauvreté
                                    </h2>
                                    <h3 class="description">
                                        en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="taux_de_pauvrete_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                            </div>
                            <div class="box col-md-4">
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Emplois au LT
                                    </h2>
                                    <h3 class="description">
                                        en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="emplois_au_lt_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                            </div>
                            <div class="box col-md-4">
                                <div class="grey-box half-box">
                                    <h2 class="title">
                                        Emplois salariés au LT
                                    </h2>
                                    <h3 class="description">
                                        en 2012
                                    </h3>
                                    <p class="kpi" 
                                       ods-aggregation="agg"
                                       ods-aggregation-context="stats" 
                                       ods-aggregation-function="SUM" 
                                       ods-aggregation-expression="emplois_salaries_au_lt_en_2012">
                                        {{ agg | number : 0 }}
                                    </p>
                                </div>
                            </div>
                        </div>

                    </ods-dataset-context>


                </ods-pane>

                <ods-pane title="Vue carte" icon="map" pane-auto-unload="true">

                    <!--div class="row">
                        <div class="box col-md-12">
                            <div class="grey-box" style="height: inherit;">
                                <h2 class="title">
                                    Couches de données proposées
                                </h2>
                                <ul>
                                    <li>
                                        <b>Base SIRENE</b> Entreprises dont l'activité est lié à la pratique d'une activité sportive, la formation ou la vente d'équipement sportif. <i>Source : INSEE</i>
                                    </li>
                                    <li>
                                        <b>Equipement sport et loisir</b> Liste des équipements de sport et de loisir en France, à la précision maille IRIS. <i>Source : INSEE</i>
                                    </li>
                                    <li>
                                        <b>Immatriculation 2016+</b> Liste des entreprises immatriculées à partir du 1 janvier 2016. <i>Source : data.infogreffe</i>
                                    </li>
                                    <li>
                                        <b>Etablissements sup.</b> Implantations des établissements d'enseignement supérieur publics
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div-->

                    <div class="row" ng-init="maptab = 'first'">
                        <div class="box col-md-12">
                            <div class="grey-box" style="height: inherit;">

                                <div class="items">
                                    <div class="item" 
                                         ng-class="{'item_selected': maptab == 'first'}" 
                                         ng-click="maptab='first'">
                                        Base SIRENE 
                                        <i translate="ods-tooltip" ods-tooltip="Entreprises dont l'activité est lié à la pratique d'une activité sportive, la formation ou la vente d'équipement sportif. <i>Source : INSEE</i>" class="fa fa-info-circle ods-form__help-icon"></i>
                                    </div>
                                    <div class="item" 
                                         ng-class="{'item_selected': maptab == 'second'}" 
                                         ng-click="maptab='second'">
                                        Equipement sport et loisir 
                                        <i translate="ods-tooltip" ods-tooltip="Liste des équipements de sport et de loisir en France, à la précision maille IRIS. <i>Source : INSEE</i>" class="fa fa-info-circle ods-form__help-icon"></i>
                                    </div>
                                    <div class="item" 
                                         ng-class="{'item_selected': maptab == 'third'}" 
                                         ng-click="maptab='third'">
                                        Immatriculation 2016+ 
                                        <i translate="ods-tooltip" ods-tooltip="Liste des entreprises immatriculées à partir du 1 janvier 2016. <i>Source : data.infogreffe</i>" class="fa fa-info-circle ods-form__help-icon"></i>
                                    </div>
                                    <div class="item" 
                                         ng-class="{'item_selected': maptab == 'fourth'}" 
                                         ng-click="maptab='fourth'">
                                        Etablissements sup. 
                                        <i translate="ods-tooltip" ods-tooltip="Implantations des établissements d'enseignement supérieur publics" class="fa fa-info-circle ods-form__help-icon"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>


                    <ods-dataset-context context="sirenepublic,localequipementsportloisirparcommunes2014,entreprisesimmatriculees2016infogreffe,entreprisesimmatriculees2017infogreffe,fresrimplantationsetablissementsdenseignementsuperieurpublicsmesr" 

                                         sirenepublic-dataset="sirene@public" 
                                         sirenepublic-parameters="{'q.code':'9311Z OR 9312Z OR 9313Z OR 9319Z OR 9321 OR 9329Z OR 4764Z OR 8551Z OR 7721Z OR 5010Z OR 5030Z'}"

                                         localequipementsportloisirparcommunes2014-dataset="equip-sport-loisir-socio-infra-2014@public"

                                         entreprisesimmatriculees2016infogreffe-dataset="entreprises-immatriculees-2016"
                                         entreprisesimmatriculees2016infogreffe-domain="infogreffe"
                                         entreprisesimmatriculees2016infogreffe-parameters="{'sort':'date_immatriculation','q.code':'9311Z OR 9312Z OR 9313Z OR 9319Z OR 9321 OR 9329Z OR 4764Z OR 8551Z OR 7721Z OR 5010Z OR 5030Z'}" 

                                         entreprisesimmatriculees2017infogreffe-dataset="entreprises-immatriculees-2017"
                                         entreprisesimmatriculees2017infogreffe-domain="infogreffe"
                                         entreprisesimmatriculees2017infogreffe-parameters="{'sort':'date_immatriculation','q.code':'9311Z OR 9312Z OR 9313Z OR 9319Z OR 9321 OR 9329Z OR 4764Z OR 8551Z OR 7721Z OR 5010Z OR 5030Z'}"

                                         fresrimplantationsetablissementsdenseignementsuperieurpublicsmesr-dataset="fr-esr-implantations_etablissements_d_enseignement_superieur_publics@mesr"k>
                        <div class="row">
                            <div class="box col-md-12">
                                <div class="grey-box" style="height: 500px; padding: 0">
                                    <ods-map style="height: 500px"
                                             search-box="false" no-refit="true" toolbar-geolocation="true" basemap="jawg.light" location="6,46.50595,2.40601">
                                        <ods-map-layer context="limitecommune" show-if="maptab != 'second'"></ods-map-layer>

                                        <ods-map-layer context="sirenepublic" color="#0B72B5" picto="dot" show-marker="false" display="auto" shape-opacity="0.5" point-opacity="1" border-color="#FFFFFF" caption="true" caption-title="Base SIRENE - Sport" size="7" size-min="3" size-max="5" size-function="linear" show-if="maptab == 'first'"></ods-map-layer>

                                        <ods-map-layer context="localequipementsportloisirparcommunes2014" color="#C32D1C" picto="ods-circle" show-marker="true" display="auto" shape-opacity="0.5" point-opacity="1" border-color="#FFFFFF" caption="true" size="4" size-min="3" size-max="5" size-function="linear" show-if="maptab == 'second'">
                                            <div>
                                                <ods-dataset-context context="local" local-dataset="equip-sport-loisir-socio-infra-2014@public">
                                                    <h2>
                                                        {{ record.fields.libelle_de_commune }}
                                                    </h2>
                                                    <h3>
                                                        IRIS {{ record.fields.libelle_de_l_iris }}
                                                    </h3>
                                                    <br/>
                                                    <div ng-if="!(field.name == 'p12_pop') && field.type == 'double' && record.fields[field.name] > 0" ng-repeat="field in local.dataset.fields">
                                                        <span style="color: grey">{{ field.label }}</span> 
                                                        <span style="color: black; font-size: 1.1em; font-weight: 500;">{{ record.fields[field.name] }}</span>
                                                    </div>
                                                </ods-dataset-context>
                                            </div>
                                        </ods-map-layer>

                                        <ods-map-layer context="entreprisesimmatriculees2016infogreffe" color="#2C3F56" picto="ods-circle" show-marker="true" display="auto" shape-opacity="0.5" point-opacity="1" border-color="#FFFFFF" caption="true" size="4" size-min="3" size-max="5" size-function="linear" show-if="maptab == 'third'"></ods-map-layer>
                                        <ods-map-layer context="entreprisesimmatriculees2017infogreffe" color="#555555" picto="ods-circle" show-marker="true" display="auto" shape-opacity="0.5" point-opacity="1" border-color="#FFFFFF" caption="true" size="4" size-min="3" size-max="5" size-function="linear" show-if="maptab == 'third'"></ods-map-layer>

                                        <ods-map-layer context="fresrimplantationsetablissementsdenseignementsuperieurpublicsmesr" show-if="maptab == 'fourth'"></ods-map-layer>
                                    </ods-map>
                                </div>
                            </div>
                        </div>

                        <div class="row" ng-if="maptab == 'first'">
                            <div class="box col-md-12">
                                <div class="grey-box">
                                    <h2 class="title">
                                        Principaux type d'activité des entreprises
                                    </h2>
                                    <ods-chart>
                                        <ods-chart-query context="sirenepublic" field-x="libapen" maxpoints="50" sort="serie1-1">
                                            <ods-chart-serie chart-type="pie" function-y="COUNT" color="range-custom" scientific-display="true">
                                            </ods-chart-serie>
                                        </ods-chart-query>
                                    </ods-chart>
                                </div>
                            </div>
                        </div>

                        <div class="row" ng-if="maptab == 'first'">
                            <div class="box col-md-12">    
                                <div class="grey-box">
                                    <h2 class="title">
                                        Liste des entreprises
                                    </h2>
                                    <ods-table context="sirenepublic"></ods-table>
                                </div>
                            </div>
                        </div>

                        <div class="row" ng-if="maptab == 'second'">
                            <div class="box col-md-12">
                                <div class="grey-box">

                                    <h2 class="title">
                                        Cumul du nombre d'équipement par région
                                    </h2>
                                    <ods-chart single-y-axis="true">
                                        <ods-chart-query context="localequipementsportloisirparcommunes2014" field-x="region" maxpoints="50" stacked="normal">
                                            <ods-chart-serie expression-y="bassin_de_natation" chart-type="column" function-y="SUM" color="#2C3F56" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="boulodrome" chart-type="column" function-y="SUM" color="#EC643C" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="tennis" chart-type="column" function-y="SUM" color="#ABCED9" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="equipement_de_cyclisme" chart-type="column" function-y="SUM" color="#D05356" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="domaine_skiable" chart-type="column" function-y="SUM" color="#1B6698" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="centre_equestre" chart-type="column" function-y="SUM" color="#4F8F55" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="athletisme" chart-type="column" function-y="SUM" color="#17A2A2" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="terrain_de_golf" chart-type="column" function-y="SUM" color="#E8AF55" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="parcours_sportif_sante" chart-type="column" function-y="SUM" color="#AA3C44" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="sports_de_glace" chart-type="column" function-y="SUM" color="#2C3F56" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="plateaux_et_terrains_de_jeux_exterieurs" chart-type="column" function-y="SUM" color="#EC643C" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="salles_specialisees" chart-type="column" function-y="SUM" color="#ABCED9" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="salles_non_specialisees" chart-type="column" function-y="SUM" color="#D05356" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="terrains_de_grands_jeux" chart-type="column" function-y="SUM" color="#1B6698" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="salles_de_combat" chart-type="column" function-y="SUM" color="#4F8F55" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="roller_skate_velo_bicross_ou_freestyle" chart-type="column" function-y="SUM" color="#17A2A2" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="sports_nautiques" chart-type="column" function-y="SUM" color="#E8AF55" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="bowling" chart-type="column" function-y="SUM" color="#AA3C44" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="salles_de_remises_en_forme" chart-type="column" function-y="SUM" color="#2C3F56" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="salles_multisports_gymnase" chart-type="column" function-y="SUM" color="#EC643C" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="baignade_amenagee" chart-type="column" function-y="SUM" color="#ABCED9" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="port_de_plaisance_mouillage" chart-type="column" function-y="SUM" color="#D05356" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="boucle_de_randonnee" chart-type="column" function-y="SUM" color="#1B6698" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="cinema" chart-type="column" function-y="SUM" color="#4F8F55" scientific-display="true">
                                            </ods-chart-serie>
                                            <ods-chart-serie expression-y="theatre" chart-type="column" function-y="SUM" color="#17A2A2" scientific-display="true">
                                            </ods-chart-serie>
                                        </ods-chart-query>
                                    </ods-chart>
                                </div>
                            </div>
                        </div>

                        <div class="row" ng-if="maptab == 'second'">
                            <div class="box col-md-12">
                                <div class="grey-box">
                                    <h2 class="title">
                                        Liste des mailles IRIS
                                    </h2>
                                    <ods-table context="localequipementsportloisirparcommunes2014"></ods-table>
                                </div>
                            </div>
                        </div>


                        <div class="row" ng-if="maptab == 'third'">
                            <div class="box col-md-12">
                                <div class="grey-box">
                                    <h2 class="title">
                                        Evolution de la création d'entreprise depuis 2016
                                    </h2>
                                    <ods-chart timescale="month">
                                        <ods-chart-query context="entreprisesimmatriculees2016infogreffe" field-x="date_immatriculation" timescale="month">
                                            <ods-chart-serie chart-type="column" function-y="COUNT" label-y="2016" color="#b3b3b3" scientific-display="true">
                                            </ods-chart-serie>
                                        </ods-chart-query>
                                        <ods-chart-query context="entreprisesimmatriculees2017infogreffe" field-x="date_immatriculation" timescale="month">
                                            <ods-chart-serie chart-type="column" function-y="COUNT" label-y="2017" color="#555555" scientific-display="true">
                                            </ods-chart-serie>
                                        </ods-chart-query>
                                    </ods-chart>
                                </div>
                            </div>
                        </div>

                        <div class="row" ng-if="maptab == 'fourth'">
                            <div class="box col-md-12">
                                <div class="grey-box">
                                    <h2 class="title">
                                        Type d'établissement
                                    </h2>
                                    <ods-chart>
                                        <ods-chart-query context="fresrimplantationsetablissementsdenseignementsuperieurpublicsmesr" field-x="bcnag_n_type_uai_libelle_edition" maxpoints="50" sort="serie1-1">
                                            <ods-chart-serie expression-y="effectif" chart-type="pie" function-y="AVG" color="range-Set1" scientific-display="true">
                                            </ods-chart-serie>
                                        </ods-chart-query>
                                    </ods-chart>
                                </div>
                            </div>
                        </div>

                        <div class="row" ng-if="maptab == 'fourth'">
                            <div class="box col-md-12">
                                <div class="grey-box">
                                    <h2 class="title">
                                        Liste des établissements
                                    </h2>
                                    <ods-table context="fresrimplantationsetablissementsdenseignementsuperieurpublicsmesr"></ods-table>
                                </div>
                            </div>
                        </div>

                    </ods-dataset-context>

                </ods-pane>

            </ods-tabs>
        </div>
    </div>

</ods-dataset-context>
```

```css
h1 .smaller {
    font-size: 0.5em;
}
h2 .smaller {
    font-size: 0.8em;
}
.ods-box {
    border-radius: 0px;
}
.titre {
    border-bottom: 1px solid black;
    width: 264px;
}

/* SEARCH */
.odswidget-text-search__search-box {
    font-size: 1.0rem;
    padding-top: 4px;
    padding-bottom: 3px;
}
.recherche {
    margin-bottom: 20px;
}


/* TABS */
.items {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: -8px;
}
.item {
    margin: 0px 15px 8px 0px;
    border-radius: 0px;
    font-size: 1.2em;
    padding: 1px 5px;
    font-family: 'Oswald', "Open Sans", Helvetica, arial, sans-serif;
    font-weight: 100;
    color: #666666;
    border-left: 1px solid #666;
    border-bottom: 1px solid #666;
}
.item:hover {
    border-left: 2px solid #ec643c;
    border-bottom: 2px solid #ec643c;
    padding-left: 4px;
}
.item_selected, .item_selected:hover {
    border-left: 2px solid black;
    border-bottom: 2px solid black;
    color: black;
    padding-left: 5px;
}

.ods-tabs__tab {
    color: black;
}

/* BOX */
.box {
    padding-left: 3px;
    padding-right: 3px;
}
.grey-box {
    background: #eee;
    border-radius: 0;
    padding: 20px;
    margin-bottom: 6px;
    height: 418px;
}
.grey-box.half-box {
    height: 206px;
}

/* BOX CONTENT */
.title {
    font-size: 1em;
    margin: 0 auto;
}
.description {
    margin: 0 auto;
    color: grey;
    font-size: 0.7em;
    font-weight: 100;
}
.kpi {
    font-size: 1.66em;
    margin-top: 40px;
    font-weight: 500;
    text-align: center;
}
/* BOX Title Line */
h2.grey-box {
    height: 70px;
    font-size: 1.3em;
}

/* CHARTS */
.ods-chart {
    height: 350px;
}
.odswidget-charts {
    margin-top: 10px;
}
.odswidget-table {
    height: 338px;
    margin-top: 10px;
}
rect.highcharts-background {
    fill: #eee !important;
}
```