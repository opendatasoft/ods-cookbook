# Local development environment - Work In Progress version with multi-lingual support

For an easier development phase, it might me useful to work locally (local server, and local files) and then, once
finished, copy-paste your code into your online environment

The biggest advantage for big and complex pages is the ability to split your code into several pieces and then compile
and reassemble the whole content to copy-paste it online.

**This toolkit helps to develop locally, compile your code, and even push it directly to your domain through the
Managment API**

This toolkit is composed of several `gulp` tasks. `gulp` is a toolkit for automating tasks in your development. (also
called a task runner).

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


### Multi-lingual management

Do develop pages in several languages (if several languages are activated on your domain),
the `--lang` option can be provided to `gulp update` and `gulp server` cmds.

#### Use EJS templating to get the translated text

While running the server locally, or compiling the code, i18n module will replace the text of your pages depending on the language.
In the `/i18n/` folder, you'll need to create a dedicated file per language named `[lang key].json`

For example :
```
\- i18n 
    \- de.json
    \- en.json
    \- fr.json
```

The json files must contain the desired keys and there corresponding text value like so :

`en.json` :
```json
{
  "map" : {
    "title": "My huge Map !",
  },
  "other": {
    "buttonLabel": "Back",
    "text": "Emptiness here and there..."
  },
  "loremipsum": "Lorem ipsum dolor sit amet consectetur ... saepe."
}
```

Finally, to access these texts, use EJS templating tags, through the `i18n` object : `<%- i18n.key %>`

For example in your `page.ejs` :
```html
<h2>
    <%- i18n.map.title %>
</h2>
<div>
    ...
    <%- i18n.loremipsum %>
</div>
<button ng-click="..."><%- i18n.other.buttonLabel %></button>
```

#### Compile in several languages your pages

```
gulp update --lang de,en,fr
```

This command will compile a specific version of the HTML for each language.
These different versions will be then used to push a different content to the management API.

> Note 1 : the CSS remains the same for all versions of the page

> Note 2 : omitting a language is possible, it will then compile only the language provided in the --lang param

> Note 3 : using <%- i18n.xxx %> tag and trying to compile the HTML without provding the --lang param wille provide an error, as the i18n module won't be loaded and there available

#### Run your pages locally in several languages

```
gulp server --lang de,en,fr
```
While running the server locally, the `--lang` option will add a language picker on every pages. To let you switch from a language to another.

# Setup

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
        \- assets\theme_(image|font)\ <--- assets from the platform
    \- kit <--- technical content, should not be modified 
        \- scripts <--- HTTP hooks for enriching or modifing local requests
        \- styles <--- CSS page structure for local development
        \- views <--- HTML page structure for local development
    \- i18n <--- translation files for multi-lingual development
        \- fr.json <--- [lang key].json files containing keys and corresponding value
        \- en.json
        \- ...
    
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

### Get the local dev kit from git

```
mkdir localdevkit
cd localdevkit/
git init
git remote add -f origin https://github.com/opendatasoft/odsapps-team/
git config core.sparseCheckout true
echo "local-dev-env" > .git/info/sparse-checkout
git pull origin master
```

### Install dependencies

Go to local-dev-env folder

```
cd local-dev-env/
```

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

