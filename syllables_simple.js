#!/usr/bin/env node
//this script could definitely be improved, and made more sophisticated
var dictionaryLookup = require('presyllabizedWords.js');
var learningAlgo = require('syllabizeLearning.js');
var linguisticRules = require('trouvain.js');


function main(word){
  return dictionaryLookup(word) || learningAlgo(word) ||
    linguisticRules(word) || false;
}
main();
module.exports = main;
