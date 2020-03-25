This the COVID-19 Dashboard as presented on the [Opendatasof apps site](https://apps.opendatasoft.com/en/regional-covid).


## How to use ?
You need a datased with a date field and then subsequent fields on number of cases, new cases etc. published on the platform. The file presented here is configured so that the dataset contains the totals for each day. It does not compute the total from daily increments.

From here :
* Copy the code in your page content (respectively the .html et .css in HTML/CSS). If you want to host your own page, start with the [minimal setup](https://help.opendatasoft.com/widgets/#/tutorial/00setup).
* Change the dataset context. You likely won't need the domain either if you are publishing on your own domain.
* Put as many cards, maps and table columns as you want. It won't autodetect the fields from your dataset, you have to manually pick them and copy code the corresponding component. The columns of the tables, the cards and maps don't have to reflects the same figures.
* You may not need the ZIP code trick, in wich case you can use a [simple color gradient widget](https://help.opendatasoft.com/widgets/#/api/ods-widgets.directive:odsColorGradient) for the colors.

Once configured, you just have to upload your dataset whenever it's available, the data will update.
