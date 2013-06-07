var phantom = require('phantom'),
	async = require('async');

function Pandora (username, password) {
	var self = this;

	self.login = function (fn) {
		self.page.open("http://www.pandora.com/account/sign-in", function (status) {
			self.page.evaluate(evaluator, evalHandler);
		});

		function evaluator () {
			return document.title;
		}

		function evalHandler (result) {
			fn(null, result);
		}
	};
}

exports.fetchTracks = function (username, password, fn) {
	var pandora = new Pandora(username, password);
	phantom.create(function (ph) {
		ph.createPage(function (page) {
			pandora.page = page;
			// Series of actions to perform on the page
			async.waterfall([
				pandora.login
			], function (err, result) {
				ph.exit();
				fn(result);
			});
		});
	});
};