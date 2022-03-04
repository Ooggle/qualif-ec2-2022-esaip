/*
npm install --save puppeteer
npm install --save sqlite3
*/

// required packages
const puppeteer = require('puppeteer');
const sqlite3 = require('sqlite3')

// variables
const host = 'crossdungeon.ec2qualifications.esaip-cyber.com'; // change for local
const table = 'report';

// initializing db 
var db = new sqlite3.Database('/usr/app/src/sqlite.db');

// Bot
async function browser(url) {

	console.log(url);

	const browser = await puppeteer.launch({
		headless: true,
		args: ['--no-sandbox'],
		executablePath: '/usr/bin/google-chrome'
	});

	const page = await browser.newPage();
	await page.setDefaultNavigationTimeout(1000);
	// Specific session cookie
	await page.setCookie({
		'name' : 'flag',
		'value' : 'R2Lille{1NN3R_HTML_t0_XSS_3AzYYY}',
		'domain' : host,
		httpOnly: false
	});

	try { await page.goto(url); } catch {
		browser.close()
		return
	}
	// Click on the potion
	await page.click('#potion')
	// Wait for all animation
	await page.waitForTimeout(2000);

	await page.screenshot({path: 'page.png'});

    browser.close();
	return;
}

// Get db info to start bot if needed
async function main() {
	// fletching urls
	await db.all('SELECT * FROM ' + table, async (err, rows) => {
		let query = db.prepare('DELETE FROM ' + table + ' WHERE session = ?');
		await rows.forEach(async (row) => {
			// clearing database
			await query.run(row.session);
			// quering associate web pages
			await browser(row.url);
		});
	});
	// db.close();
};

// Start routine
setInterval(main, 60000);
