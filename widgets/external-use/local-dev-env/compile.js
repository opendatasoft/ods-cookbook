var args = process.argv.slice(2);

if (args.length <= 1) {
    process.stdout.write("Missing param.\nUsage: node compile.js ./views/ods-app.ejs output.html\n");
    process.exit(1);
}

ejs_file = args[0];
output_file = args[1];

const fs = require('fs');
const ejs = require('ejs');
const path = require('path');

/* EJS Compiler and path resolver */
ejs.compileFile = function(filePath, options) {
    let templatePath = filePath;
    if (options && options.root) templatePath = path.resolve(options.root, templatePath);
    const templateStr = ejs.fileLoader(templatePath, 'utf8');
    options = Object.assign({ filename: templatePath }, options);
    return ejs.compile(templateStr, options);
}

const templatePath = path.resolve(__dirname, ejs_file);
const template = ejs.compileFile(templatePath);

const data = new Uint8Array(Buffer.from(template()));

fs.writeFile(output_file, data, (err) => {
    if (err) throw err;
    process.stdout.write('HTML successfully compiled and generated!\n');
});