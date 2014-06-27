#!/usr/bin/env node
var test_string = process.argv[2] || 'test';  //'_s1AXrpIHkOW.';
var execSync = require('exec-sync'); 
test_string = execSync('phonemes \"'+test_string+'\"');
console.log(test_string);
