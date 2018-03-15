### Custom view 

#### Live result

[Please find the live exemple on Discovery](https://discovery.opendatasoft.com/explore/dataset/2015-registry-of-power-plant-connections-to-the-eletricity-transport-network/custom/)

#### Code

HTML code :

```html
<ods-tabs class="custom-tab">
    <ods-pane title="Number of power plants and maximum power" icon="pie-chart">

        <p>
            NB: The values below match the active filters
        </p>

        <div class="row">
            <div class="col-sm-6">
                <h3>
                    Total maximum power per sector (in MW)
                </h3>
                <ods-chart>
                    <ods-chart-query context="ctx" field-x="sector">
                        <ods-chart-serie expression-y="maximum_power_mw" 
                                         chart-type="treemap" 
                                         function-y="SUM" 
                                         color="range-Accent" 
                                         scientific-display="true">
                        </ods-chart-serie>
                    </ods-chart-query>
                </ods-chart>
            </div>
            <div class="col-sm-6">
                <h3>
                    Number of power plants per sector
                </h3>
                <ods-chart>
                    <ods-chart-query context="ctx" field-x="sector">
                        <ods-chart-serie expression-y="maximum_power_mw" chart-type="treemap" function-y="COUNT" color="range-Accent" scientific-display="true">
                        </ods-chart-serie>
                    </ods-chart-query>
                </ods-chart>
            </div>
        </div>
    </ods-pane>
    <ods-pane title="Geographic distribution" icon="map" pane-auto-unload="true">
        <p>
            NB: The values below match the active filters
        </p>

        <ods-map display-control="false" 
                 search-box="true" 
                 toolbar-fullscreen="true" 
                 toolbar-geolocation="true" 
                 basemap="jawg.streets" 
                 location="6,47.30903,2.0874"
                 style="height: 600px;">
            <ods-map-layer-group>
                <ods-map-layer context="ctx" 
                               color-numeric-ranges="{'42152923196196.8':'#e6755c','24286534228129.4':'#fc9272','60019312164264.2':'#d05946','77885701132331.6':'#ba3d30','95752090100399':'#a5211b'}" 
                               color-by-field="maximum_power_mw" 
                               picto="circle" 
                               show-marker="true" 
                               display="choropleth" 
                               border-color="#FFFFFF" 
                               caption="true">
                    <h3>
                        {{ record.fields.sector }}
                    </h3>
                    <p>
                        <i class="fa fa-industry fa-fw" aria-hidden="true"></i>
                        <strong>{{ record.fields.company }}</strong>
                        <br />
                        <i class="fa fa-battery-full fa-fw" aria-hidden="true"></i>
                        <strong>{{ record.fields.maximum_power_mw|number }} MW</strong> (maximum power)
                        <br />
                        <i class="fa fa-calendar fa-fw" aria-hidden="true"></i>
                        Entry into service on <strong>{{ record.fields.entry_into_service | moment: 'LL' }}</strong>
                    </p>
                </ods-map-layer>
            </ods-map-layer-group>
        </ods-map>
    </ods-pane>

    <ods-pane title="Wind power" icon="leaf">
        <div class="row">
            <div class="col-sm-6">
                <p>
                    For the specific case of wind power, we'll have a look at the connections made on both sides of the energy transportation network. 
                    That is connection made by the entity in charge of the high voltage network (the so-called network operator, which provided all data in this dataset) 
                    and connections made by the entity in charge of the medium and low voltage network (called distributor).
                    We can consider that connections made by the former are to companies which primary activity is power production whereas those made by the latter are to individuals and local companies (who happen to have a local energy production).
                </p>
                <p>
                    Using data from both entities, is it therefore possible to compare their activity and to see that wind power is mostly due to local companies and not nation-wide energy producers.
                </p>
            </div>
            <div class="col-sm-6" style="overflow: hidden;">
                <img src="/assets/theme_image/turbines_wind_farm.jpg" style="max-height: 400px;">
            </div>
        </div>
        <div class="row">
            <div class="col-sm-6">
                <h3>
                    Connections made to the high-voltage network
                </h3>    
                <ods-dataset-context context="registryofpowerplantconnectionstotheeletricitytransportnetwork"
                                     registryofpowerplantconnectionstotheeletricitytransportnetwork-dataset="2015-registry-of-power-plant-connections-to-the-eletricity-transport-network" 
                                     registryofpowerplantconnectionstotheeletricitytransportnetwork-parameters="{'disjunctive.sector':true,'refine.sector':'Eolien'}">
                    <ods-chart>
                        <ods-chart-query context="registryofpowerplantconnectionstotheeletricitytransportnetwork" field-x="region_name" sort="serie1-1">
                            <ods-chart-serie expression-y="maximum_power_mw" chart-type="column" function-y="SUM" color="#2C3F56" scientific-display="true">
                            </ods-chart-serie>
                        </ods-chart-query>
                    </ods-chart>
                </ods-dataset-context>
            </div>
        </div>

    </ods-pane>
</ods-tabs>
```

CSS code: 

```css
.custom-tab {
    margin-left: -21px;
    margin-right: -21px;
}
```
