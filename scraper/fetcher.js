'use strict';

const process = require('process');
const puppeteer = require('puppeteer');
const debug = require('./debug');

let opts = {
    args: []
};

if (debug.LOAD_IMAGES == true) {
    opts.args.push('--blink-settings=imagesEnabled=false');
}

puppeteer.launch(opts).then(async browser => {
    let url = process.argv[2];
    let selector = process.argv[3];

    let page = await browser.newPage();
    page.setUserAgent(debug.USER_AGENT);
    await page.setViewport({
        width: debug.VIEWPORT_SIZE.width,
        height: debug.VIEWPORT_SIZE.height
    });
    await page.goto(url, {waitUntil: 'load'});
    let output = await page.$eval(selector, function(ss) {
        return ss ? (ss.innerHTML || '').trim() : '';
    });
    console.log(output);
    await page.close();
    await browser.close();
});
