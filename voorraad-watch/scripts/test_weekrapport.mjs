// Test: bouwt het weekrapport uit radar_js.json (uitvoer van test_radar_js.mjs) naar rapport_test.html.
import fs from 'fs';
const R = JSON.parse(fs.readFileSync('radar_js.json'));
const bron = { 'Uitverkoopradar': [R], 'Analyse: signaal per maat': [] };
globalThis.$ = n => ({ all: () => bron[n].map(json => ({ json })), first: () => ({ json: bron[n][0] }) });
const uit = new Function(fs.readFileSync(process.argv[2], 'utf8'))()[0].json;
fs.writeFileSync('rapport_test.html', uit.html); console.log(uit.onderwerp, uit.html.length, 'tekens');
