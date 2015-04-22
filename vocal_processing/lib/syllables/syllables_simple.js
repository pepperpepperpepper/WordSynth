#!/usr/bin/env node
//this script could definitely be improved, and made more sophisticated
var test_string = process.argv[2] || 'caramellonianish';  var tokenize = require('./tokenizer.js');
var dictionaryLookup = require('./presyllabizedWords.js');
var learningAlgo = require('./syllabizeLearning.js');
var linguisticRules = require('./trouvain.js');
var Separate = require('./syllableSeparation.js');
var prettyjson = require('prettyjson');



function main(word){
  var tokens = tokenize(word);
  var separation_points = dictionaryLookup(word) || learningAlgo(tokens) ||  
    linguisticRules(tokens) || false;
  var syllables = Separate.separateSyllables(tokens, separation_points);
  var hyphenated_spelling = Separate.printSyllableString(syllables);
  return {
    word : word,
    tokens : tokens,
    separation_points: separation_points,
    syllables : syllables,
    hyphenated_spelling : hyphenated_spelling
  }
}
if (require.main === module) {
    console.log(main(test_string));
}
module.exports = main;
