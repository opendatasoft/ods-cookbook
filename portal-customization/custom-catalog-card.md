# Custom catalog card

[Live exemple here](https://discovery.opendatasoft.com/pages/catalog_card/)

## The default one

```html
<ods-catalog-card>
    <ods-catalog-card-theme-icon></ods-catalog-card-theme-icon>
    <ods-catalog-card-body>
        <ods-catalog-card-title></ods-catalog-card-title>
        <ods-catalog-card-description></ods-catalog-card-description>
        <div class="ods-catalog-card__metadata">
            <ods-catalog-card-metadata-item item-title="Publisher" item-key="publisher"></ods-catalog-card-metadata-item>
            <ods-catalog-card-metadata-item item-title="License" item-key="license"></ods-catalog-card-metadata-item>
        </div>
        <ods-catalog-card-keywords></ods-catalog-card-keywords>
    </ods-catalog-card-body>
    <ods-catalog-card-visualizations></ods-catalog-card-visualizations>
</ods-catalog-card>
```

## The default one ++ 

```html
<ods-catalog-card class="defaultplusplus">
    <ods-catalog-card-theme-icon></ods-catalog-card-theme-icon>
    <ods-catalog-card-body>
        <ods-catalog-card-title></ods-catalog-card-title>
        <ods-catalog-card-description></ods-catalog-card-description>
        <ods-catalog-card-keywords></ods-catalog-card-keywords>
        <div class="ods-catalog-card__metadata">
            <ods-catalog-card-metadata-item item-title="Publisher" item-key="publisher"></ods-catalog-card-metadata-item>
            <ods-catalog-card-metadata-item item-title="License" item-key="license"></ods-catalog-card-metadata-item>
            <ods-catalog-card-metadata-item item-title="Modified" item-key="modified"></ods-catalog-card-metadata-item>
            <ods-catalog-card-metadata-item item-title="Records count " item-key="records_count"></ods-catalog-card-metadata-item>
        </div>
    </ods-catalog-card-body>
    <ods-catalog-card-visualizations></ods-catalog-card-visualizations>
</ods-catalog-card>
```

```css
@media screen and (min-width: 768px) {
    ods-catalog-card.defaultplusplus .ods-catalog-card__metadata-item-label {
        width: 110px;
    }
    ods-catalog-card.defaultplusplus .ods-catalog-card__metadata-item-value {
        margin-left: 120px;
    }
}

ods-catalog-card.defaultplusplus .ods-catalog-card__theme-icon {
    top: 5px;
    left: 5px;
    width: 42px;
    height: 42px;
}
```


## highlight dataset

```html
<ods-catalog-card class="defaultstared" ng-class="{'ods-catalog-card-highlighted' : dataset.metas.keyword.indexOf('Discovery') > -1 }">
    <ods-catalog-card-theme-icon></ods-catalog-card-theme-icon>
    <ods-catalog-card-body>
        <ods-catalog-card-title></ods-catalog-card-title>
        <ods-catalog-card-description></ods-catalog-card-description>
        <ods-catalog-card-keywords></ods-catalog-card-keywords>
        <div class="ods-catalog-card__metadata">
            <ods-catalog-card-metadata-item item-title="Publisher" item-key="publisher"></ods-catalog-card-metadata-item>
            <ods-catalog-card-metadata-item item-title="License" item-key="license"></ods-catalog-card-metadata-item>
        </div>
    </ods-catalog-card-body>
    <div class="ods-catalog-card__visualizations">
        <div class="stared">
            <img ng-repeat="kw in dataset.metas.keyword track by $index"
                 ng-if="kw == 'Demo' || kw =='documentation' || kw =='Map'"
                 src="/assets/theme_image/stared.png" />
        </div>
    </div>
</ods-catalog-card>
```

```css
ods-catalog-card.defaultstared .stared {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}
ods-catalog-card.defaultstared .stared img {
    height: 35px;
    width: 35px;
    margin: 3px;
}
.ods-catalog-card-highlighted .ods-catalog-card {
    border: solid 2px #fec101;
}
```
## Full custom by ODS Discovery

```html
<ods-catalog-card class="discovery">    
    <div class="card__title"
         ng-class="{'card__title--stared' : dataset.metas.keyword.indexOf('Demo') != -1}">
        <h2 ng-bind="dataset.metas.title"></h2>
        <ods-theme-picto theme="{{dataset.metas.theme}}" color="white"></ods-theme-picto>
    </div>
    <div class="card__content">
        <div class="card__description-holder">
            <p class="card__description" ng-bind-html="dataset.metas.description|shortSummary|prettyText"></p>
            <div class="stared">
                <img ng-repeat="kw in dataset.metas.keyword track by $index"
                     ng-if="kw == 'Demo' || kw =='documentation' || kw =='Map'"
                     src="/assets/theme_image/stared.png" />
            </div>
        </div>
        <div ng-if="dataset.metas.publisher == 'OpenDataSoft'" class="poweredby">Powered by OpenDataSoft</div>
        <ods-catalog-card-keywords></ods-catalog-card-keywords>
    </div>

    <a ods-main-click=""
       ng-href="{{ '/explore/dataset/' + dataset.datasetid + '/' }}" 
       target="_self">
    </a>
</ods-catalog-card>
```

```css
ods-catalog-card.discovery .ods-catalog-card {
    flex-direction: column;
    padding: 0px
}
ods-catalog-card.discovery .ods-catalog-card:hover {
    background-color: #f5f5f5;
    padding: 0px 0px 0px 2px;
    border-left: 5px solid #1e0c33;
    transition: padding 0.35s ease, border-left 0.35s ease, background 0s;
}
ods-catalog-card.discovery .card__title {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 10px 10px 10px 20px;
    background-color: white;
    border-top: 2px solid #1e0c33;
}
ods-catalog-card.discovery .card__title--stared {
    border-top: 2px solid #EC643C;
}

ods-catalog-card.discovery .card__title h2 {
    color: #1e0c33;
    margin-bottom: 0;
    font-weight: 200;
}
ods-catalog-card.discovery .card__description-holder {
    display: flex;
    justify-content: space-between;
}
ods-catalog-card.discovery .card__description {
    padding: 15px;
}
ods-catalog-card.discovery .stared {
    display: flex;
    margin: 10px;
}
ods-catalog-card.discovery .stared img {
    height: 40px;
}
ods-catalog-card.discovery .ods-catalog-card .odswidget.odswidget-picto.odswidget-theme-picto {
    width: 32px;
    height: 32px;
}
ods-catalog-card.discovery .ods-catalog-card .ods-svginliner__svg-container svg path, 
ods-catalog-card.discovery .ods-catalog-card .ods-svginliner__svg-container svg rect, 
ods-catalog-card.discovery .ods-catalog-card .ods-svginliner__svg-container svg polygon {
    fill: #1e0c33 !important;
}
ods-catalog-card.discovery .ods-catalog-card__keywords {
    margin-left: 20px;
    margin-bottom: 10px;
}

ods-catalog-card.discovery .poweredby {
    transform: rotate(-16deg);
    position: absolute;
    top: 50px;
    left: 50px;
    font-size: 1.8em;
    opacity: 0.5;
    font-weight: 400;
    color: #ec653d;
    text-align: center;
}
```


