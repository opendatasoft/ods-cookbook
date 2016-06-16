### How to translate textual content in external pages

For the moment, textual translation is not available for external use of ODS Widgets.
In the mean time, you can specify your own dictionary to AngularJS translate tool.

Simply add this block of javascript at the end of your page (after angular and ods-widget import)

```html
    <script type="text/javascript">
          var ods = angular.module('ods-widgets');
          ods.run(function(gettextCatalog) {
              gettextCatalog.setStrings('fr', {
                'Clear all': 'Tout effacer',
                'More': 'Voir plus'
              });
              gettextCatalog.setCurrentLanguage('fr');
          });
    </script>	
```

#### Explanation

```javascript
    gettextCatalog.setStrings('fr', {
                'Clear all': 'Tout effacer',
                'More': 'Voir plus'
              });
```
sets the French dictionnary.


```javascript
    gettextCatalog.setCurrentLanguage('fr');
```
sets the current language of the page !
Feel free to develop your own language picker on top of it !