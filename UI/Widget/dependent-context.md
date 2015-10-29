# Dependent context

## Goal
The current case is the following: we have energy consumption data available in a dataset. 
We want to see what the current year's consumption is and compare it to the previous year's at the same date.

## Code
```html
<ods-dataset-context context="energy2014,energy2015"
                     energy2014-dataset="energy_consumption"
                     energy2014-parameters="{'disjunctive.siteref':'true','q': ''}"
                     energy2015-dataset="energy_consumption"
                     energy2015-parameters="{'disjunctive.siteref':'true','refine.date':'2015'}">
    <ods-results ods-results="items" ods-results-context="energy2015" ods-results-max="1">     
        <div ng-if="items" ng-init="energy2014.parameters.q = 'date:[2014 TO ' + (items[0].fields.date|momentadd:'year':-1) + ']'">
            <div ods-analysis="totalEnergy2015"
                 ods-analysis-context="energy2015"
                 ods-analysis-serie-conso="SUM(conso)">
            </div>
            <div ods-analysis="totalEnergy2014"
                 ods-analysis-context="energy2014"
                 ods-analysis-serie-conso="SUM(conso)">
            </div>
            
            <p>
                Consumption in 2015: {{ totalEnergy2015.results[0].conso | number:0}} kWh <br>
                Variation from 2014: {{ ((totalEnergy2015.results[0].conso - totalEnergy2014.results[0].conso) / totalEnergy2014.results[0].conso * 100)|number:0 }}%            
            </p>
        </div>
    </ods-results>
</ods-dataset-context>
```

## Explanations

* The ng-if prevents multiple requests from being made for the energy2014 context.
* We are using ods-results and not ods-result-enumerator because ods-result-enumerator isolates its content in a distinct scope.
* We are using ods-analysis instead of ods-aggregation for the same reason.
