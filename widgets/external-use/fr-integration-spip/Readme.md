# Intégrer une page ODS sur un site SPIP

_Principale ressource technique en ligne: https://github.com/opendatasoft/ods-cookbook/tree/master/widgets/external-use ._

## Etapes pour une intégration sur un Spip vierge de modules (test effectué sur un Spip en local version 3.2.11 sans aucun module ajouté).

### Etape 1: Création d’un squelette d'articles ODS.

Dans votre dossier de squelettes SPIP, créez un nouveau squelette d'articles que vous utiliserez pour les articles avec des widgets ODS. Ce squelette est une copie de votre squelette d'articles habituels.

### Etape 2: Modification de la balise head du squelette d'articles.

Nous expliquerons en-dessous du code ce que fait chaque partie, mais il n’est pas nécessaire de comprendre toutes les parties, vous pouvez simplement faire les copié-collés.

Un template de code de squelette (à partir du squelette par défaut de SPIP 3.2.11) se trouve également [ici, de manière à faciliter la copié-collé](https://github.com/opendatasoft/ods-cookbook/blob/master/widgets/external-use/fr-integration-spip/template_squelette.html).


Ajoutez au modifiez la balise ```<base>``` juste après l'ouverture de la balise ```<head>``` :

```html
<base href="#URL_SITE_SPIP/" />
```

Ajoutez toujours au sein de la balise ```<head>``` les balises ```<link>``` de style :

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="https://static.opendatasoft.com/ods-widgets/latest-v2/ods-widgets.css">
```
Enfin, ajoutez encore dans cette ballise ```<head>``` les balises ```<script>``` :

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.8.2/angular.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular-sanitize/1.8.2/angular-sanitize.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular-i18n/1.8.2/angular-locale_fr.min.js"></script>
<script type="text/javascript" src="https://static.opendatasoft.com/ods-widgets/latest-v2/ods-widgets.min.js"></script> 
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
                    "id": "jawg.streets",
                    "jawg_apikey": "xR04uwhHrvdCDoa7fOcwtnzQJ692NTKx1ae0n0QratDbuNgUuzo089KTzubJJ9mc"
                },
                {
                    "label": "Jawg Light",
                    "provider": "jawg.light",
                    "id": "jawg.light",
                    "jawg_apikey": "xR04uwhHrvdCDoa7fOcwtnzQJ692NTKx1ae0n0QratDbuNgUuzo089KTzubJJ9mc"
                },
                {
                    "label": "Stamen",
                    "provider": "stamen.toner",
                    "id":"stamen"
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
```

Spip intègre de base JQuery, mais si vous l'avez désactivé sur votre version, il faudrait bien charger en premier lieu le script Jquery :

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
```

Explications des différentes parties du code d’intégration:
* Balises link pour intégrer les librairies CSS. 

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://static.opendatasoft.com/ods-widgets/latest-v2/ods-widgets.css">

  Les portails ODS embarquent de nombreuses classes et styles associés. Les balises ```<link>``` permettront d’importer toutes les librairies nécessaires à un affichage équivalent aux portails ODS. L’ordre doit être respecté, à savoir:
    * Bootstrap
    * Font Awesome
    * ods-widgets

* Balises scripts pour intégrer les librairies JS.

        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.8.2/angular.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular-sanitize/1.8.2/angular-sanitize.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/angular-i18n/1.8.2/angular-locale_fr.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.17.1/locale/fr.js"></script>
        <script type="text/javascript" src="https://static.opendatasoft.com/ods-widgets/latest-v2/ods-widgets.min.js"></script> 

  Les portails ODS fonctionnent grâce à des méthodes et fonctions de différentes librairies JS. Les balises ```<script>``` permettent d’importer les librairies nécessaires aux interactions des portails ODS. L’ordre doit être respecté, à savoir:
    * AngularJS (version 1.8.2)
    * AngularJS Sanitize (version 1.8.2) pour valider le HTML.
    * AngularJS Locale (version 1.8.2) pour gérer correctement les chiffres et dates en français (il faut charger une autre librairie si gestion dans d’autres langues: https://code.angularjs.org/1.8.2/i18n/).
    * ods-widgets
    * Moment Locale (version 2.17.1) également pour gérer correctement les dates en français.   
  
* Script à rajouter avec les autres scripts pour gérer les paramètres urlsync.

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
                                    "id": "jawg.streets",
                                    "jawg_apikey": "xR04uwhHrvdCDoa7fOcwtnzQJ692NTKx1ae0n0QratDbuNgUuzo089KTzubJJ9mc"
                                },
                                {
                                    "label": "Jawg Light",
                                    "provider": "jawg.light",
                                    "id": "jawg.light",
                                    "jawg_apikey": "xR04uwhHrvdCDoa7fOcwtnzQJ692NTKx1ae0n0QratDbuNgUuzo089KTzubJJ9mc"
                                },
                                {
                                    "label": "Stamen",
                                    "provider": "stamen.toner",
                                    "id":"stamen"
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

### Etape 3: Création d'un article qui utilise le squelette des articles ODS.

Copiez-collez votre code HTML au sein des balises suivantes :
```html
<html>
    <body>
        <div ng-cloak ng-app="ods-widgets">
            <!-- YOUR ODS CODE HERE !!! -->
        </div>
    </body>
</html>
```

Autrement dit, vous remplacez <!-- YOUR ODS CODE HERE !!! --> par votre code HTML.

### Etape 4: Ajout du CSS de votre page au sein de votre article.

En fin de code de votre article, avant de fermer votre balise ```</body>```, ajoutez une balise ```<style>``` ouvrante et une balise ```</style>``` fermante. Entre ces deux balises, copiez-collez votre code CSS.

Si vous avez du CSS défini dans votre feuille de style du portail (https://votreportail.opendatasoft.com/backoffice/customization/theme/#stylesheet), vous pouvez également le copier coller dans une balise de style avant de refermer la balise </body>.

Un template de code de squelette (à partir du squelette par défaut de SPIP 3.2.11) se trouve également [ici, de manière à faciliter la copié-collé](https://github.com/opendatasoft/ods-cookbook/blob/master/widgets/external-use/fr-integration-spip/template_article.html).

### Etape 5: Vérification des permissions d’accès aux données de la page.

Il se peut que la page affiche des données d’un jeu de données en accès restreint. Dans ce cas, si vous souhaitez que tout le monde sur votre site voit l’intégralité de la page, vous devez inclure un paramètre d’apikey dans le ods-dataset-context. Vous trouverez les syntaxes de ce widget et du paramètre dans la documentation technique: https://help.opendatasoft.com/widgets/#/api/ods-widgets.directive:odsDatasetContext .

En suivant toutes ces étapes à partir d’une version SPIP vierge, votre page devrait être la même que celle que vous aviez sur votre portail ODS!

## Bonnes pratiques pour faciliter les intégrations récurrentes.

* Faire en sorte que les classes des éléments de la page d’ODS aient des noms spécifiques, toutes préfixées par exemple par “ods-”, de manière à ce qu’aucune règle CSS ne soit en conflit avec des règles déjà définies dans votre Drupal.

* Ne pas utiliser de class "container", qui fixe une largeur en dure. Préférez par exemple une classe de type container. Ou surchargez les classes de container avec le style suivant :

```css
/** Specific override **/
@media screen and (min-width: 1408px) {
    .ods-dataset-visualization .ods-tabs__pane .container:not(.is-max-desktop):not(.is-max-widescreen) {
        max-width: 100%;
    }
}
@media screen and (min-width: 1216px) {
    .ods-dataset-visualization .ods-tabs__pane .container:not(.is-max-desktop) {
        max-width: 100%;
    }
}
@media screen and (min-width: 1024px) {
    .ods-dataset-visualization .ods-tabs__pane .container {
        max-width: 100%;
    }
}
```

* Au lieu d’écrire directement le style CSS dans la partie html en utilisant les balises <style> et </style>, vous pouvez créer une feuille de style CSS spéciale ODS qui viendraient donc reprendre les styles utilisées dans tous les contenus d’Opendatasoft copiés sur le site institutionnel. Comment écrit précédemment, mieux vaut que ces classes soient préfixées de “ods-”. Cela ne concernent cependant pas les classes génériques de type container, container-fluid, row, etc. Cette feuille de style serait intégrée dans le squelette des articles ODS.

## Conflits d’intégration connus avec un SPIP non vierge (eg des modules ont été ajoutés).

* Conflit de versions de librairies chargées pour ODS: il se peut que votre SPIP charge déjà des librairies comme JQuery ou AngularJS et que vos versions utilisées soient plus anciennes ou plus récentes que celles d’ODS. Ces différentes peuvent entraîner des conflits et il faut donc être vigilant aux versions des librairies que vous chargez, ou à l’ordre dans lequel vous chargez les librairies. 

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
        
  Tout d’abord il faut avoir créer la fiche Drupal avec une bonne url /pages/fichedetaillee. Ensuite, il faut vérifier que votre spip ne préfixe pas l’URL. Dans des tests en local, toutes les pages seront préfixées par /drupaldir. Dans ce cas, il faudra réécrire les urls pour inclure ce préfixe, comme suit:

        <a href=”/spip/pages/fichedetaillee”>Accédez à la fiche détaillée</a>

* Autres problèmes d’intégration: contactez votre CSM si vous ne parvenez toujours pas à intégrer vos pages, et soyez le plus précis possible (logs d’erreurs, codes de votre page, modules de votre Drupal, etc.). Nous mettrons à jour ce document en fonction des problèmes d’intégration remontés.
