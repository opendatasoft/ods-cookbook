# Local development environment V4.1

For an easier development phase, it might me useful to work locally (local server, and local files) and then, once finished, copy-paste your code into your online environment

The biggest advantage for big and complex pages is the ability to split your code into several pieces and then compile and reassemble the whole content to copy-paste it online.

**This toolkit helps to develop locally, compile your code, and even push it directly to your domain through the Managment API** 

This toolkit is composed of several `gulp` tasks. `gulp` is a toolkit for automating tasks in your development. (also called a task runner).

### What's new in 4.1

 - `PROXY_URL` parameter added to deal with HTTP Proxy within your organization
 - `BASEPATH` parameter added to set a base path locally to deal with specific development environment within your organization
 - `ODS_ADMIN_APIKEY` parameter will now replace ODS_USERNAME and ODS_PASSWORD parameters, to no longer use basic auth. 
 - Better error logs for gulp update errors
 - /assets will no longer by proxified, they should now be available in the kit

## List of tasks

### Main tasks

#### **server**

Starts the web server with a auto-refresh module that reload automatically your page when any resource is modified.
Pretty useful during your development to see the modifications while you code.

#### **compile**

Compile web resources and build a single HTML and CSS file to upload on ODS

#### **update**

Update the ODS page by replacing it's content by the compile local resources. 
(this task triggers **get, compile, edit, put** tasks)

* **get** Get the page properties structure from the API (according to the json configuration file).
* **compile** Compile HTML and CSS local resources.
* **edit** Edit the properties structure whith the compiled resources.
* **put** Put the new resources to the API (according to the json configuration file).


#### **clean**

Delete temporary folders and compiled files


### Secondary actions 

#### **express-app**

Starts ExpressJS: a local web server
 
#### **browser-sync**

Starts browserSync: a synchronised browser testing tool.

#### **compile-html**

Compile EJS and HTML files into one single HTML file ready to upload on ODS

#### **compile-css**

Compile SASS and CSS files into one single CSS file ready to upload on ODS




## Setup


### Get the proper tree view

```
\- app.js
     \- pages
         \- views <--- your HTML content (as EJS or HTML)
         \- style <--- your CSS content (as SCSS or CSS)
     \- ods-portal
         \- ods-code-widgets <--- optionnal/local libs from ODS
         \- internal-stylesheets <--- ODS Syles from the platform
         \- theme.scss <--- your portal theme, to copy here
     \- kit <--- technical content, should not be modified 
         \- scripts <--- HTTP hooks for enriching or modifing local requests
         \- styles <--- CSS page structure for local development
         \- views <--- HTML page structure for local development

    \- config.js <--- Contains private credientials MUST NOT BE COMMIT
    \- config.project.js <--- Contains project specific varaibles
```

### Install dependencies

Install nodeJs packages
```
npm install
```

Gulp is then available locally:
```
./node_modules/.bin/gulp
```

But you can also install it globally to just call `gulp` directly:
```
npm install -g gulp
```

Then, to see the list of available tasks
```
gulp --tasks 
```

And to run a task simply `gulp <task>` to execute. For exemple:
```
gulp server
```



## Good to know

### Local server and templating with `Express` and `EJS`

https://expressjs.com/

Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web applications.

We will use Express to create a simple tree view of our application

https://ejs.co/

EJS is a simple templating language that lets you generate HTML markup with plain JavaScript.

We will use EJS to create layouts to have a well structured and organized layout for our app


### CSS with `Sass`

https://en.wikipedia.org/wiki/Sass_(stylesheet_language)

Sass provide the ability to include CSS stylesheets into another, we will mainly use this feature to write cleaner and more efficient code.
Once you have a Sass tree view, you can compile it back to regular CSS to use it in the platform.


### Virgin Mac OS install guide

Get brew 

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Get Node JS and npm

```
brew install node
```

Check npm install

```
npm -v
```
