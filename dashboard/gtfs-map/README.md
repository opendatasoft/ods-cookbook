# GTFS lines and stops visualisation!

### Live result

[Please find the live exemple on Discovery](https://discovery.opendatasoft.com/explore/dataset/gtfs-ny-english/)

### Process

##### Ask the activation of the GTFS extractors to the ODS support team

##### Upload the routes' shapes

1. Go to '+ New dataset'. 
2. Select a GTFS zip file as the source and choose the 'GTFS Routes' extractor.
3. Add as many GTFS sources as you want, each time checking the 'Extract filename' box.
4. Go to the 'Map tab' and configure the tooltip to your liking.

##### Upload the stops' shapes

1. Go to '+ New dataset'. 
2. Select a GTFS zip file as the source and choose the 'GTFS Stops' extractor.
3. Add as many GTFS sources as you want, each time checking the 'Extract filename' box.
4. Go to the 'Map tab' and configure the tooltip to your liking.

##### Upload the list of GTFS available for download

Follow the usual step of 'CSV and attached media' to display the list of the GTFS files with their metadata.

##### Go to the custom tab and write the dashboard code

### Code

(The CSS code is written so that the map takes exactly the remaining height of the screen in the default theme configuration)

```html
<ods-dataset-context context="lines,stops" lines-dataset="gtfs_ny_routes" stops-dataset="gtfs_ny_stops">

    <div class="row">
        <div class="col-md-8 dashboard">

            <ods-map no-refit="true" display-control="false" search-box="false" toolbar-fullscreen="true" toolbar-geolocation="true" basemap="jawg.streets" location="10,40.70795,-73.97688" scroll-wheel-zoom="false">
                <ods-map-layer-group>
                    <ods-map-layer context="stops" color="#6A79B0" picto="ods-bus" show-marker="true" display="auto" shape-opacity="0.5" point-opacity="1" border-color="#FFFFFF" border-opacity="1" border-size="1" border-pattern="solid" caption="false" title="Stations du réseau urbain" size="2" size-min="3" size-max="5" size-function="linear" show-if="stations"></ods-map-layer>
                </ods-map-layer-group>
                <ods-map-layer-group>
                    <ods-map-layer context="lines" color-by-field="route_color" picto="ods-circle" show-marker="true" display="categories" shape-opacity="0.5" point-opacity="1" border-color="#FFFFFF" border-opacity="1" border-size="1" border-pattern="solid" caption="false" title="Lignes du réseau urbain" size="1"></ods-map-layer>
                </ods-map-layer-group>
            </ods-map>
        </div>
        <div class="col-md-4 dashboard filters">

            <div class="row">
                <div class="col-xs-3">


                    <label class="switch">
                        <input type="checkbox" ng-click="stations=!stations">
                        <span class="slider round"></span>
                    </label>
                </div>
                <div class="col-xs-9">
                    <h2>
                        Afficher les stations</h2>
                </div>
            </div>
            <ods-facets context="lines">
                <h2>
                    Opérateur
                </h2>
                <ods-facet name="filename" refine-also="stops" disjunctive="true"></ods-facet>
                <hr />
                <p><i>
                    (filtres des lignes seulement)
                    </i></p>
                <h2 id="filterline" disjunctive="true">
                    Type de ligne
                </h2>
                <ods-facet name="route_type" disjunctive="true"></ods-facet>
                <h2>
                    Numéro de ligne
                </h2>
                <ods-facet name="route_short_name" disjunctive="true"></ods-facet>
                <h2>
                    Nom de ligne
                </h2>
                <ods-facet name="route_long_name" disjunctive="true"></ods-facet>

            </ods-facets>
        </div>
    </div>
</ods-dataset-context>
```

```css
.dashboard p {
    text-align: right;
    margin-bottom: 0;
}

#filterline {
    margin-top: 0;
}

.dashboard {
    height: calc(100vh - 210px);
}

.filters {
    overflow-y: scroll;
}

.odswidget-map, .odswidget-map__map {
    height: 100%;
}

.odswidget-map-display-control__groups {
    min-height: 0px;
}

/* The switch - the box around the slider */
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

/* Hide default HTML checkbox */
.switch input {display:none;}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
```
