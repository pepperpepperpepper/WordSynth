#!/usr/bin/env node

var ARGS = process.argv.slice(2);
var presyllabizedTest = require('./main/trouvain.js');
console.log(presyllabizedTest(ARGS[0]));
