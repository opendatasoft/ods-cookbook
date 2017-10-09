## Contact form 

### How to add a custom field

You can add custom input field to the contact form widget.

[Discovery example]() includes a multi-choice drop down list. 

```html
<ods-page-contact-form class="ods-box ods-page__contact-page__contact-form" 
                               id="block-contact" 
                               page-id="pageId"
                               additional-fields="[{'id': 'querytype', 'name': 'querytype', 'label': 'Type', 'type': 'choice', 'choices': ['General question', 'Ask for a feature demo', 'Report an issue', 'Other'], 'required': true }]"></ods-page-contact-form>
```

But you can also go for simple input text like this :

```
additional-fields="[{'id': 'test1', 'name': 'test1', 'label': 'Test champ 1', 'type': 'choice', 'choices': ['Value 1', 'Value 2'] }, {'id': 'test2', 'name': 'test2', 'label': 'Test champ 2', 'type': 'text', 'required': 'true' }]"
```
