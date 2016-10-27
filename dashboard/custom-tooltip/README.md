# Custom tooltip !

#### Live result

[Please find the live exemple on Discovery](https://discovery.opendatasoft.com/pages/demo-custom-tooltip/)

#### Code - Default version

**Default** : information are displayed with OpenDataSoft Map default style 

```html
<ods-map style="height:600px" location="8,41.35826,-72.23511">
    <ods-map-layer color="#2C3F56" context="ushospitals">
    </ods-map-layer>
</ods-map>
```

#### Code - Advanced version

**Advanced** : information are displayed differently with colors, icons and links  

```html
<ods-map style="height:600px" location="8,41.35826,-72.23511">
    <ods-map-layer picto="hospital" color="#2C3F56" context="ushospitals">
        <ul style="display: block; list-style-type: none; color: #2c3f56; padding:0; margin:0;">
            <li><strong style="font-size:17px;">{{ record.fields.name | limitTo:25 }}</strong></li>
            <li style="color:#bbb;">{{ record.fields.address | limitTo:140 }}</li>
            <li style="font-style:italic;color:#bbb;">{{ record.fields.city | limitTo:140 }}<br/></li>
            <br/>
            <li style="color:#ec643c; font-size:15px;">
                <i class="fa fa-hospital-o"></i> {{record.fields.type}}
            </li>
            <li style="font-size:15px;">
                <i class="fa fa-calendar-o"></i>
                <span style="font-size: 14px; color: #bcbcbc;">Established </span> {{record.fields.date_creat | date}}
            </li>
            <li style="font-size:15px;">
                <i class="fa fa-medkit"></i>
                <span style="font-size: 14px; color: #bcbcbc;">Trauma </span> {{record.fields.trauma }}
            </li>
            <li style="font-size:15px;">
                <i class="fa fa-dot-circle-o"></i>
                <span style="font-size: 14px; color: #bcbcbc;">Helipad </span>{{record.fields.helipad}}
            </li>
            <li>
                <ul style="list-style-type: none; color: #2c3f56;padding:0 0 15px;margin-top:0px;">
                    <li>
                        <strong style="font-size:15px;">
                            <i aria-hidden="true" class="fa fa-users"></i><span style="color: #bcbcbc;"> Population/Beds </span>{{record.fields.population}}
                        </strong>
                    </li>
                    <li style="float:right;"><strong style="font-size:13px;"><a ng-href="{{record.fields.website}}" style="color:#ec643c;" target="_blank">Source </a></strong><i class="fa fa-external-link" style="color:#ec643c;"></i></li>
                </ul>
            </li>
        </ul>
    </ods-map-layer>
</ods-map>
```


#### Code - Analytic version
 
**Analytic** : tooltip present dynamic aggregation based on the dataset API. A smaller value than the average will be in red, a greater one in green
 
```html
<ods-map id="analytics" style="height:600px" location="8,41.35826,-72.23511">
    <ods-map-layer color="#2C3F56" picto="hospital" context="ushospitals">
        <ul style="display: block; list-style-type: none; color: #2c3f56; padding:0; margin:0;">
            <li><strong style="font-size:17px;">{{ record.fields.name | limitTo:25 }}</strong></li>
            <li style="color:#bbb;">{{ record.fields.address | limitTo:140 }}</li>
            <li style="font-style:italic;color:#bbb;">{{ record.fields.city | limitTo:140 }}<br/></li>
            <br/>

            <ods-dataset-context context="type,state"
                                 type-dataset="us-hospitals" 
                                 type-parameters="{'refine.type':''+record.fields.type}"
                                 state-dataset="us-hospitals"
                                 state-parameters="{'refine.state':''+record.fields.state}">
                <div style=""
                     ods-aggregation="aggtype"
                     ods-aggregation-context="type"
                     ods-aggregation-function="AVG"
                     ods-aggregation-expression="beds">
                    <li style="color:#ec643c; font-size:15px; border-left: 3px solid #f19073;padding-left: 5px;">
                        <i class="fa fa-bed"></i> Avg # of beds for
                    </li>
                    <li style="color: #ec643c;font-size: 15px;text-align: center;">
                        <strong>{{record.fields.type}}</strong>
                    </li>
                    <li ng-if="!aggtype"
                        style="text-align:center;font-size:20px">
                        <ods-spinner></ods-spinner>
                    </li>
                    <li ng-if="aggtype"
                        style="text-align:center;" 
                        ng-class="{'red': record.fields.beds < aggtype, 'green' : record.fields.beds > aggtype}">
                        <strong style="font-size:20px;">
                            {{ aggtype | number : 1 }}
                        </strong>
                    </li>
                </div>
                <br/>
                <div style=""
                     ods-aggregation="aggstate"
                     ods-aggregation-context="state"
                     ods-aggregation-function="AVG"
                     ods-aggregation-expression="beds">
                    <li style="color: #ec643c;font-size: 15px;text-align: center;">
                        <strong>{{record.fields.state}}</strong>
                    </li>
                    <li ng-if="!aggstate"
                        style="text-align:center;font-size:20px">
                        <ods-spinner></ods-spinner>
                    </li>
                    <li ng-if="aggstate"
                        style="text-align:center;" 
                        ng-class="{'red': record.fields.beds < aggstate, 'green' : record.fields.beds > aggstate}">
                        <strong style="font-size:20px;">
                            {{ aggstate | number : 1 }}
                        </strong>
                    </li>
                </div>
            </ods-dataset-context>

            <li style="margin-top: 20px">
                <ul style="list-style-type: none; color: #2c3f56;padding:0 0 15px;margin-top:0px;">
                    <li style="display: inline;float:left;"><strong style="font-size:15px;"><i aria-hidden="true" class="fa fa-users"></i> Population/Beds : {{record.fields.beds}}</strong></li>
                    <li style="display: inline;float:right;"><strong style="font-size:13px;"><a ng-href="{{record.fields.website}}" style="color:#ec643c;" target="_blank">Source </a></strong><i class="fa fa-external-link" style="color:#ec643c;"></i></li>
                </ul>
            </li>
        </ul>

    </ods-map-layer>
</ods-map>
```
