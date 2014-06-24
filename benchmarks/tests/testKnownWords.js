#!/usr/bin/env node

var ARGS = process.argv.slice(2);
var presyllabizedTest = require('./main/presyllabizedWords.js');
console.log(presyllabizedTest(ARGS[0]));
