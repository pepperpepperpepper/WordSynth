#!/usr/bin/env node

var ARGS = process.argv.slice(2);
var tokenize = require('../../lib/tokenizer.js');
var test = require('../../lib/presyllabizedWords.js');
//just accepts string
console.log(test(ARGS[0]));
