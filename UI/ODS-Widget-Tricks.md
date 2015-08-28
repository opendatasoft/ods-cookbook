# UI OpenDataSoft Widget Tricks
 
## Charts 

### How to hide some legends with CSS code

When two many legends are display above a chart, it's messy.

Consider a timeline X axis with quarters.

<pre>
00:00
00:15
00:30
00:45
01:00
01:15
01:30
01:45
02:00
...
</pre>

You want to only display hours and skip 1 2 and 3 quarter of an hour, just add this CSS code to your page :

```css
@media (max-width: 1200px) {
    #mychart .highcharts-xaxis-labels text:nth-child(4n+2) { display: none; }
    #mychart .highcharts-xaxis-labels text:nth-child(4n+3) { display: none; }
    #mychart .highcharts-xaxis-labels text:nth-child(4n+4) { display: none; }
}
```

`#mychart` the HTML id of my chart.
Child numbering starts at 1, `n` formula variable starts at 0.  
So, it applies a `display: none;` on child 2, 3, 4, 6, 7, 8, 10 etc...
[More about nth-child here] (http://www.w3schools.com/cssref/sel_nth-child.asp, "W3Schoolds nth-child selector")



### How to display chart data into a data table

Consider a dataset containing male and female profile with their height and weight.
Each profile is validated or not.

We would like to display in a chart the average height and weight split by gender.
We would also like to split the gender axis by a second dimension : the account validation status.

Data sample : 

<pre>
#1
gender : 2 (Male)
height: 187
weight: 74
isvalid: 1

#2
gender : 1 (Female)
height: 187
weight: 74
isvalid: 0
</pre>

Chart HTML code :

```html
<ods-chart single-y-axis="true">
    <ods-chart-query context="mycontext" field-x="gender" series-breakdown="isvalid">
        <ods-chart-serie expression-y="height" chart-type="column" function-y="AVG" color="range-Dark2">
        </ods-chart-serie>
        <ods-chart-serie expression-y="weight" chart-type="column" function-y="AVG" color="range-Dark2">
        </ods-chart-serie>
    </ods-chart-query>
</ods-chart>
```


Chart result :

![Chart to table](./chart_to_table.png "Chart to table")



Now, to display these values into a table, let's add this code into your ods-context :

Table HTML code :

```html
<table>
    <thead>
      <tr>
        <td>Height</td>
        <td>Weight</td>
        <td>Gender (account state)</td>
      </tr>
    </thead>
    <tbody>
      <tr ng-repeat="result in analysis.results"
           ods-analysis="analysis"
           ods-analysis-context="mycontext"
           ods-analysis-max="50"
           ods-analysis-x="gender"
           ods-analysis-x-split="isvalid"
           ods-analysis-serie-height="AVG(height)"
           ods-analysis-serie-weight="AVG(weight)"
           >
        <td ng-repeat="(i,e) in result">
          <p ng-if="!e.gender && !e.isvalid">
            {{ e }}
          </p>
          <div ng-if="e.gender == 1">
            Male
          </div>
          <div ng-if="e.isvalid == 1">
            (validated profile)
          </div>
          <div ng-if="e.gender == 2">
            Female
          </div>
          <div ng-if="e.isvalid == 0">
            (not validated)
          </div>
        </td>
      </tr>
    </tbody>  
</table>
```


Table result :

| Height             | Weight            | Gender (account state)    |
|--------------------|-------------------|---------------------------|
| 167.75321336760925 | 60.65638389031705 | Male (not validated)      |
| 168.01616322204558 | 61.27265500794912 | Male (validated profile)  |
| 177.17472719924558 | 74.3245318604338  | Female (not validated)    |
| 177.8441081661891  | 75.00420845272207 | Female (validated profile)|



