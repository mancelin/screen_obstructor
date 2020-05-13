#!/usr/bin/env node

const { exec } = require('child_process');
const config = require('./config.json');

exec('xwininfo', (error, stdout, stderr) => {
  if (error) {
    console.error(`Error running 'xwininfo': ${error.message}`);
    return;
  }
  if (stderr) {
    console.log(`stderr: ${stderr}`);
    return;
  }
  const lines = stdout.split('\n');
  const windowName = lines
    .find(l => /Window id:/.test(l))
    .match(/"(.+)"/)[1];
  let X = parseInt(lines
    .find(l => /Absolute upper-left X:/.test(l))
    .match(/\d+/)[0]);
  let Y = parseInt(lines
    .find(l => /Absolute upper-left Y:/.test(l))
    .match(/\d+/)[0]);
  let W = parseInt(lines
    .find(l => /Width:/.test(l))
    .match(/\d+/)[0]);
  let H = parseInt(lines
    .find(l => /Height:/.test(l))
    .match(/\d+/)[0]);
  let cfg = null;
  for (let i in config) {
    if (windowName.includes(i)) {
      cfg = config[i];
      break;
    }
  }
  if (cfg !== null) {
    X += cfg.offset_x;
    W -= cfg.offset_x + cfg.offset_width;
    Y += cfg.offset_y;
    H -= cfg.offset_y + cfg.offset_height;
  }
  console.log(`${X} ${Y} ${W} ${H}`);
});
