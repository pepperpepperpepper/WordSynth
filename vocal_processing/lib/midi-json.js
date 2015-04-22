#!/usr/bin/env node
var fs = require('fs');
var execSync = require('exec-sync');

function main(file_uri){
  var cmd = './bin/midi-json '+file_uri;
  return JSON.parse(execSync(cmd));
}
module.exports = main;
