#!/usr/bin/env node

var ARGS = process.argv.slice(2);
var test = require('./main/syllabizeLearning_withaccent.js');
console.log(test(ARGS[0]));
