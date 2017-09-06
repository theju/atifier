'use strict';

const child_proc = require('child_process');
const crypto = require('crypto');
const process = require('process');

const website = process.argv[2];
const selector = process.argv[3];

child_proc.exec('node fetcher.js "' + website + '" "' + selector + '"', function(error, stdout, stderr) {
    if (!error) {
        let output = stdout.replace(/\s+/gm, ' ').replace(/\n|\r\n/gm, '');
        if (output.trim().length > 0) {
	          let hash = crypto.createHash('sha1').update(output, 'utf8').digest('hex');
	          console.log(hash + '|||' + output);
        }
    }
});
