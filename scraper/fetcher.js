'use strict';

const process = require('process');
const puppeteer = require('puppeteer');
const debug = require('./debug');

puppeteer.launch({
    args: [debug.LOAD_IMAGES == true ? '--blink-settings=imagesEnabled=false': '']
}).then(async browser => {
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
