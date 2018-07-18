# Ods-Timerange tricks

## Live demo

[Please find the live exemple on Discovery](https://discovery.opendatasoft.com/pages/date-tricks-home/)

## Code

### 'Last three month' default selection

The default start date is set to now minus 3 months, and the default end date is set to now

HTML code:
```html
    <ods-dataset-context context="ds" 
                         ds-dataset="global-shark-attack-c"
                         ds-parameters="{'sort':'date'}">

        ...
        <div ods-datetime="now">

            <ods-timerange display-time="false"
                           date-format="MM/DD/YYYY"
                           context="ds"
                           default-from="{{ now | momentadd : 'months' : -3 }}"
                           default-to="{{ now }}">
            </ods-timerange>

        </div>

        <br/>
        <ods-table context="ds"></ods-table>

    </ods-dataset-context>
```

CSS code:
```css
.odswidget-timerange {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.input-holder, .odswidget-timerange__from, .odswidget-timerange__to {
    border: 1px solid #e4e4e4;
    padding: 10px;
    border-radius: 3px;
    box-shadow: 1px 1px 5px gainsboro;
    background-color: white;
    z-index: 2;
    margin-bottom: 10px;
    
    display: flex;
    align-items: center;
    
    margin: 3px;
}
.odswidget-timerange__from {
    margin-right: 10px;
}
.input-holder input, .odswidget-timerange__from input, .odswidget-timerange__to input {
    border: none;
    width: 153px;
    margin-left: 8px;
}
.input-holder input:focus, .odswidget-timerange__from input:focus, .odswidget-timerange__to input:focus {
    outline: 0;
}
```

### Compute the range date size

Get the number of hours, days, months or any units you'd like between the from and to selection.

HTML code:
```html

    <ods-dataset-context context="ds" 
                         ds-dataset="global-shark-attack-c"
                         ds-parameters="{'sort':'date'}"
                         ds-parameters="{'sort':'date'}"
                         ng-init="dates = {'to': '', 'from': ''}">

        ...
        <div ods-datetime="now">

            <ods-timerange display-time="false"
                           date-format="MM/DD/YYYY"
                           context="ds"
                           default-from="{{ now | momentadd : 'months' : -1 }}"
                           default-to="{{ now }}"
                           to="dates.to"
                           from="dates.from">
            </ods-timerange>


            {{ nbdays = (dates.to | momentdiff : dates.from : 'days') ; "" }}

            <h4>
                Current selection : {{ nbdays }} day{{nbdays>1?'s':''}} range
            </h4>
            <p>
                This value can then help to have different behavior/displays in your dashboard depending on the date range.<br/>
                The typical usecase is to display a chart with hour precision in case of a small range of a few days, and switch to a day chart precision in case of a several week range selection. The dashboard can then adapt the chart precision to make it more readable.
            </p>
            <h4 ng-if="nbdays <= 90">
                Less or equals than 3 months range
            </h4>
            <h4 ng-if="nbdays > 90">
                More than 3 months range
            </h4>

            <br/>

            <h3>
                Other date comparators can detect if a date if before or after another one
            </h3>
            <h4 ng-if="dates.from | isAfter : now">
                'From' selection is in the futur
            </h4>
            <h4 ng-if="dates.from | isBefore : (now | momentadd : 'days' : -1)">
                'From' selection is in the past
            </h4>
            <h4 ng-if="!(dates.from | isBefore : (now | momentadd : 'days' : -1)) && !(dates.from | isAfter : now)">
                'From' selection is today !
            </h4>
            
            <h4 ng-if="dates.to | isAfter : (now | momentadd : 'days' : 1)">
                'To' selection is in the futur
            </h4>
            <h4 ng-if="dates.to | isBefore : now">
                'To' selection is in the past
            </h4>
            <h4 ng-if="!(dates.to | isAfter : (now | momentadd : 'days' : 1)) && !(dates.to | isBefore : now)">
                'To' selection is today !
            </h4>
        </div>

    </ods-dataset-context>
```

CSS code:
```css

.odswidget-timerange {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.input-holder, .odswidget-timerange__from, .odswidget-timerange__to {
    border: 1px solid #e4e4e4;
    padding: 10px;
    border-radius: 3px;
    box-shadow: 1px 1px 5px gainsboro;
    background-color: white;
    z-index: 2;
    margin-bottom: 10px;
    
    display: flex;
    align-items: center;
    
    margin: 3px;
}
.odswidget-timerange__from {
    margin-right: 10px;
}
.input-holder input, .odswidget-timerange__from input, .odswidget-timerange__to input {
    border: none;
    width: 153px;
    margin-left: 8px;
}
.input-holder input:focus, .odswidget-timerange__from input:focus, .odswidget-timerange__to input:focus {
    outline: 0;
}
```

### Filter on two different date fields (start and end date)

This example use the ods-timerange widget to set from and to date, and then filter an event dataset on two different fields.

This is particuarily useful for events dataset with a begining date of the event and an end date. The timerange selection helps the user to provide his availability, and the result displays events available on this selected period.

HTML code:
```html
    <ods-dataset-context context="ds,timerange" 
                         ds-dataset="evenements-publics-openagenda"
                         timerange-dataset="evenements-publics-openagenda"
                         ds-parameters="{'sort':'date_start'}"
                         ng-init="dates = {'to': '', 'from': ''}">

        ...

        <div ods-datetime="now">

            <ods-timerange display-time="false"
                           date-format="MM/DD/YYYY"
                           context="timerange"
                           default-from="{{ now | momentadd : 'days' : -2 }}"
                           default-to="{{ now }}"
                           to="dates.to"
                           from="dates.from">
            </ods-timerange>

            {{ ds.parameters['q'] = 'date_start:[1900-01-01 TO ' + (dates.to?dates.to:'2099-01-01') + '] AND date_end >= ' + (dates.from?dates.from:'1900-01-01') ; "" }}

        </div>

        <br/>

        <ods-table context="ds"></ods-table>

    </ods-dataset-context>
```

CSS code:
```css
.odswidget-timerange {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.input-holder, .odswidget-timerange__from, .odswidget-timerange__to {
    border: 1px solid #e4e4e4;
    padding: 10px;
    border-radius: 3px;
    box-shadow: 1px 1px 5px gainsboro;
    background-color: white;
    z-index: 2;
    margin-bottom: 10px;
    
    display: flex;
    align-items: center;
    
    margin: 3px;
}
.odswidget-timerange__from {
    margin-right: 10px;
}
.input-holder input, .odswidget-timerange__from input, .odswidget-timerange__to input {
    border: none;
    width: 153px;
    margin-left: 8px;
}
.input-holder input:focus, .odswidget-timerange__from input:focus, .odswidget-timerange__to input:focus {
    outline: 0;
}

```

### Select current, past or next week

This is a dedicated dashboard, [jump here to reach and get the code](../../dashboard/canteen-menu)


### Single date picker + range slider

This example highlights two usages. The ability to have a single date picker instead of two usually. But also the use of sliders to play with date ranges.

This combination is pretty useful to facilitate range selection for the end user.

HTML code:
```html
    <ods-dataset-context context="ds,timerange" 
                         ds-dataset="evenements-publics-openagenda"
                         timerange-dataset="evenements-publics-openagenda"
                         ds-parameters="{'sort':'date_start'}"
                         ng-init="dates = {'to': '', 'from': ''};
                                  dayrange = 7">

        ...

        <p style="text-align: center">
            <strong>Current selection:</strong> events starting from the <strong>{{ dates.from | date }}</strong> to the <strong>{{ (dates.to | momentadd : 'days' : dayrange) | date }}</strong> (<strong>+{{ dayrange }} day{{dayrange>1?'s':''}}</strong>)
        </p>

        <div class="controlers">
            <div class="controler control-date">
                <h2>
                    Starting date
                </h2>
                <div ods-datetime="now">
                    <ods-timerange display-time="false"
                                   date-format="MM/DD/YYYY"
                                   context="timerange"
                                   default-from="{{ now }}"
                                   default-to="{{ now }}"
                                   to="dates.to"
                                   from="dates.from">
                    </ods-timerange>
                </div>
            </div>
            <div class="controler control-range">
                <h2>
                    Day range
                </h2>
                <div class="input-range-with-button">
                    <input type="range" min="0" max="14" step="1"
                           ng-model="dayrange"
                           ng-model-options="{ debounce: { 'default': 300 }}" />
                </div>
            </div>
        </div>

        {{ ds.parameters['q'] = 'date_start:[' + dates.from + ' TO ' + (dates.to | momentadd : 'days' : dayrange) + ']' ; "" }}

        <br/>

        <ods-chart>
            <ods-chart-query context="ds" field-x="date_start" maxpoints="0" timescale="day">
                <ods-chart-serie chart-type="column" function-y="COUNT" label-y="Number of events" color="#2C3F56" scientific-display="true">
                </ods-chart-serie>
            </ods-chart-query>
        </ods-chart>


    </ods-dataset-context>
```

CSS code:
```css

.controlers {
    display: flex;
    justify-content: space-around;
    flex-flow: wrap;
}


/* TIMERANGE */

.odswidget-timerange__to {
    display: none;
}

.odswidget-timerange {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.input-holder, .odswidget-timerange__from {
    border: 1px solid #e4e4e4;
    padding: 10px;
    border-radius: 3px;
    box-shadow: 1px 1px 5px gainsboro;
    background-color: white;
    z-index: 2;
    margin-bottom: 10px;

    display: flex;
    align-items: center;

    margin: 3px;
}
.odswidget-timerange__from {
    margin-right: 10px;
}
.input-holder input, .odswidget-timerange__from input {
    border: none;
    width: 110px;
    margin-left: 8px;
}
.input-holder input:focus, .odswidget-timerange__from input:focus {
    outline: 0;
}


/* SLIDER / RANGE */
.controler {
    display: flex;
    margin: 2px 15px;
}
.controler h2 {
    line-height: 2em;
    margin-right: 10px;
}
.control-hour input[type=range] {
    width: 150px;
}
.control-range input[type=range] {
    width: 200px;
}
.input-range-with-button {
    line-height: 3.5em;
}
.controler .ods-button i.fa {
    vertical-align: middle;
}



rect.highcharts-background {
    fill: transparent !important;
}
```


