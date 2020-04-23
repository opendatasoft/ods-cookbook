This the COVID-19 Dashboard as presented on the [Opendatasoft apps site](https://apps.opendatasoft.com/en/regional-covid).


## How to use ?
You need a datased with a date field and then subsequent fields on number of cases, new cases etc. published on the platform. The file presented here is configured so that the dataset contains the totals for each day. It does not compute the total from daily increments.

From here :
* Copy the code in your page content (respectively the .html et .css in HTML/CSS). If you want to host your own page, start with the [minimal setup](https://help.opendatasoft.com/widgets/#/tutorial/00setup).
* Change the dataset context. You likely won't need the domain either if you are publishing on your own domain.
* Put as many cards, maps and table columns as you want. It won't autodetect the fields from your dataset, you have to manually pick them and copy code the corresponding component. The columns of the tables, the cards and maps don't have to reflects the same figures.
* You may not need the ZIP code trick, in which case you can use a [simple color gradient widget](https://help.opendatasoft.com/widgets/#/api/ods-widgets.directive:odsColorGradient) for the colors.

Once configured, you just have to upload your dataset whenever it's available, the data will update.

## Data scheme used in the example from Junta de Castilla y León
The main data set used in the example can be found [here](https://analisis.datosabiertos.jcyl.es/explore/dataset/situacion-epidemiologica-coronavirus-en-castilla-y-leon/api/?disjunctive.provincia&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJzcGxpbmUiLCJmdW5jIjoiU1VNIiwieUF4aXMiOiJjYXNvc19jb25maXJtYWRvcyIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiM2NmMyYTUifSx7ImFsaWduTW9udGgiOnRydWUsInR5cGUiOiJzcGxpbmUiLCJmdW5jIjoiU1VNIiwieUF4aXMiOiJmYWxsZWNpbWllbnRvcyIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiNmYzhkNjIifV0sInhBeGlzIjoiZmVjaGEiLCJtYXhwb2ludHMiOiIiLCJ0aW1lc2NhbGUiOiJkYXkiLCJzb3J0IjoiIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJzaXR1YWNpb24tZXBpZGVtaW9sb2dpY2EtY29yb25hdmlydXMtZW4tY2FzdGlsbGEteS1sZW9uIiwib3B0aW9ucyI6eyJkaXNqdW5jdGl2ZS5wcm92aW5jaWEiOnRydWV9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIiLCJzaW5nbGVBeGlzIjp0cnVlfQ%3D%3D&location=8,41.64954,-4.33333&basemap=jawg.streets)

The scheme of data used is as follow :
```
    "provincia":"Burgos",
    "altas":0,
    "fallecimientos":4,
    "fecha":"2020-03-15",
    "nuevos_positivos":8,
    "codigo_ine":9059,
    "casos_confirmados":119,
    "posicion":[
        42.383333,
        -3.666667
    ]
```
The *fecha* (date) field is critical: for each date, all the data are present, including the cumulative sum.
Field *altas*, *falleciementos*, *nuevos_positivos* and *casos_confirmados* are your main stats about COVID. They can be anything : total cases at a given date, number of free hospital beds, number of new cases etc.

The second dataset used here is the *region* dataset, which contains map tiles of the region of Spain. It is used to draw the geographic regions as their contours are not included in the main dataset. The two sets are joined by the ZIP code. You have to change it to the corresponding set of your region (available on https://public.opendatasoft.com). See the [map join live tutorial for more details](https://discovery.opendatasoft.com/pages/techtrick-mpajoinlive/).
