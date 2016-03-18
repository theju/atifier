var child_proc = require("child_process");
var crypto = require("crypto");
var process = require("process");

var website = process.argv[2];
var selector = process.argv[3];


child_proc.exec("phantomjs fetcher.js " + website + " \"" + selector + "\"", function(error, stdout, stderr) {
    if (error) {
	return null;
    }

    var output = stdout.replace(/\s+/gm, ' ').replace(/\n|\r\n/gm, '');
    var hash = crypto.createHash('sha1').update(output, 'utf8').digest('hex');
    console.log(hash + "|||" + output);
});
