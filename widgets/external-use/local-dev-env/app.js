let express = require('express');
let app = express();

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('index');
});

app.use(express.static('static'));

app.listen(9090, () => console.log('Listening on :9090 !'));