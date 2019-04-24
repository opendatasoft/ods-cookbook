var yargs = require('yargs');
var argv = yargs.argv;
var config = require('./config');

var gulp = require('gulp');

var del = require('del');
gulp.task('clean', function () {
    return del([config.OUTPUT_DIR, 'tmp']);
});

/* SERVER */
var gls = require('gulp-live-server');
var browserSync = require('browser-sync');

gulp.task('express-app', async function () {
    var server = gls.new(['./app.js', '--port', config.SERVER_PORT]);
    server.start();
});

gulp.task('browser-sync', function () {
    browserSync.init(null, {
        proxy: "http://localhost:" + config.SERVER_PORT,
        files: config.WATCH_DIRS,
        browser: config.BROWSER,
        port: (1 * config.SERVER_PORT + 1),
    });
});

gulp.task('server', gulp.series('express-app', 'browser-sync'));

/* HTML */
var ejs = require('gulp-ejs');
const rename = require('gulp-rename');

gulp.task('compile-html', function () {
    return gulp.src(argv.ejsfile || config.DEFAULT_EJSFILE)
        .pipe(ejs({}))
        .pipe(rename({extname: '.html'}))
        .pipe(gulp.dest(config.OUTPUT_DIR));
});

/* LESS CSS */
var less = require('gulp-less');
var path = require('path');

gulp.task('compile-css', function () {
    return gulp.src(argv.lessfile || config.DEFAULT_LESSFILE)
        .pipe(less({
            paths: [path.join(__dirname, 'static', 'spreadsheets')]
        }))
        .pipe(gulp.dest(config.OUTPUT_DIR));
});

gulp.task('compile', gulp.series('compile-html', 'compile-css'));

/* API Managment */
var request = require('request');
var fs = require('fs');

gulp.task('get', function (cb) {
    request.get({
        url: 'https://' + config.ODS_PORTAL_DOMAIN + config.ODS_PORTAL_SUFFIX + '/api/management/v2/pages/' + config.PAGE_ID,
        auth: {
            'user': config.ODS_USERNAME,
            'pass': config.ODS_PASSWORD
        }
    }, function (error, response, body) {
        if (error || !body) throw error
        fs.mkdir(path.join(__dirname, 'tmp'), { recursive: true }, (err) => {if(err) throw err;});
        fs.writeFileSync(path.join(__dirname, 'tmp', 'pages.json'), body);
        cb();
    })
});

var jeditor = require("gulp-json-editor");

gulp.task('edit', function (cb) {
    return gulp.src(path.join(__dirname, 'tmp', 'pages.json'))
        .pipe(jeditor(function (json) {
            json.slug = undefined;
            json.pushed_by_parent = undefined;
            json.has_subdomain_copies = undefined;
            json.created_at = undefined;
            json.last_modified = undefined;
            json.last_modified_user = undefined;
            json.author = undefined;
            Object.keys(json.content.main.text).forEach(function(key) {
                json.content.main.text[key] = fs.readFileSync(path.join(__dirname, config.OUTPUT_DIR, 'ods-app.html'), "utf8");
                json.content.custom_css.text[key] = fs.readFileSync(path.join(__dirname, config.OUTPUT_DIR, 'index.css'), "utf8");
            })
            return json;
        }))
        .pipe(gulp.dest(path.join(__dirname, 'tmp')))
});


var through2 = require('through2');

gulp.task('put', function (cb) {
    gulp.src(path.join(__dirname, 'tmp', 'pages.json'))
        .pipe(through2.obj(function(file, enc, cb) {
                // Prepare the payload
                var body = file.contents.toString();
                console.log(body);
                request.put({
                    url: 'https://' + config.ODS_PORTAL_DOMAIN + config.ODS_PORTAL_SUFFIX + '/api/management/v2/pages/' + config.PAGE_ID,
                    auth: {
                        'user': config.ODS_USERNAME,
                        'pass': config.ODS_PASSWORD
                    },
                    body: body,
                    headers: {
                        'Content-Type': 'application/json',
                        'Content-Length': body.length
                    }
                }, function (error, response, body) {
                    if (error) {
                        console.log(error);
                    }
                    if (response) {
                        console.log(response.body);
                    }
                    cb();
                })
            }
        ));
    cb();
});

gulp.task('update', gulp.series('get', 'compile', 'edit', 'put'));