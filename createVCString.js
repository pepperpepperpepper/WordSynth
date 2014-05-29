#!/usr/bin/env node

var tokenize = require('./tokenizer.js');
var ARGS = process.argv.slice(2);
var word = ARGS[0];

function syllabize(string){
  var tokens = tokenize(string);
  var consonants_vowel_pattern = "";
//  console.log(tokens);
  tokens.forEach(function(token){
    if (token[1] == 'PHONEME'){
      consonants_vowel_pattern += token[2];
    }
  });
//  console.log(consonants_vowel_pattern);
  return consonants_vowel_pattern;

}
console.log(syllabize(word));

