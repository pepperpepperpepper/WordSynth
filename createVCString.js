#!/usr/bin/env node

var tokenize = require('./tokenizer.js');
var ARGS = process.argv.slice(2);
var word = ARGS[0];

function syllabize(string){
  var tokens = tokenize(string);
  var consonants_vowel_pattern = "";
  tokens.forEach(function(token){
    if (token['type'] == 'PHONEME'){
      consonants_vowel_pattern += token['phoneme_type'];
    }
  });
  return consonants_vowel_pattern;

}
module.exports = syllabize;

