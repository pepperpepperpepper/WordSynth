#!/usr/bin/env node

var tokenize = require('./tokenizer.js');
var ARGS = process.argv.slice(2);
var word = ARGS[0];

function createVCString(string){
  var tokens = tokenize(string);
  var consonants_vowel_pattern = "";
  tokens.forEach(function(token){
    if (token['type'] == 'PHONEME'){
      consonants_vowel_pattern += token['phoneme_type'];
    }
    else if(token['type'] == 'PROSODIC_CONTROL' && ! /[~_\.]/.exec(token['symbol'])){
      consonants_vowel_pattern += token['symbol']

    }
  });
  return consonants_vowel_pattern;

}
VC_string = createVCString(word);

console.log(VC_string);
//console.log(createVCString(word));
module.exports = createVCString;

