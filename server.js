var express = require('express'),
	app = express(),
	pandora = require('./pandora'),
	config = require('./privateconfig');

app.use(express.static(__dirname+'/public'));

app.listen(8080);

pandora.fetchTracks(config.pandora.username, config.pandora.password, function (result) {
	console.log(result);
});
