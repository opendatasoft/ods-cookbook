### How to restrict the content of a page

Content on a page can be restricted depending of the user's rights on a dataset, i.e. the content will not be displayed if the user can't access the data.
The restriction is applied with a ng-if attribute so only the content in the tag with the ng-if on is affected.

Example to restrict a whole page:

```html
<ods-dataset-context context="ctx" ctx-dataset="my-restricted-dataset">

    <div ng-if="ctx && ctx.dataset && ctx.error">
        <!-- everything here ONLY if the user doesn't have the rights on the dataset -->
        <!-- or if something wrong happened -->
        No data available or you don't have access to this content
    </div>

    <div ng-if="ctx && ctx.dataset && !ctx.error">
        <!-- everything here is restricted -->
        <h1>The page title</h1>
        The page content
        Some map: <ods-map context="ctx"></ods-map>
    </div>

    <!-- everything outside is NOT restricted and ALWAYS displayed -->

</ods-dataset-context>
```