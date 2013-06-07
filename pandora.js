var phantom = require('phantom'),
	async = require('async');

function Pandora (username, password) {
	var browser = 
	function login () {

	}
}

phantom.create(function (ph) {
	ph.createPage(function (page) {
		page.open("http://www.google.com", function (status) {
			console.log("Opened google?", status);
			page.evaluate(function () { return document.title; }, function (result) {
				console.log("Page title is " + result);
				ph.exit();
			});
		});
	});
});

exports.fetchTracks = function (username, password) {
	var pandora = new Pandora();
	pandora.login(username, password);
};