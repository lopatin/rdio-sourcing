var express = require('express'),
	app = express(),
	pandora = require('./pandora');

app.use(express.static(__dirname+'/public'));

app.listen(8080);

