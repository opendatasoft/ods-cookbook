# Sorted chart breakdown on OpenDataSoft

The working example can be found [on Discovery](https://discovery.opendatasoft.com/pages/sorted-chart-breakdown/). It is based on [the AirBnB listings dataset](https://public.opendatasoft.com/explore/dataset/air-bnb-listings/table/).

What you need to reproduce this example is an understanding of the following three elements:
* Configuration of the ods-vega-lite-chart widget
* Configuration of the ods-analysis widget
* Specifications of the Vega-lite library

## Configuration of the ods-vega-lite-chart widget

An ods-vega-lite-chart widget takes two parameters:
* A vega-lite spec - or "spec=" below
* One or several arrays of values - or "values-name="" below

```html
<ods-vega-lite-chart spec='{
                                           "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
                                           "data": {"name": "listings"},
                                           VEGA-LITE SPEC CONTINUES HERE
                                           }'
                                     values-listings="breakdown.results">
</ods-vega-lite-chart>
```

Unfortunately, the code editor in OpenDataSoft won't indent properly the specification of the spec parameter, so you should probably write beforehand your vega-lite outside the OpenDataSoft platform.

## Configuration of the ods-analysis widget

This widget will result in an array of values, which is what is needed in the ods-vega-lite-chart parameters. The complete documentation can be found on [the help website](https://help.opendatasoft.com/widgets/#/api/ods-widgets.directive:odsAnalysis).

```html
<div ods-analysis="breakdown"
                 ods-analysis-context="airbnb"
                 ods-analysis-x-type="room_type"
                 ods-analysis-x-city="city"
                 ods-analysis-serie-listings="COUNT(*)">
```

## Specifications of the Vega-lite library

All the documentation of the vega-lite specifications can be found [on a dedicated website](https://vega.github.io/vega-lite/). Our goal here is not to replicate this documentation.

We can merely point to a few decisive values of the specification below:
* "data": {"name": "xxxxx"} -> the name value will correspond to xxxx in the vega-lite-chart parameter values-xxxx.
* change the names of the fields if needed: listings, x.city, x.room_type
* change the filter is you want something else than a top 10: "filter":"datum.rank<=10"
* change the color and legend if needed: "scale": {
                                           "domain": ["Entire home/apt", "Private room","Shared room"],
                                           "range": ["#FEC45A", "#563C7E","#03A658"]
                                           }

## HTML code of the example

```html
<div class="container-fluid">
    <div class="ods-box" >
        <ods-dataset-context context="airbnb"
                             airbnb-dataset="air-bnb-listings"
                             airbnb-domain="public">
            <ods-facets context="airbnb">
                <ods-facet name="column_19">
                </ods-facet>
            </ods-facets>

            <div ods-analysis="breakdown"
                 ods-analysis-context="airbnb"
                 ods-analysis-x-type="room_type"
                 ods-analysis-x-city="city"
                 ods-analysis-serie-listings="COUNT(*)">
                
                <ods-vega-lite-chart spec='{
                                           "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
                                           "data": {"name": "listings"},
                                           width: 700,
                                           height: 500,
                                           "transform": [
                                           {
                                           "window":
                                           [{
                                           "op":"sum",
                                           "field":"listings",
                                           "as":"sum_listings_city"}],
                                           "frame": [null, null],
                                           "groupby": [
                                           "x.city"
                                           ]
                                           },
                                           {
                                           "window":
                                           [{
                                           "op":"dense_rank",
                                           "as":"rank"}],
                                           "sort": [{"field":"sum_listings_city","order":"descending"}]
                                           },
                                           {
                                           "filter":"datum.rank<=10"
                                           }
                                           ],
                                           "mark": {"type":"bar","tooltip": {"content": "data"}},
                                           "encoding": {
                                           "x": {
                                           "field":"x.city",
                                           "type": "nominal",
                                           "sort": {"op": "mean", "field": "listings", "order":"descending"},
                                           "axis": {"title": "City"}
                                           },
                                           "y": {
                                           "field":"listings",
                                           "type": "quantitative"
                                           },
                                           "color": {
                                           "field": "x.room_type",
                                           "type": "nominal",
                                           "scale": {
                                           "domain": ["Entire home/apt", "Private room","Shared room"],
                                           "range": ["#FEC45A", "#563C7E","#03A658"]
                                           },
                                           "legend": {"title": "Room type"}
                                           },
                                           "tooltip": [
                                           {"field":"x.city", "type":"nominal", "name":"City"},
                                           {"field":"x.room_type", "type":"nominal"},
                                           {"field":"listings", "type":"quantitative"},
                                           {"field":"sum_listings_city", "type":"quantitative"}
                                           ]
                                           }
                                           }'
                                     values-listings="breakdown.results">
                </ods-vega-lite-chart>
            </div>

        </ods-dataset-context>
    </div>
</div>
```