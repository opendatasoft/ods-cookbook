# Local development environment

For an easier development phase, it might me useful to work locally (local server, and local files) and then, once
finished, copy-paste your code into your online environment

The biggest advantage for big and complex pages is the ability to split your code into several pieces and then compile
and reassemble the whole content to copy-paste it online.

**This toolkit helps to develop locally, compile your code, and even push it directly to your domain through the Automation API**

This toolkit is composed of several `gulp` tasks. `gulp` is a toolkit for automating tasks in your development. (also
called a task runner).


### What's new in 4.2
- Removal of Management API for the Automation API
- Updated gulp processes to reflect the changes in portal

## List of tasks

### Main tasks

#### **server**

Starts the web server with a auto-refresh module that reload automatically your page when any resource is modified.
Pretty useful during your development to see the modifications while you code.

#### **compile**

Compile web resources and build a single HTML and CSS file to upload on Huwise.

#### **update**

Update the Huwise page by replacing it's content by the compile local resources.
(this task triggers **get, compile, edit, put** tasks)

* **get** Get the page properties structure from the API (according to the json configuration file).
* **compile** Compile HTML and CSS local resources.
* **edit** Edit the properties structure whith the compiled resources.
* **put** Put the new resources to the API (according to the json configuration file).
* **publish** Publishes the pages a


#### **clean**

Delete temporary folders and compiled files

#### **newproject loadproject listprojects save**

Versioning and backup commands to create, load and save your work

# Setup

### Get the proper tree view

```
\- app.js
     \- pages
         \- views <--- your HTML content (as EJS or HTML)
         \- style <--- your CSS content (as SCSS or CSS)
     \- ods-portal
         \- ods-code-widgets <--- optionnal/local libs from ODS
         \- internal-stylesheets <--- Huwise Syles from the platform
         \- theme.scss <--- your portal theme, to copy here
         \- assets\theme_(image|font)\ <--- assets from the platform
     \- kit <--- technical content, should not be modified 
         \- scripts <--- HTTP hooks for enriching or modifing local requests
         \- styles <--- CSS page structure for local development
         \- views <--- HTML page structure for local development

    \- config.js <--- Contains private credientials MUST NOT BE COMMIT
    \- config.project.js <--- Contains project specific varaibles
```

`index-*.ejs` are the starting point. It loads all pre-requisites, CSS libs, JS libs etc... and run them all.

Then, it includes `page.ejs` that is a single ODS page.

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


### Install dependencies

Install nodeJs packages

```
npm install
```

Gulp is then available locally, install it globally ! :

```
npm install -g gulp
```

Then, to see the list of available tasks

```
gulp --tasks 
```

Finally, copy `config.example.js` to `config.js`

```
cp config.example.js config.js
```

And to run a task simply `gulp <task>` to execute.

For example:

```
gulp server
```

The command `gulp server` spins up a local server on your computer that can be accessed by entering in your favorite
browser the local URLs that are displayed when you execute the command. If you use Google Chrome, this command will even
automatically open the URL on Google Chrome. If you don't have Google Chrome or wish to use another web browser, open
the `config.js` file and modify the `BROWSER` variable. For instance, replace `BROWSER: "google chrome"`
by `BROWSER: "firefox"`. Then execute the `gulp server` command.

## Good to know

### Local server and templating with `Express` and `EJS`

https://expressjs.com/

Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web
applications.

We will use Express to create a simple tree view of our application

https://ejs.co/

EJS is a simple templating language that lets you generate HTML markup with plain JavaScript.

We will use EJS to create layouts to have a well structured and organized layout for our app

### CSS with `Sass`

https://en.wikipedia.org/wiki/Sass_(stylesheet_language)

Sass provide the ability to include CSS stylesheets into another, we will mainly use this feature to write cleaner and
more efficient code. Once you have a Sass tree view, you can compile it back to regular CSS to use it in the platform.

## Proxy settings

If the network proxy has a self-signed certificate, you will need to run this command before trying to `gulp update`

```
export NODE_TLS_REJECT_UNAUTHORIZED='0'
```