# Local development environment

For an easier development phase, it might be useful to work locally (local server, and local files) and then, once finished, copy-paste your code into your online environment.

The biggest advantage for big and complex pages is the ability to split your code into several pieces and then compile and reassemble the whole content to copy-paste it online.

**This guide helps to go through the usage of 2 different methods, Less for CSS compiling, and EJS for HTML compiling** 

## CSS with Less

http://lesscss.org

Less provide the ability to include CSS stylesheets into anothers, we will mainly use this aspect to write cleaner and more efficient code.
Once you have a Less tree view, you can compile it back to regular CSS to use it in the platform.

To do so, follow these steps
(pre-requisites: having npm installed)

##### Install lessc
```bash
http://lesscss.org
```

`lessc` command line usage:
```
lessc [option option=parameter ...] <source> [destination]
```

##### Compile your less code
```
mkdir -p output
lessc static/stylesheets/index.less output/output.css
```

Then simply copy paste `output.css` content



## Local server and templating with `Express` and `EJS`

https://expressjs.com/

Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web applications.

We will use Express to create a simple tree view of our application.

https://ejs.co/

EJS is a simple templating language that lets you generate HTML markup with plain JavaScript.

We will use EJS to create layouts to have a well structured and organized layout for our app.


##### Install both

```npm install express --save```

```npm install ejs```

##### Get the proper tree view

```
\- app.js
     \- static
         \- lib <--- optionnal/local libs
         \- stylesheets <--- less playground
     \- views
         \- index.ejs <--- main EJS template, the STARTING point
         \- headers.ejs <--- all head includes
         \- subbody.ejs <--- all angularjs and widgets scripts
         \- ods-app.ejs <--- the ODS App container
         \- ods-app.html <--- the ODS App content

```

`index.ejs` is the starting point.
It loads all pre-requisites, CSS libs, JS libs etc... and loads them all.

Then, it loads ods-app.html which is a single page ODS app. 

But we can also imagine a more complex setup with a middle level:

```
\- views
    \- index.ejs <--- loads blocks.ejs
    \- blocks.ejs <--- loads block1.html, block2.html, block3.ejs
    \- block1.html
    \- block2.html
    \- block3.ejs
    \- block3content.html
```

blocks.ejs :
```
<div>
    <div>
        <%- include('block1.html'); -%>
    </div>
    <div>
        <%- include('block2.html'); -%>
    </div>
    <div>
        <%- include('block3.ejs'); -%>
    </div>
</div>
```

block3.ejs
```
<h2>
    Block 3
</h2>
<%- include('block3content.html'); -%>
```

then, HTML pages might include any HTML content.

##### Result

```
<div>
    <div>
        <h2>
            Block 1
        </h2>    
    </div>
    <div>
        <h2>
            Block 2
        </h2>    
    </div>
    <div>
        <h2>
            Block 3
        </h2>
        <h3>
            Block 3 sub content
        </h3>    
    </div>
</div>
```

### Finally, compile HTML 

Usage
```
node compile.js <ejs file> <output file>
```

Finally, to export your HTML code, use the `compile.js` node helper to generate automatically the final code to copy-paste on the platform

```
mkdir -p output
node compile.js ./views/ods-app.ejs output/output.html
```


**N.B.:** to generate the entire page for external-usage, you can also start the generation from the `index.ejs` page
```
node compile.js ./views/index.ejs test.html
```
