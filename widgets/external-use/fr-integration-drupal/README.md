# Intégrer une page ODS sur un site DRUPAL

_Principale ressource technique en ligne: https://github.com/opendatasoft/ods-cookbook/tree/master/widgets/external-use ._

## Etapes pour une intégration sur un Drupal vierge de modules (test effectué sur un Drupal en local version 8.8.3 sans aucun module ajouté).

### Etape 1: Création d’une nouvelle page de contenu (contenu basique).

### Etape 2: Passage en format HTML Complet et en mode Source (bouton Source dans l’éditeur).

### Etape 3: Copié-Collé du code d’intégration:

Nous expliquerons en-dessous du code ce que fait chaque partie. Il n’est pas nécessaire de comprendre toutes les parties, vous pouvez seulement faire confiance au code et remplacer la partie: <!-- YOUR ODS CODE HERE !!! -->

Le template de code d'intégration se trouve également [ici, de manière à faciliter la copié-collé](https://github.com/opendatasoft/ods-cookbook/blob/master/widgets/external-use/fr-integration-drupal/template_code.html).

```html
<!DOCTYPE html>
<html>

    <head>
        <base href="/">

        <title>ODS Widgets Sandbox</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://static.opendatasoft.com/ods-widgets/latest/ods-widgets.css">
    </head>

    <body>

        <div ng-cloak ng-app="ods-widgets">

            <!-- YOUR ODS CODE HERE !!! -->

        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/angular.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/angular-sanitize.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/i18n/angular-locale_fr-fr.js"></script>
        <script type="text/javascript" src="https://static.opendatasoft.com/ods-widgets/latest/ods-widgets.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.17.1/locale/fr.js"></script>

        <!-- ODS Translation dict. -->
        <script type="text/javascript">
            var ods = angular.module('ods-widgets');
            ods.run(function(gettextCatalog) {
                gettextCatalog.setStrings('fr', {
                    'Clear all': 'Tout effacer',
                    'More': 'Voir plus',
                    'Less': 'Voir moins',
                    'Download image': 'Télécharger l\'image'
                });
                gettextCatalog.setCurrentLanguage('fr');
            });
        </script>

        <!-- urlsync patch -->
        <script type="text/javascript">
            angular.module('ods-widgets').config(function($locationProvider) {
                $locationProvider.html5Mode(true);
            });
        </script>

        <!-- custom basemap -->
        <script type="text/javascript">
            angular.module('ods-widgets').config(function(ODSWidgetsConfigProvider) {
                ODSWidgetsConfigProvider.setConfig({
                    "basemaps": [
                       {
                            "label": "Jawg Streets",
                            "provider": "jawg.streets",
                            "jawg_apikey": "xR04uwhHrvdCDoa7fOcwtnzQJ692NTKx1ae0n0QratDbuNgUuzo089KTzubJJ9mc"
                        },
                        {
                            "label": "Jawg Light",
                            "provider": "jawg.light",
                            "jawg_apikey": "xR04uwhHrvdCDoa7fOcwtnzQJ692NTKx1ae0n0QratDbuNgUuzo089KTzubJJ9mc"
                        },
 		{
                            "label": "Stamen",
                            "provider": "stamen.toner"
                        },
                        {
                            "url": "https://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png",
                            "strictTMS": false,
                            "provider": "custom",
                            "label": "Thunderforest",
                            "id": "land"
                        }
                    ]
                });
            });
        </script>

    </body>

</html>
```

Explications des différentes parties du code d’intégration:
* Balises link pour intégrer les librairies CSS. 

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://static.opendatasoft.com/ods-widgets/latest/ods-widgets.css">

  Les portails ODS embarquent de nombreuses classes et styles associés. Les balises ```<link>``` permettront d’importer toutes les librairies nécessaires à un affichage équivalent aux portails ODS. L’ordre doit être respecté, à savoir:
    * Bootstrap
    * Font Awesome
    * ods-widgets

* Balises scripts pour intégrer les librairies JS.

        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/angular.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/angular-sanitize.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/i18n/angular-locale_fr-fr.js"></script>
        <script type="text/javascript" src="https://static.opendatasoft.com/ods-widgets/latest/ods-widgets.js"></script></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.17.1/locale/fr.js"></script> 

  Les portails ODS fonctionnent grâce à des méthodes et fonctions de différentes librairies JS. Les balises ```<script>``` permettent d’importer les librairies nécessaires aux interactions des portails ODS. L’ordre doit être respecté, à savoir:
    * JQuery (version 2.1.4)
    * AngularJS (version 1.4.7)
    * AngularJS Sanitize (version 1.4.7) pour valider le HTML.
    * AngularJS Locale (version 1.4.7) pour gérer correctement les chiffres et dates en français (il faut charger une autre librairie si gestion dans d’autres langues: https://code.angularjs.org/1.4.7/i18n/).
    * ods-widgets
    * Moment Locale (version 2.17.1) également pour gérer correctement les dates en français.   

* Balise avec ng-cloak pour gérer le chargement de la page: 

        <div ng-cloak ng-app="ods-widgets">
                
        </div>

  Le fait de mettre tout le code de la page à l’intérieur de cette balise permet de ne pas brièvement afficher la page sous sa forme non compilée.
  
* Copié collé du code HTML de votre page ODS à intégrer.

        <!-- YOUR ODS CODE HERE !!! -->
         
* Balise en tout début de page et script à rajouter avec les autres scripts pour gérer les paramètres urlsync.

        <base href="/">

  Puis

        <!-- urlsync patch -->
        <script type="text/javascript">
              angular.module('ods-widgets').config(function($locationProvider) {
                  $locationProvider.html5Mode(true);
               });
        </script>

* Script en bas de page pour gérer la traduction de certains labels affichés dans les widgets.

        <!-- ODS Translation dict. -->
        <script type="text/javascript">
                var ods = angular.module('ods-widgets');
                ods.run(function(gettextCatalog) {
                     gettextCatalog.setStrings('fr', {
                            'Clear all': 'Tout effacer',
                            'More': 'Voir plus',
                            'Less': 'Voir moins',
                            'Download image': 'Télécharger l\'image'
                    });
                    gettextCatalog.setCurrentLanguage('fr');
                });
        </script>

* Script en bas de page pour ajouter des fonds de carte customisés (et qui seront donc disponibles dans les widgets ods-map). Le plus simple est la configuration Jawg, puisque la configuration est faite côté Jawg, avec une clé api.

        <!-- custom basemap -->
                <script type="text/javascript">
                    angular.module('ods-widgets').config(function(ODSWidgetsConfigProvider) {
                        ODSWidgetsConfigProvider.setConfig({
                            "basemaps": [
                               {
                                    "label": "Jawg Streets",
                                    "provider": "jawg.streets",
                                    "jawg_apikey": "xR04uwhHrvdCDoa7fOcwtnzQJ692NTKx1ae0n0QratDbuNgUuzo089KTzubJJ9mc"
                                },
                                {
                                    "label": "Jawg Light",
                                    "provider": "jawg.light",
                                    "jawg_apikey": "xR04uwhHrvdCDoa7fOcwtnzQJ692NTKx1ae0n0QratDbuNgUuzo089KTzubJJ9mc"
                                },
         		{
                                    "label": "Stamen",
                                    "provider": "stamen.toner"
                                },
                                {
                                    "url": "https://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png",
                                    "strictTMS": false,
                                    "provider": "custom",
                                    "label": "Thunderforest",
                                    "id": "land"
                                }
                            ]
                        });
                    });
                </script>

### Etape 4: Ajout du CSS de votre page (si vous avez un CSS personnalisée pour votre page).

En début de page, après les balises de style (link), ajoutez une balise <style> ouvrante et une balise </style> fermante. Entre ces deux balises, copiez-collez votre code CSS.

### Etape 5: Ajout du CSS de votre portail (si vous avez un CSS de portail personnalisée).

Si vous avez du CSS défini dans votre feuille de style du portail (https://votreportail.opendatasoft.com/backoffice/customization/theme/#stylesheet), vous pouvez également le copier coller dans une balise de style, exactement de la même manière que pour l’étape 4.

### Etape 6: Vérification des permissions d’accès aux données de la page.

Il se peut que la page affiche des données d’un jeu de données en accès restreint. Dans ce cas, si vous souhaitez que tout le monde sur votre site voit l’intégralité de la page, vous devez inclure un paramètre d’apikey dans le ods-dataset-context. Vous trouverez les syntaxes de ce widget et du paramètre dans la documentation technique: https://help.opendatasoft.com/widgets/#/api/ods-widgets.directive:odsDatasetContext .

En suivant toutes ces étapes à partir d’une version Drupal vierge, votre page devrait être la même que celle que vous aviez sur votre portail ODS!

## Bonnes pratiques pour faciliter les intégrations récurrentes.

* Faire en sorte que les classes des éléments de la page d’ODS aient des noms spécifiques, toutes préfixées par exemple par “ods-”, de manière à ce qu’aucune règle CSS ne soit en conflit avec des règles déjà définies dans votre Drupal.

* Au lieu d’appeler les librairies js de JQuery, Angular et ODS, et les feuilles de style CSS de Bootstrap, Font Awesome of ODS (https://help.opendatasoft.com/widgets/#/tutorial/00setup) directement dans l’écriture du code de la page, vous pouvez charger ces librairies dans le header de votre site institutionnel. Le responsable de site institutionnel pourra charger ces librairies dans le header, et vous n’aurez ainsi pas à recopier tous les appels aux librairies dans chacune de vos pages ou articles qui viennent d’un portail ODS.

* Il est préférable de télécharger les librairies ods-widgets (css et js) pour les charger en local: https://github.com/opendatasoft/ods-widgets/releases/tag/1.4.3 . En effet, le lien distant n’est plus mis à jour et vous manquez donc les fonctionnalités récentes. A terme, nous proposerons des liens de distributions de nos librairies, mais, pour l’heure, nous conseillons de télécharger des versions locales.

* Au lieu d’écrire directement le style CSS dans la partie html en utilisant les balises <style> et </style>, vous pouvez créer une feuille de style CSS spéciale ODS qui viendraient donc reprendre les styles utilisées dans tous les contenus d’Opendatasoft copiés sur le site institutionnel. Comment écrit précédemment, mieux vaut que ces classes soient préfixées de “ods-”. Cela ne concernent cependant pas les classes génériques de type container, container-fluid, row, etc.

## Conflits d’intégration connus avec un Drupal non vierge (eg des modules ont été ajoutés).

* Conflit de versions de librairies chargées pour ODS: il se peut que votre Drupal charge déjà des librairies comme JQuery ou AngularJS et que vos versions utilisées soient plus anciennes ou plus récentes que celles d’ODS. Ces différentes peuvent entraîner des conflits et il faut donc être vigilant à l’ordre dans lequel vous chargez les librairies. 

  Exemple: dans un cas précis de client, la librairie JQuery du Drupal était plus récente que la version d’ODS (2.1.4). Ainsi, le fait de charger la librairie JQuery dans la page elle-même remplaçait la plus récente, et le “sticky sidebar” ne fonctionnait plus, car absent de la version 2.1.4. Pour éviter cela, il a fallu enlever la ligne qui charge JQuery dans la page (<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>) et ajouter un paramètre defer dans toutes les autres lignes de chargement de script, comme suit:
  
        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/angular.min.js" defer></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/angular-sanitize.min.js" defer></script>
        <script type="text/javascript" src="https://opendatasoft.github.io/ods-widgets/dist/ods-widgets.js" defer></script>


* Problème de chargement CSS: certaines classes génériques qui étaient modifiées sur le site ODS ne sont pas modifiables sur Drupal. Par exemple, modifier body ne semble rien changer dans les pages Drupal. dans ce cas, il faut adapter à la marge le CSS, par exemple en remplaçant body par .content, car c’est ce qui est utilisé pour une page Drupal. Le CSS de la page ODS peut donc nécessiter une modification à la marge. 

* Problème de gestion des ressources: Il se peut que vous fassiez appel avec des URLs relatives à des ressources dans votre page, soit dans la partie HTML, soit dans la partie CSS. Dans ce cas, il faudra soit faire appel à l’URL complète de la ressource de votre portail, soit faire un appel à un service délivrant la ressource directement.

  Exemple: Vous chargez dans votre page ODS des polices grâce au code CSS suivant:
  
        @font-face {
            font-family: 'Eczar';
            src: url('/assets/theme_font/Eczar-Regular.ttf') format('truetype');
            font-style: normal;
            font-weight: 300;
            }
            
  L’URL est relative et vous n’allez rien récupérer en faisant ‘/assets’. Dans ce cas, vous pouvez soit entrer l’URL complète soit récupérer directement les fonts à partir de l’API google font:

        @import url('https://fonts.googleapis.com/css?family=Eczar:400,500,600,700,800&display=swap');

* Problème de gestion des liens: Votre site drupal peut changer la manière d’écrire les liens relatifs. Ainsi, il faut être vigilant à vos redirections dans votre page HTML.

  Exemple: dans votre page, vous faites des redirections via des liens vers d’autres pages de votre portail ODS, comme dans le code ci-dessous:
        
        <a href=”/pages/fichedetaillee”>Accédez à la fiche détaillée</a>
        
  Tout d’abord il faut avoir créer la fiche Drupal avec une bonne url /pages/fichedetaillee. Ensuite, il faut vérifier que votre drupal ne préfixe pas l’URL. Dans des tests en local, toutes les pages seront préfixées par /drupaldir. Dans ce cas, il faudra réécrire les urls pour inclure ce préfixe, comme suit:

        <a href=”/drupaldir/pages/fichedetaillee”>Accédez à la fiche détaillée</a>

* Autres problèmes d’intégration: contactez votre CSM si vous ne parvenez toujours pas à intégrer vos pages, et soyez le plus précis possible (logs d’erreurs, codes de votre page, modules de votre Drupal, etc.). Nous mettrons à jour ce document en fonction des problèmes d’intégration remontés.
