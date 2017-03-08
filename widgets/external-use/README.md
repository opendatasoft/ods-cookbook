### External use of ODS-Widget

In order to use ODS-Widget outside the platform a few elements needs to be added :
 
- AngularJS Locale module to deal with numbers display for exemple (French VS English, space VS comma to separate 1000x digits)
- Translations : ODS Platform embed traduction that are not available the platfrom, you'll need to define your own traduction
- Context urlsync parameter is not properly working without some additionnal javascript parameters.

Some other aspect needs your attentions :

- Library should be downloaded and hosted on your site, in order to block the corresponding AngularJS and ODSWidget version regarding your code.
- The ods-dataset-context must know on wich domain the dataset is hosted with the `context-domain` parameter. A private dataset should also required a `context-apikey` parameter to authenticate the API call.

An exemple for most of these topics is available on Plnkr here : [here] (http://embed.plnkr.co/x19rZSNCdf07MEJc2Bxq/)
 
Do not hesitate to fork it and use it as a template !
 
Prerequisite : the facet must be disjunctive (allow multiple criteria selection)

N.B. : Remove the ods-facet widget, it's here to illustrate that the refine works correctly


#### AngularJS Locale_FR

In javascript includes, the angular-locale script should be included.
It can be downloaded here :
https://code.angularjs.org/1.4.7/i18n/angular-locale_fr-fr.js

Or include directly the file :
```html
<script src="//cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/i18n/angular-locale_fr-fr.js"></script>
```

#### Translations :

Translation dictinary must be declared for each language through this bunch of code :

```html
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
```

Here, 4 keys are declared with the corresponding French translation.


#### Urlsync context parameter

First, some information about urlsync parameter [here] (http://opendatasoft.github.io/ods-widgets/docs/#/api/ods-widgets.directive:odsCatalogContext)

To make it work with an external use of ODSWidget, 2 elements needs to be added to the page, first in the header :
```html
  <base href="/">
```
then, at the end, with other scripts :
```html
<script type="text/javascript">
    angular.module('ods-widgets').config(function($locationProvider) {
      $locationProvider.html5Mode(true);
    });
</script>
```

#### Blocking JQuery, AngularJS and ODSWidget versions

To prevent from any changes or weird behavior from external libraries, the best practice is to block the working version of each library you use.
ODSWidget doesn't contains the version number, it means that for each new release, your code will be run on this new version if you point directly to the remote address.
It's highly advised to download and store the ODSWidget library locally on your website and include it in your page.


#### context-domain and context-apikey

Any context declaration on ODS Platform suppose that the corresponding dataset is hosted locally (on the domain where you display the page) and the user right are the current user displaying the page.
You can override these 2 behaviors by defining :
-   the domain where the dataset is hosted by adding the optional `context-domain`.
-   the user apikey to authenticate the API calls by adding the optional `context-apikey`.

More information [here] (http://opendatasoft.github.io/ods-widgets/docs/#/api/ods-widgets.directive:odsCatalogContext)

A context declaration should looks like this :

```html
<ods-dataset-context 
    context="ctx,ctx1" 
    ctx-dataset="formesjuridiquefinal" 
    ctx-domain="fpassaniti"
    ctx1-dataset="formesjuridiquefinal"
    ctx1-parameters="{'q':'societe'}"
    ctx1-domain="fpassaniti">
    
    ...
    
</ods-dataset-context>
```


### Final code :

```html
<!DOCTYPE html>
<html>

<head>
  <base href="/">

  <title>ODS Widgets Sandbox</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://opendatasoft.github.io/ods-widgets/dist/ods-widgets.css">
</head>

<body>

  <div ng-app="ods-widgets">

    <ods-dataset-context 
    context="ctx" 
    ctx-dataset="formesjuridiquefinal" 
    ctx-domain="fpassaniti">
      <h2>{{ ctx.dataset.metas.records_count | number }} formes juridiques</h2>
      
      <ods-text-search context="ctx" placeholder="société, caisse, asso"></ods-text-search>
      <ods-table context="ctx" sort="nom"></ods-table>
    </ods-dataset-context>

  </div>

  <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
  <script src="//cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/angular.js"></script>
  <script src="//cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/angular-sanitize.min.js"></script>
  <script src="//cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/i18n/angular-locale_fr-fr.js"></script>
  <script type="text/javascript" src="//opendatasoft.github.io/ods-widgets/dist/ods-widgets.js"></script>

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

  <script type="text/javascript">
    angular.module('ods-widgets').config(function($locationProvider) {
      $locationProvider.html5Mode(true);
    });
  </script>
</body>

</html>
```