#!/usr/bin/env node

var ARGS = process.argv.slice(2);
var tokenize = require('./main/tokenizer.js');
var test = require('./main/presyllabizedWords.js');
//just accepts string
console.log(test(ARGS[0]));
