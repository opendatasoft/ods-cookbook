# ODS starter-kit with snowpack

> ✨ Test and play with widgets and ods SDKs easily

This package helps you to run a static website instantly with all the required scripts to run ods-widgets and ods SDKs.
Simply install dependencies and run.

The example page query the API with `@opendatasoft/api-client` and with an `ods-adv-analysis` widget. 

## Available commands

### npm install

Install all dependencies, must be run first

### npm run dev

Runs the app in the development mode.
Open http://localhost:8080 to view it in the browser.

The page will reload if you make edits.
You will also see any lint errors in the console.

### npm run build

Builds a static copy of your site to the `build/` folder.
Your app is ready to be deployed!

**For the best production performance:** Add a build bundler plugin like [@snowpack/plugin-webpack](https://github.com/snowpackjs/snowpack/tree/master/plugins/plugin-webpack) or [snowpack-plugin-rollup-bundle](https://github.com/ParamagicDev/snowpack-plugin-rollup-bundle) to your `snowpack.config.json` config file.
