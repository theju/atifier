var page = require("webpage").create();
var system = require("system");

var debug = require("./debug");

var url = system.args[1];
var selector = system.args[2];

page.settings.userAgent = debug.USER_AGENT
page.settings.loadImages = debug.LOAD_IMAGES;
page.viewportSize = debug.VIEWPORT_SIZE;

page.onLoadFinished = function(status) {
    if (status === "success") {
	var output = page.evaluateJavaScript("function() { return document.querySelector('" + selector + "'); }");
	console.log(output.innerHTML);
    }
    phantom.exit();
}

page.onError = function(err) {
}

page.open(url)
