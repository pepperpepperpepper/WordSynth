#!/usr/bin/env node

var ARGS = process.argv.slice(2);
var tokenize = require('../../lib/tokenizer.js');
var test = require('../../lib/syllabizeLearning_withaccent.js');
console.log(test(tokenize(ARGS[0])));
