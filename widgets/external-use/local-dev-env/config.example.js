module.exports = {
    ODS_PORTAL_DOMAIN: '<DOMAIN ID>',
    ODS_USERNAME: '<USERNAME>',
    ODS_PASSWORD: '<PASSWORD>',
    PAGE_ID: '<ID>',

    // Command-line defaults
    DEFAULT_EJSFILE: 'views/ods-app.ejs',
    DEFAULT_LESSFILE: 'static/stylesheets/index.less',

    // Adv. settings
    WATCH_DIRS: [
        "./static/**/*.less",
        "./static/**/*.css",
        "./views/**/*.html",
        "./views/**/*.ejs"
    ],
    BROWSER: "google chrome",

    // You usually shouldn't have to edit these
    ODS_PORTAL_SUFFIX: '.opendatasoft.com',
    SERVER_PORT: 9090,
    OUTPUT_DIR: 'output'
};