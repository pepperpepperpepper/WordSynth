#!/usr/bin/env node

var ARGS = process.argv.slice(2);
var tokenize = require('./main/tokenizer.js');
var test = require('./main/trouvain.js');
console.log(test(tokenize(ARGS[0])));
