### Ods-Timerange tricks

#### 'Last one month' default selection

How to select by default the last month from now :

From : 1 month ago
To : now

```html
<ods-dataset-context context="ds"
                     ds-dataset="ods-activity_log-monitoring" 
                     ds-parameters="{'source':'monitoring'}">

    <div ods-datetime="now">

        <ods-timerange display-time="false"
                       date-format="DD/MM/YYYY"
                       context="ds"
                       default-from="{{ now | momentadd : 'months' : -1 }}"
                       default-to="{{ now }}">
        </ods-timerange>
        
    </div>
 
    <ods-table context="ds"></ods-table>
    
</ods-dataset-context>
</ods-dataset-context>
```

#### How to have different behavior depending on the selected timerange

Display if the time range is bigger or smaller than 6 months

```html
<ods-dataset-context ng-init="var={'dates': {'to': '', 'from': ''}]"
                     context="ds"
                     ds-dataset="ods-activity_log-monitoring" 
                     ds-parameters="{'source':'monitoring'}">

    <div ods-datetime="now">

        <ods-timerange display-time="false"
                       date-format="DD/MM/YYYY"
                       context="ds"
                       default-from="{{ now | momentadd : 'months' : -1 }}"
                       default-to="{{ now }}"
                       to="var.dates.to"
                       from="var.dates.from">
        </ods-timerange>

        <p ng-if="var.dates.from| isAfter : (var.dates.to|momentadd:'month':-6)">
            Moins de 6 mois d'écart
        </p>

        <p ng-if="var.dates.from| isBefore : (var.dates.to|momentadd:'month':-6)">
            Plus de 6 mois d'écart
        </p>

    </div>
    
    <ods-table context="ds"></ods-table>
    
</ods-dataset-context>
```