## Print & Share demo !

 - [Dashboard here] (https://discovery.opendatasoft.com/pages/demo-urlsync/)
 
### Main page code :

```html
<div class="container">

    <h2>
        Browse, Search, Filter then Share or Print !    
    </h2>

    <ods-dataset-context context="ctx"
                         ctx-dataset="record-stores"
                         ctx-urlsync="true">
        <div class="row ods-box">
            <h3>
                Share by copying this link : 
            </h3>
            <h4>
                <a href="?{{ ctx.getQueryStringURL() }}"
                   target="_blank">https://discovery.opendatasoft.com/pages/demo-urlsync/?{{ ctx.getQueryStringURL() }}</a>
            </h4>

            <h3>
                Share through social network or by email:
            </h3>
            <div class="boutons" style="font-size: 1.6rem;">
                <a href="https://twitter.com/intent/tweet?text=OpenDataSoft Page Test;url=https%3A%2F%2Fdiscovery.opendatasoft.com%2Fpages%2Fdemo-urlsync%2F%3F{{ctx.getQueryStringURL() | encodeURIComponent}}"
                   class="ods-dataset-visualization__social-button ods-dataset-visualization__social-button--twitter" 
                   target="_blank">
                    <i class="fa fa-twitter ods-dataset-visualization__social-button-icon" aria-hidden="true"></i>
                </a>
                <a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdiscovery.opendatasoft.com%2Fpages%2Fdemo-urlsync%2F%3F{{ctx.getQueryStringURL() | encodeURIComponent}}" 
                   class="ods-dataset-visualization__social-button ods-dataset-visualization__social-button--facebook" 
                   target="_blank">
                    <i class="fa fa-facebook ods-dataset-visualization__social-button-icon" aria-hidden="true"></i>
                </a>
                <a href="https://plus.google.com/share?url=https%3A%2F%2Fdiscovery.opendatasoft.com%2Fpages%2Fdemo-urlsync%2F%3F{{ctx.getQueryStringURL() | encodeURIComponent}}" 
                   class="ods-dataset-visualization__social-button ods-dataset-visualization__social-button--google-plus" 
                   target="_blank">
                    <i class="fa fa-google-plus ods-dataset-visualization__social-button-icon" aria-hidden="true"></i>
                </a>
                <a href="https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fdiscovery.opendatasoft.com%2Fpages%2Fdemo-urlsync%2F%3F{{ctx.getQueryStringURL() | encodeURIComponent}}&amp;mini=true&amp;title=OpenDataSoft Page Test;source=OpenDataSoft" 
                   class="ods-dataset-visualization__social-button ods-dataset-visualization__social-button--linkedin" 
                   target="_blank">
                    <i class="fa fa-linkedin ods-dataset-visualization__social-button-icon" aria-hidden="true"></i>
                </a>
                <a href="mailto:?subject=OpenDataSoft Page Test&amp;body=https%3A%2F%2Fdiscovery.opendatasoft.com%2Fpages%2Fdemo-urlsync%2F%3F{{ctx.getQueryStringURL() | encodeURIComponent}}" 
                   class="ods-dataset-visualization__social-button ods-dataset-visualization__social-button--mail"
                   target="_blank">
                    <i class="fa fa-envelope ods-dataset-visualization__social-button-icon" aria-hidden="true"></i>
                </a>
            </div>
        </div>

        <div class="row ods-box">
            <h3>
                A dashboard : Music record store in the world
            </h3>
            <div class="col-md-3 ods-box">
                <ods-text-search context="ctx" placeholder="disc, records, music..."></ods-text-search>
                <ods-filter-summary context="ctx"></ods-filter-summary>
                <ods-facets context="ctx"></ods-facets>                            
            </div>
            <div class="col-md-9 ods-box">
                <ods-map>
                    <ods-map-layer context="ctx">
                        <div>
                            <h3>
                                {{ record.fields.name }}
                            </h3>
                            <p style="font-style:italic; color:grey; font-weight:300">
                                {{ record.fields.address }}
                            </p>
                            <div style="line-height: 0px;">
                                <p>
                                    <span style="font-style:italic;">Has closed </span><b style="font-size:1.2em">{{ record.fields.hasclosed }}</b>
                                </p>
                                <p>
                                    <span style="font-style:italic;">Active </span><b style="font-size:1.2em">{{ record.fields.active }}</b>
                                </p>
                                <p>
                                    <span style="font-style:italic;">Reviewers </span><b style="font-size:1.2em">{{ record.fields.ratecnt }}</b>
                                </p>
                            </div>
                            <a style="position: absolute; right: 0px; bottom: 0px; color: #1e0c33; font-weight: 600; font-size: 1.1em;" 
                               href="/pages/demo-urlsync-card?q=city:%22{{ record.fields.city }}%22 AND name:%22{{ record.fields.name }}%22"
                               target="_blank">Go to the store card</a>
                        </div>
                    </ods-map-layer>
                </ods-map>
                <div class="ods-box">
                    <ods-table context="ctx"></ods-table>                    
                </div>
            </div>
        </div>

    </ods-dataset-context>

</div>
```

### Secondary page / card code :

```html
<div class="ods-box card">

    <h2>
        Fiche magasin <span style="font-size:0.7em; color:darkred; margin-left:40px">Imprimez la (Ctrl/Cmd+P) ou partagez le lien !</span>
    </h2>

    <ods-dataset-context context="ctx"
                         ctx-dataset="record-stores"
                         ctx-urlsync="true">

        <div ng-repeat="item in items" ods-results="items" ods-results-context="ctx" ods-results-max="1">
            <ul class="field-list">
                <li class="field" ng-repeat="field in ctx.dataset.fields">
                    <p class="label">
                        {{ field.label }}
                    </p>
                    <p class="value">
                        {{ item.fields[field.name] }}
                    </p>
                </li>
            </ul>
        </div>
        
        <ods-map context="ctx"></ods-map>

    </ods-dataset-context>

</div>
```

```css
.card {
    width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.field-list {
    list-style-type: none;
    display: grid;
}
.field {
    display: inline-flex;
    line-height: 25px;
    margin-bottom: 5px;
}

.label {
    width: 175px;
    color: black;
    font-weight: 500;
}

.value {
    width: 400px;
    border: 1px solid black;
    border-radius: 5px;
    padding: 2px 0px 0px 5px;
    line-height: 25px;
    background-color: #f0f0f0;
}
```
