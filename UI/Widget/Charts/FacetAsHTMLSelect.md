### Feed an HTML Select with Facet values

In this case, we want to force a refine by default, and allo the user to switch to another one.
The HTML select if fed by the values of a facet.

Dataset : [here] (http://public.opendatasoft.com/explore/dataset/titres-diffuses-sur-6-stations-de-radios-francaises/?tab=table)
 
'''
<ods-dataset-context  
                 context="test"
                 test-domain="public"
                 test-dataset="titres-diffuses-sur-6-stations-de-radios-francaises" 
                 test-parameters="{'sort':'radio'}"> <!-- Sort to choose the default refine -->

    <div ng-repeat="j in items" ods-results="items" ods-results-context="test" ods-results-max="1">
        
        {{ j.fields.radio }} 
        
            <h4>
                Select fed by a facet + Auto refine on first value + ability to select another value to update the refine            
            </h4>
            <select ng-if="j"
                    ng-model="test.parameters['refine.radio']" 
                    ng-init="test.parameters['refine.radio']=j.fields.radio"
                    > <!-- Work on radio refine and apply a refine at init. -->
                <option
                        ng-repeat="item in items" 
                        ng-selected="item.name == j.fields.radio"
                        ods-facet-results="items" 
                        ods-facet-results-context="test"
                        ods-facet-results-facet-name="radio" 
                        value="{{item.name}}">
                    {{item.name}}
                </option>
            </select>

            <h4>
                Facet to illustrate what is refined by the select            
            </h4>
            <ods-facets ng-if="j" context="test">
                <ods-facet name="radio" disjunctive="true"></ods-facet>
            </ods-facets>

    </div>
</ods-dataset-context>
'''