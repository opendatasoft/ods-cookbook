### How to reproduce the [MaVille](http://lille.data.opendatasoft.com) Dashboard

#### Datasets to add to your domain

First you need to add this list of datasets on your domain:

* entreprises-immatriculees-en-2015
* entreprises-radiees-en-2015
* repartition-des-emplois-sur-le-territoire-france-1982-1990-1999-2007-2012
* deces-par-commune-departement-et-region-de-2003-a-2013
* equipement-sport-loisir-par-communes-2014-iris
* equipements-services-tourisme-transport-2014-iris
* equipements-services-enseignement-superieur-2014-iris
* nombre-de-fonctions-medicales-et-paramedicales-2014-iris
* balance_communes
* offres-demploi-anonymisees
* delinquance-2014-en-france
* statistiques-immatriculations
* pop-active-25-54-csp-activite-1968-2011
* resume-statistique-communes-departements-et-regions-france-2012-2013-2014
* naissances-par-commune-departement-et-region-de-2003-a-2013
* evolution-et-structure-de-la-population-france-csp-2012
* couverture-2g-3g-4g-en-france-par-operateur-juillet-2015
* fr-esr-sise-effectifs-d-etudiants-inscrits-esr-public

You can simply use the `Add a dataset from the OpenDataSoft network` button when you add a new source of data.

#### Dashboard

Then you can create a page from the administration panel, and, when editing in expert mode, paste the following code.

HTML code:

```html
	<div class="container">
	    <div id="page-layout-single-main" class="page-layout">
    	    <div class="row">
	            <div id="cityhour">
        	        <h1>Castres</h1>
            	    <h4>Ce portail a été généré automatiquement et avec &hearts; par <a style="color: #abced9" href="https://www.opendatasoft.com/">OpenDataSoft</a>
	            	</h4>
	            </div>
	     	</div>
	     <ods-dataset-context context="resumestatistiquecommunesdepartementsetregionsfrance201220132014" 
	                          resumestatistiquecommunesdepartementsetregionsfrance201220132014-dataset="resume-statistique-communes-departements-et-regions-france-2012-2013-2014" 
	                          resumestatistiquecommunesdepartementsetregionsfrance201220132014-parameters="{}">
	         <div class="row">
	             <div class="col-md-4 col-sm-6">
	                 <div class="ods-box datafact" 
	                      ods-results="items" 
	                      ods-results-context="resumestatistiquecommunesdepartementsetregionsfrance201220132014">
	                     <h3>Population</h3>
	                     <h2><a href="/explore/dataset/resume-statistique-communes-departements-et-regions-france-2012-2013-2014/">{{ items[0].fields.population_en_2012 | number }}</a></h2>
	                     <h4>Insee 2012</h4>
	                 </div>
	             </div>
	             <div class="col-md-4 col-sm-6">
	                 <div class="ods-box datafact" 
	                      ods-results="items" 
	                      ods-results-context="resumestatistiquecommunesdepartementsetregionsfrance201220132014">
	                     <h3>Part des ménages fiscaux imposés</h3>
	                     <h2><a href="/explore/dataset/resume-statistique-communes-departements-et-regions-france-2012-2013-2014/">{{ items[0].fields.part_des_menages_fiscaux_imposes_en_2012 | number:0 }} %</a></h2>
	                     <h4>Insee 2012</h4>
	                 </div>
	             </div>
	             <div class="col-md-4 col-sm-6">
	                 <div class="ods-box datafact" 
	                      ods-results="items" 
	                      ods-results-context="resumestatistiquecommunesdepartementsetregionsfrance201220132014">
	                     <h3>Taux de Chômage</h3>
	                     <h2><a href="/explore/dataset/resume-statistique-communes-departements-et-regions-france-2012-2013-2014/">{{ (items[0].fields.chomeurs_15_64_ans_en_2012 * 100) / items[0].fields.pop_15_64_ans_en_2012 | number:2 }} %</a></h2>
	                     <h4>Insee 2012</h4>
	                 </div>    
	             </div>
	             <div class="col-md-4 col-sm-6">
	                 <div class="ods-box datafact" 
	                      ods-results="items" 
	                      ods-results-context="resumestatistiquecommunesdepartementsetregionsfrance201220132014">
	                     <h3>Logements vacants</h3>
	                     <h2><a href="/explore/dataset/resume-statistique-communes-departements-et-regions-france-2012-2013-2014/">{{ items[0].fields.logements_vacants_en_2012 | number:0 }}</a></h2>
	                     <h4>Insee 2012</h4>
	                 </div>
	             </div>
	             <div class="col-md-4 col-sm-6">
	                 <div class="ods-box datafact" 
	                      ods-results="items" 
	                      ods-results-context="resumestatistiquecommunesdepartementsetregionsfrance201220132014">
	                     <h3>Etablissements de 10+ salariés</h3>
	                     <h2><a href="/explore/dataset/resume-statistique-communes-departements-et-regions-france-2012-2013-2014/">{{ items[0].fields.ets_actifs_10_salaries_ou_plus_au_31_decembre_2012 | number }}</a></h2>
	                     <h4>Insee 2012</h4>
	                 </div>
	             </div>
	             <div class="col-md-4 col-sm-6">
	                 <div class="ods-box datafact" 
	                      ods-results="items" 
	                      ods-results-context="resumestatistiquecommunesdepartementsetregionsfrance201220132014">
	                     <h3>Etablissements de 1-9 salariés</h3>
	                     <h2><a href="/explore/dataset/resume-statistique-communes-departements-et-regions-france-2012-2013-2014/">{{ items[0].fields.ets_actifs_de_1_a_9_salaries_au_31_decembre_2012 | number }}</a></h2>
	                     <h4>Insee 2012</h4>
	                 </div>   
	             </div>
	         </div>
	     </ods-dataset-context>    
	     <div class="row">
	         <div class="col-md-6 col-sm-12">
	             <div class="ods-box">
	                 <h3>Décès et Naissances <a href="/explore/?q=publisher:INSEE+AND+(décès+OR+naissances)"><i class="icon-external-link-sign"></i></a></h3>
	                 <ods-dataset-context context="naissancesparcommunedepartementetregionde2003a2013,decesparcommunedepartementetregionde2003a2013" 
	                                      naissancesparcommunedepartementetregionde2003a2013-dataset="naissances-par-commune-departement-et-region-de-2003-a-2013" 
	                                      naissancesparcommunedepartementetregionde2003a2013-parameters="{'source':''}" 
	                                      decesparcommunedepartementetregionde2003a2013-dataset="deces-par-commune-departement-et-region-de-2003-a-2013" 
	                                      decesparcommunedepartementetregionde2003a2013-parameters="{'source':''}">
	                     <ods-chart timescale="year" 
	                                single-y-axis="true">
	                         <ods-chart-query context="naissancesparcommunedepartementetregionde2003a2013" 
	                                          field-x="annee" 
	                                          timescale="year">
	                             <ods-chart-serie expression-y="naissances" 
	                                              chart-type="column" 
	                                              function-y="AVG" 
	                                              color="#1b6698"
	                                              label-y="Nombre de naissances">
	                             </ods-chart-serie>
	                         </ods-chart-query>
	                         <ods-chart-query context="decesparcommunedepartementetregionde2003a2013" 
	                                          field-x="annee" 
	                                          timescale="year">
	                             <ods-chart-serie expression-y="nombre_deces" 
	                                              chart-type="column" 
	                                              function-y="AVG" 
	                                              color="#ec643c"
	                                              label-y="Nombre de décès">
	                             </ods-chart-serie>
	                         </ods-chart-query>
	                     </ods-chart>
	                 </ods-dataset-context>
	             </div>
	         </div>
	         <div class="col-md-6 col-sm-12">
	             <div class="ods-box">
	                 <h3>Composition <a href="/explore/dataset/evolution-et-structure-de-la-population-france-csp-2012"><i class="icon-external-link-sign"></i></a></h3>            
	                 <ods-dataset-context context="evolutionetstructuredelapopulationfrance2012categoriessocioprofessionn" 
	                                      evolutionetstructuredelapopulationfrance2012categoriessocioprofessionn-dataset="evolution-et-structure-de-la-population-france-csp-2012" 
	                                      evolutionetstructuredelapopulationfrance2012categoriessocioprofessionn-parameters="{'refine.sexe':'Total','refine.tranche_dage':'15+','q':'NOT csp:total'}">
	                     <ods-chart>
	                         <ods-chart-query context="evolutionetstructuredelapopulationfrance2012categoriessocioprofessionn" 
	                                          field-x="csp">
	                             <ods-chart-serie expression-y="value" 
	                                              chart-type="pie" 
	                                              function-y="AVG" 
	                                              color="range-custom">
	                             </ods-chart-serie>
	                         </ods-chart-query>
	                     </ods-chart>
	                 </ods-dataset-context>
	             </div>
	         </div>
	     </div>
	     <div class="ods-box">
	         <h3>Evolution des Catégories Socio-Professionelles <a href="/explore/dataset/pop-active-25-54-csp-activite-1968-2011"><i class="icon-external-link-sign"></i></a></h3>            
	         <ods-dataset-context context="populationactive2554ansparcategoriesocioprofessionnelleetactivite1960" 
	                              populationactive2554ansparcategoriesocioprofessionnelleetactivite1960-dataset="pop-active-25-54-csp-activite-1968-2011" 
	                              populationactive2554ansparcategoriesocioprofessionnelleetactivite1960-parameters="{}">
	             <ods-chart>
	                 <ods-chart-query context="populationactive2554ansparcategoriesocioprofessionnelleetactivite1960" 
	                                  field-x="annee" 
	                                  series-breakdown="csp_activite"
	                                  maxpoints="200">
	                     <ods-chart-serie expression-y="value" 
	                                      chart-type="spline" 
	                                      function-y="AVG" 
	                                      color="range-custom"
	                                      label-y="Population">
	                     </ods-chart-serie>
	                 </ods-chart-query>
	             </ods-chart>
	         </ods-dataset-context>
	     </div>
	     <div class="row">
	         <div class="col-md-6 col-sm-12">
	             <div class="ods-box">
	                 <h3>Répartition par type de Bac <a href="/explore/dataset/fr-esr-sise-effectifs-d-etudiants-inscrits-esr-public"><i class="icon-external-link-sign"></i></a></h3>
	                 <ods-dataset-context context="effectifsdetudiantsinscritsdanslesetablissementspublicssoustutelledumi" 
	                                      effectifsdetudiantsinscritsdanslesetablissementspublicssoustutelledumi-dataset="fr-esr-sise-effectifs-d-etudiants-inscrits-esr-public" 
	                                      effectifsdetudiantsinscritsdanslesetablissementspublicssoustutelledumi-parameters="{'sort':'-rentree'}">
	                     <ods-chart>
	                         <ods-chart-query context="effectifsdetudiantsinscritsdanslesetablissementspublicssoustutelledumi" field-x="bac_lib">
	                             <ods-chart-serie expression-y="effectif" 
	                                              chart-type="column" 
	                                              function-y="SUM" 
	                                              color="#2f7ed8"
	                                              label-y="Nombre d'inscrits">
	                             </ods-chart-serie>
	                             <ods-chart-serie expression-y="nouv_bachelier" 
	                                              chart-type="column" 
	                                              function-y="SUM" 
	                                              color="#0d233a"
	                                              label-y="Nombre de nouveaux bachelier">
	                             </ods-chart-serie>
	                         </ods-chart-query>
	                     </ods-chart>
	                 </ods-dataset-context>
	             </div>
	         </div>
	         <div class="col-md-6 col-sm-12">
	             <div class="ods-box">
	                 <h3>Répartition par cursus universitaire <a href="/explore/dataset/fr-esr-sise-effectifs-d-etudiants-inscrits-esr-public/"><i class="icon-external-link-sign"></i></a></h3>
	                 <ods-dataset-context 
	                                      context="effectifsdetudiantsinscritsdanslesetablissementspublicssoustutelledumi" 
	                                      effectifsdetudiantsinscritsdanslesetablissementspublicssoustutelledumi-dataset="fr-esr-sise-effectifs-d-etudiants-inscrits-esr-public" 
	                                      effectifsdetudiantsinscritsdanslesetablissementspublicssoustutelledumi-parameters="{'sort':'-rentree'}">
	                     <ods-chart>
	                         <ods-chart-query context="effectifsdetudiantsinscritsdanslesetablissementspublicssoustutelledumi" 
	                                          field-x="cursus_lmd_lib" 
	                                          series-breakdown="discipline_lib"
	                                          label-y="Nombre d'inscrits">
	                             <ods-chart-serie 
	                                              expression-y="effectif" 
	                                              chart-type="column" 
	                                              function-y="AVG"
	                                              color="range-custom"
	                                              label-y="Nombre d'inscrits">
	                             </ods-chart-serie>
	                         </ods-chart-query>
	                     </ods-chart>
	                 </ods-dataset-context>
	             </div>
	         </div>
	     </div>
	     <div class="ods-box">
	         <h3>Répartition par métier <a href="/explore/dataset/repartition-des-emplois-sur-le-territoire-france-1982-1990-1999-2007-2012"><i class="icon-external-link-sign"></i></a></h3>
	         <ods-dataset-context context="repartitiondesemploissurleterritoirefrance19821990199920072012" 
	                              repartitiondesemploissurleterritoirefrance19821990199920072012-dataset="repartition-des-emplois-sur-le-territoire-france-1982-1990-1999-2007-2012" 
	                              repartitiondesemploissurleterritoirefrance19821990199920072012-parameters="{}">
	             <ods-chart timescale="year">
	                 <ods-chart-query context="repartitiondesemploissurleterritoirefrance19821990199920072012" 
	                                  field-x="annee" 
	                                  timescale="year" 
	                                  stacked="percent" 
	                                  series-breakdown="metier">
	                     <ods-chart-serie expression-y="nombre" 
	                                      chart-type="column" 
	                                      function-y="AVG" 
	                                      color="range-custom"
	                                      label-y="Pourcentage">
	                     </ods-chart-serie>
	                 </ods-chart-query>
	             </ods-chart>
	         </ods-dataset-context>
	     </div>
	     <div class="ods-box">
	         <h3>Couverture 4G <a href="/explore/dataset/couverture-2g-3g-4g-en-france-par-operateur-juillet-2015"><i class="icon-external-link-sign"></i></a></h3>
	         <ods-dataset-context context="couverture2g3g4genfranceparoperateurjuillet2015" 
	                              couverture2g3g4genfranceparoperateurjuillet2015-dataset="couverture-2g-3g-4g-en-france-par-operateur-juillet-2015" 
	                              couverture2g3g4genfranceparoperateurjuillet2015-parameters="{'refine.reseau':'4G','refine.type_couverture':'Population'}">
	             <ods-chart>
	                 <ods-chart-query context="couverture2g3g4genfranceparoperateurjuillet2015" 
	                                  field-x="operateur" 
	                                  maxpoints="50">
	                     <ods-chart-serie expression-y="couverture" 
	                                      chart-type="column" 
	                                      function-y="AVG" 
	                                      color="#2c3f56"
	                                      label-y="Pourcentage de la population couverte">
	                     </ods-chart-serie>
	                 </ods-chart-query>
	             </ods-chart>
	         </ods-dataset-context>
	     </div>
	     <div class="row">
	         <div class="col-md-6 col-sm-12">
	             <div class="ods-box">
	                 <h3>Equipements de sports et loisirs <a href="/explore/dataset/equipement-sport-loisir-par-communes-2014-iris/?tab=table"><i class="icon-external-link-sign"></i></a></h3>
	                 <ods-dataset-context context="equipementsportloisirparcommunes2014iris" 
	                                      equipementsportloisirparcommunes2014iris-dataset="equipement-sport-loisir-par-communes-2014-iris" 
	                                      equipementsportloisirparcommunes2014iris-parameters="{}">
	                     <ods-map location="12,43.6156511237, 2.23787231587" scroll-wheel-zoom="false">
	                         <ods-map-layer context="equipementsportloisirparcommunes2014iris"
	                                        color="#d05356">
	                             <h3>
	                                 {{ record.fields.libelle_de_l_iris }}
	                             </h3>
	                             <ul class="equip-tooltip">
	                                 <li ng-repeat="f in context.dataset.fields">
	                                     <div ng-if= "f.name != 'geo_shape' && f.name != 'departement_commune' && f.name != 'empty' && f.name != 'code_commune' && f.name != 'departement' && f.name != 'depcom' && f.name != 'nom_dept' && f.name != 'nom_com' && f.name != 'geo_point_2d' && f.name != 'nom_region' && f.name != 'typ_iris' && f.name != 'nom_iris' && f.name != 'num_dept' && f.name != 'iris' && f.name != 'region2016' && f.name != 'region' && f.name != 'libelle_de_commune' && f.name != 'libelle_de_l_iris' && f.name != 'code_iris' && record.fields[f.name] != 0">
	                                         <strong>{{ f.label }}</strong> : {{ record.fields[f.name] }}
	                                     </div>
	                                 </li>
	                             </ul>
	                         </ods-map-layer>
	                     </ods-map>
	                 </ods-dataset-context>
	             </div>
	         </div>
	         <div class="col-md-6 col-sm-12">
	             <div class="ods-box">
	                 <h3>Fonctions médicales et paramédicales <a href="/explore/dataset/nombre-de-fonctions-medicales-et-paramedicales-2014-iris/?tab=table"><i class="icon-external-link-sign"></i></a></h3>
	                 <ods-dataset-context context="nombredefonctionsmedicalesetparamedicales2014iris" 
	                                      nombredefonctionsmedicalesetparamedicales2014iris-dataset="nombre-de-fonctions-medicales-et-paramedicales-2014-iris" 
	                                      nombredefonctionsmedicalesetparamedicales2014iris-parameters="{}">
	                     <ods-map location="12,43.6156511237, 2.23787231587" scroll-wheel-zoom="false">
	                         <ods-map-layer context="nombredefonctionsmedicalesetparamedicales2014iris"
	                                        color="#17a2a2">
	                             <h3>
	                                 {{ record.fields.libelle_de_l_iris }}
	                             </h3>
	                             <ul class="equip-tooltip">
	                                 <li ng-repeat="f in context.dataset.fields">
	                                     <div ng-if= "f.name != 'geo_shape' && f.name != 'departement_commune' && f.name != 'empty' && f.name != 'code_commune' && f.name != 'departement' && f.name != 'depcom' && f.name != 'nom_dept' && f.name != 'nom_com' && f.name != 'geo_point_2d' && f.name != 'nom_region' && f.name != 'typ_iris' && f.name != 'nom_iris' && f.name != 'num_dept' && f.name != 'iris' && f.name != 'region2016' && f.name != 'region' && f.name != 'libelle_de_commune' && f.name != 'libelle_de_l_iris' && f.name != 'code_iris' && record.fields[f.name] != 0">
	                                         <strong>{{ f.label }}</strong> : {{ record.fields[f.name] }}
	                                     </div>
	                                 </li>
	                             </ul>
	                         </ods-map-layer>
	                     </ods-map>
	                 </ods-dataset-context>
	             </div>
	         </div>
	     </div>
	     <div class="row">
	         <div class="col-md-6 col-sm-12">
	             <div class="ods-box">
	                 <h3>Activité Entreprises 2015 <a href="/explore/dataset/entreprises-immatriculees-en-2015/?tab=table&sort=date"><i class="icon-external-link-sign"></i></a></h3>
	                 <ods-dataset-context context="entreprisesimmatriculeesen2015,entreprisesradieesen2015" 
	                                      entreprisesimmatriculeesen2015-dataset="entreprises-immatriculees-en-2015" 
	                                      entreprisesimmatriculeesen2015-parameters="{'disjunctive.code_postal':true,'disjunctive.ville':true,'disjunctive.date':true}" 
	                                      entreprisesradieesen2015-dataset="entreprises-radiees-en-2015" 
	                                      entreprisesradieesen2015-parameters="{'disjunctive.libelle':true,'disjunctive.date':true}">
	                     <ods-chart single-y-axis="true">
	                         <ods-chart-query context="entreprisesimmatriculeesen2015" field-x="date" timescale="month">            
	                             <ods-chart-serie expression-y="personne_physique" 
	                                              chart-type="spline" 
	                                              function-y="COUNT" 
	                                              color="#4f8f55"
	                                              label-y="Créations">
	                             </ods-chart-serie>
	                         </ods-chart-query>
	                         <ods-chart-query context="entreprisesradieesen2015" 
	                                          field-x="date" 
	                                          timescale="month">
	                             <ods-chart-serie expression-y="siren" 
	                                              chart-type="spline" 
	                                              function-y="COUNT" 
	                                              color="#aa3c44"
	                                              label-y="Radiations">
	                             </ods-chart-serie>
	                         </ods-chart-query>
	                     </ods-chart>
	                 </ods-dataset-context>
	             </div>
	         </div>
	         <div class="col-md-6 col-sm-12">
	             <div class="ods-box">
	                 <ods-dataset-context context="offresdemploianonymisees"
	                                      offresdemploianonymisees-dataset="offres-demploi-anonymisees" 
	                                      offresdemploianonymisees-parameters="{'sort':'modification_date'}">
	                     <h3>Dernières offres d'emploi <a href="/explore/dataset/offres-demploi-anonymisees/?tab=table"><i class="icon-external-link-sign"></i></a></h3>
	                     <ods-result-enumerator context="offresdemploianonymisees"
	                                            max=8>
	                         <li>
	                             <h4><a ng-href="/explore/dataset/offres-demploi-anonymisees/?tab=table" target="_blank">{{item.fields.rome_profession_name}}</a></h4>
	                             <p>{{ item.fields.contract_type_name }} {{ item.fields.working_hours_type_name }} {{ item.fields.annual_minimum_salary | currency:"€/an (minimum)":0 }}</p>
	                         </li>
	                     </ods-result-enumerator>
	                 </ods-dataset-context>
	             </div>
	         </div>
	     </div>
	     <div class="row">
	         <div class="col-md-6 col-sm-12">
	             <div class="ods-box">
	                 <h3>Balance 2013 <a href="/explore/dataset/balance_communes/?tab=table"><i class="icon-external-link-sign"></i></a></h3>
	                 <ods-dataset-context context="balancecommunes" 
	                                      balancecommunes-dataset="balance_communes" 
	                                      balancecommunes-parameters="{}">
	                     <ods-table context="balancecommunes"
	                                displayed-fields="budget,sd,sc">
	                     </ods-table>
	                 </ods-dataset-context>
	             </div>
	         </div>
	         <div class="col-md-6 col-sm-12">
	             <div class="ods-box">
	                 <h3>Délinquance 2014 <a href="/explore/dataset/delinquance-2014-en-france/?tab=table&disjunctive.region&disjunctive.departement"><i class="icon-external-link-sign"></i></a></h3>
	                 <ods-dataset-context context="delinquance2014enfrance" 
	                                      delinquance2014enfrance-dataset="delinquance-2014-en-france" 
	                                      delinquance2014enfrance-parameters="{'disjunctive.region':'true','disjunctive.departement':'true'}">
	                     <ods-chart>
	                         <ods-chart-query context="delinquance2014enfrance"
	                                          field-x="categorie" 
	                                          maxpoints="10" 
	                                          sort="serie1-1">
	                             <ods-chart-serie expression-y="nombre_dactes" 
	                                              chart-type="column" 
	                                              function-y="AVG" 
	                                              color="#e8af55"
	                                              label-y="Nombre d'actes">
	                             </ods-chart-serie>
	                         </ods-chart-query>
	                     </ods-chart>
	                 </ods-dataset-context>
	             </div>
	         </div>
	     </div>
	     <div class="ods-box">
	         <h3>Prévisions météo <a href="/explore/dataset/arome-0025-sp1_sp2/?tab=table"><i class="icon-external-link-sign"></i></a></h3>
	         <ods-dataset-context context="arome0025sp1sp2" 
	                              arome0025sp1sp2-dataset="arome-0025-sp1_sp2" 
	                              arome0025sp1sp2-parameters="{}">
	             <ods-chart timescale="year">
	                 <ods-chart-query context="arome0025sp1sp2" field-x="forecast" timescale="hour">
	                     <ods-chart-serie expression-y="2_metre_temperature" 
	                                      chart-type="spline" 
	                                      function-y="AVG" 
	                                      color="#ec643c"
	                                      label-y="Température">
	                     </ods-chart-serie>
	                     <ods-chart-serie expression-y="relative_humidity" 
	                                      chart-type="spline" 
	                                      function-y="AVG" 
	                                      color="#17a2a2"
	                                      label-y="Humidité">
	                     </ods-chart-serie>
	                     <ods-chart-serie expression-y="total_water_precipitation" 
	                                      chart-type="spline" 
	                                      function-y="AVG" 
	                                      color="#2c3f56"
	                                      label-y="Précipitations">
	                     </ods-chart-serie>
	                 </ods-chart-query>
	             </ods-chart>
	         </ods-dataset-context>
	     </div>
	     <div class="row" id="dash_nav">
	         <a class="flat-btn" href="/page/apropos">A Propos</a>
	         <a class="flat-btn" href="/explore">Données</a>    
	     </div>
	 </div>
</div>
```

CSS code:

```css
/* General */

body {
    background: #fff url("http://public.opendatasoft.com/explore/dataset/villes-ods-background-images/files/d0e0b6b162a4f16fb4f345694cadbf84/download/");
    background-repeat: no-repeat;
   	min-height: 100%;
 	background-size: cover;
  	background-attachment: fixed;
    background-position: center center;
    font-family: 'Helvetica', 'Arial', sans-serif;
}

a:hover {
    text-decoration: none;
}

.ods-box {
    border-radius: 0;
    text-align: center;
}

#dash_nav {
    text-align: center;
}

.flat-btn {
    text-decoration: none;
    text-transform: uppercase;
    border-radius: 0;
    border-style: solid;
    border-width: 2px;
    text-align: center;
    color: #fff;
    padding: 0.66em 1.33em;
    display: inline-block;
    margin-top: 30px;
}
.flat-btn:hover {
    color: #2c3f56;
    background-color: #fff;
    text-decoration: none;
}

li {
	list-style-type: none;
	margin-bottom: 0.33em;
}

li > h4 {
    padding: 0;
    margin-bottom: 0;
}

/* Header */

#cityhour {
    text-align: left;
    margin: 2em auto;
}

#cityhour > h1, #cityhour > ods-dataset-context > h2 {
    color: #fff;  
    margin-bottom: 0.1em;
    line-height: 10vw;
    font-size: 10vw;
}

#cityhour > h4 {
    text-align: left;
    color: #fff;
    font-size: 12px;
    margin-top: 3em;
}

/* Content */

.equip-tooltip {
    line-height: 1;
    padding-left: 0;
}

.datafact {
    text-align: center;
}

.datafact {
    height: 110px;
    width: 250px;
    margin: 2em auto;
    padding: 0.5em 0 0 0;
}

.datafact h2 {
    border: 0;
    font-size: 180%;
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
}
```