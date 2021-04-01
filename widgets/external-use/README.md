### External use of ODS-Widget

In order to use ODS-Widget outside the platform a few elements need to be added :
 
- AngularJS locale module to deal with numbers display for example (French VS English, space VS comma to separate 1000x digits)
- Translations : ODS Widgets do not embed translations automatically, like it does on the platform, you'll need to define your own translation dictionary
- Context urlsync parameter is not properly working without some additional javascript parameters.

Some other aspects need your attention :

- Library should be downloaded and hosted on your site, in order to block the corresponding AngularJS and ODSWidget version regarding your code.
- The ods-dataset-context must know on wich domain the dataset is hosted with the `context-domain` parameter. A private dataset should also required a `context-apikey` parameter to authenticate the API call.
- Custom basemap needs to be defined in your HTML code as it can't get the configuration from your platform automatically. 
- ng-cloak to prevent displaying AngularJS before it has been fully loaded 

An example for most of these topics is available on Plnkr [here] (http://embed.plnkr.co/Ly6BNY/)
 
Do not hesitate to fork it and use it as a template or simply download the [virgin template] (./template.html) !
 

#### AngularJS locale :

The angular-locale library should be included in the script includes at the end of the html page.
All locales can be found here for AngularJS V 1.4.7 :
https://code.angularjs.org/1.4.7/i18n/

French version for example is : 
https://code.angularjs.org/1.4.7/i18n/angular-locale_fr-fr.js


Or include directly the file from Cloudflare CDN :
```html
<script src="//cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/i18n/angular-locale_fr-fr.js"></script>
```

Another module might need to be localized concerning date formating filter. 
Include directly this file :
```html
<script src="//cdnjs.cloudflare.com/ajax/libs/moment.js/2.17.1/locale/fr.js"></script>
```


#### Translations :

##### AngularJS :

Translation dictionary must be declared for each language through this bunch of code :

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

To make it work with an external use of ODSWidget, 2 elements need to be added to the page, first in the header :
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

To prevent from any changes or weird behaviors from external libraries, the best practice is to block the working version of each library you use.

The current URL of the ODS-Widgets library doesn't contain the version number, which means that for each new release, your code will be run on this new version if you point directly to the remote address, and your page could change without you knowing so if a widget changes

For this reason, it's highly advised to download and store the ODSWidget library locally on your website and include it in your page.


#### `context-domain` and `context-apikey`

Any context declaration on ODS Platform suppose that the corresponding dataset is hosted locally (on the domain where you display the page) and the user right are the current user displaying the page.
You can override these 2 behaviors by defining :
-   the domain where the dataset is hosted by adding the optional `context-domain`.
-   the user apikey to authenticate the API calls by adding the optional `context-apikey`.

More information [here] (http://opendatasoft.github.io/ods-widgets/docs/#/api/ods-widgets.directive:odsCatalogContext)

A context declaration should looks like this :

```html
<ods-dataset-context 
    context="ctx,ctx1" 
    
    ctx-dataset="us-hospitals" 
    ctx-domain="discovery"
    
    ctx1-dataset="formesjuridiquefinal"
    ctx1-parameters="{'q':'societe'}"
    ctx1-domain="fpassaniti"
    
    >
    
    ...
    
</ods-dataset-context>
```

#### Custom basemaps throught the `ODSWidgetsConfigProvider`

First, have a look to the [ODSWidgetsConfigProvider] (https://opendatasoft.github.io/ods-widgets/docs/#/api/ods-widgets.ODSWidgetsConfigProvider) documentation.
It explains how to set up custom basemap while using ODS Widgets library.

To add an OpenStreeMap custom basemap like [Thunderforest landscape] (http://www.thunderforest.com/maps/landscape/)
Get the tile URL : `https://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png`
And build the json configuration like :
```json
{
    "url": "https://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png",
    "strictTMS": false,
    "provider": "custom",
    "label": "Thunderforest",
    "id": "landscape"
}
```

For custom WMS basemap, build the json configuration like :
```json
{
    "url": "https://wms.umea.se/geoserver/gwc/service/wms",
    "provider": "custom_wms",
    "label": "LantmäterietsKarta",
    "id": "custom_basemap",
    "layers": "Projektkarta_V2",
    "styles": "",
    "minZoom": 1,
    "maxZoom": 20,
    "attribution": "Lantmäteri Umeå kommun"
}
```

Then, add it to your code :
```html
<script type="text/javascript">
angular.module('ods-widgets').config(function(ODSWidgetsConfigProvider) {
  ODSWidgetsConfigProvider.setConfig({
      "basemaps": [
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
```

#### `ng-cloak` the page loading

Everything is explained [here] (https://docs.angularjs.org/api/ng/directive/ngCloak) : This directive is used to prevent the AngularJS html template from being briefly displayed by the browser in its raw (uncompiled) form while your application is loading. Use this directive to avoid the undesirable flicker effect caused by the html template display.

To sum up, simply add `ng-cloak` directive on the HTML element that contains all your AngularJS/ODS Widget code.

```html
<body>

  <div ng-cloak ng-app="ods-widgets">

    <ods-dataset-context . . . 
```

### Final code :

[here](./template.html)
