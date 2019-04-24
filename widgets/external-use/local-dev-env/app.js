var yargs = require('yargs');
var argv = yargs.argv;

let express = require('express');
let app = express();

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('index');
});

app.use(express.static('static'));

app.listen(argv.port, () => console.log('ExpressJS App listening on :' + argv.port + ' !'));