### Discovery home page - How to list records in a nicer way, as list elements or cards !

 - [Demo here](https://discovery.opendatasoft.com/)
 

#### Resources list :

The key widget is the `ods-result-enumerator`, or the ability to iterate over records and display custom HTML blocs for each record.
Feel free to build any kind of vizualisation for each records.

In this exemple, you'll find resources cards, custom displayed dependings on specific values of fields etc...


```html
    <div class="row resources">
        <ods-dataset-context  context="discoveryresources" 
                             discoveryresources-dataset="discovery-resources" 
                             discoveryresources-parameters="{'sort':'sort', 'disjunctive.type':true}">            
            <h2>
                Resources
            </h2>

            <div class="resources-filters">
                <ods-text-search context="discoveryresources"></ods-text-search>
                <ods-facets context="discoveryresources">
                    <ods-facet name="type">
                        <div>{{category.name}}</div>
                    </ods-facet>
                </ods-facets>
            </div>

            <div class="resources-blocks">
                <ods-result-enumerator context="discoveryresources" max="16">
                    <div class="themeblock col-lg-4 col-sm-6 hover-group">
                        <a class="pledge__hover hover-zoomout"  href="{{ item.fields.lien }}">
                            <div class="pledge__hover-content">
                                <div class="themeblock__icon">
                                    <i class="fa" ng-class="'{{ item.fields.icone }}'"></i>
                                </div>
                                <h3>{{ item.fields.description_en }}</h3>
                                <span>
                                    {{ item.fields.description_2_en }}
                                </span>
                                <br/>
                                <span class="themeblock__type">
                                    {{ item.fields.type_en }}
                                </span>
                            </div>
                        </a>
                        <div class="themeblock__content themeblock__content--a">
                            <ods-picto ng-if="item.fields.new"
                                       url="'/assets/theme_image/new_flag_2.svg'"
                                       color="'#E23F32'"
                                       class="new-flag">
                            </ods-picto>
                            <ods-picto ng-if="!item.fields.visibilite"
                                       url="'/assets/theme_image/lock.svg'"
                                       color="'#1E0C33'"
                                       class="lock">
                            </ods-picto>
                            <div class="themeblock__icon">
                                <i class="fa" ng-class="'{{ item.fields.icone }}'"></i>
                            </div>
                            <h3>{{ item.fields.description_en }}</h3>
                            <span>
                                {{ item.fields.description_2_en }}
                            </span>
                                                            <br/>
                            <span class="themeblock__type">
                                {{ item.fields.type_en }}
                            </span>
                        </div>
                    </div>
                </ods-result-enumerator>
            </div>
        </ods-dataset-context>
    </div>
```


```css
/* RESOURCES FILTERS */
.resources {
    position: relative;
}
.resources-filters {
    display: inline-flex;
    position: absolute;
    right: 5px;
    top: 0;
}
.resources-blocks {
    margin-top: 15px;
}

.odswidget.odswidget-text-search {
    width: 120px;
    margin: 15px 20px 0px 0px;
}
.odswidget-text-search__search-box {
    font-size: 1rem;
    height: 30px;
}
.odswidget-facet__category-list {
    display: inline-flex;
}
.odswidget-facet__category {
    border: 2px solid #1e0c33;
    padding: 2px 6px 0px 6px;
    border-radius: 5px;   
    margin-right: 5px;
    font-size: 0.9em;
    font-weight: 600;
}

.themeblock {
    color:black;
    fill:black;
    text-align: center;
    padding: 10px;
}

.themeblock h3 {
    color: #1E0C33;
    text-transform: uppercase;
}
.themeblock__icon {
    font-size: 3rem;
    color: #1E0C33;
}
.themeblock__content {
    background-color: #eeeeee;
    padding: 20px;
    display: block;
    color: inherit;
    text-decoration: none;
}
.themeblock__type {
    border: 2px solid #1e0c33;
    padding: 2px 6px 0px 6px;
    border-radius: 5px;
    font-size: 0.9em;
    font-weight: 600;
}
.new-flag, .lock {
    position: absolute;
    right: 10px;
    top: 10px;
    width: 100px;
}
.lock {
    top: 30px;
    width: 60px;
}

@media (min-width: 768px) and (max-width: 991px)  {
    .themeblock__content {
        height: 250px;
    }
}
@media (min-width: 992px) and (max-width: 1199px)  {
    .themeblock__content {
        height: 230px;
    }
}
@media (min-width: 1200px) {
    .themeblock__content {
        height: 230px;
    }
}
.themeblock__content{
    background-color: #ddd;
}


.pledge__hover {
    /*background: rgba(43,222,115,0.6);*/
    background: rgba(30, 12, 51, 0.8);
}
.hover-group .hover-zoomout {
    -webkit-transform: scale(1.17);
    -moz-transform: scale(1.17);
    -ms-transform: scale(1.17);
    -o-transform: scale(1.17);
    transform: scale(1.17);
    -webkit-transition: all 0.2s ease-in-out;
    -moz-transition: all 0.2s ease-in-out;
    -ms-transition: all 0.2s ease-in-out;
    -o-transition: all 0.2s ease-in-out;
    transition: all 0.2s ease-in-out;
    opacity: 0;
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    margin: 10px;
}
.pledge__hover-content {
    font-size: 15px;
    color: white;
    display: inline-block;
    padding: 20px;
}
.pledge__hover-content h3 {
    color: white;
}
.pledge__hover-content .themeblock__icon {
    color: white;
}
.pledge__hover-content .themeblock__type {
    border-color: white;
}

.hover-group .hover-zoomout:hover {
    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -ms-transform: scale(1);
    -o-transform: scale(1);
    transform: scale(1);
    opacity: 1;    
}

```
