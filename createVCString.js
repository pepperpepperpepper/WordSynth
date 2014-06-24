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
    else if(token['type'] == 'PROSODIC_CONTROL' && token['symbol'] == '1'){
      consonants_vowel_pattern += token['symbol']

    }
  });
  return consonants_vowel_pattern;

}

var main = function(){
  console.log(createVCString(word));
}

if (require.main === module) {
    main();
}
module.exports = createVCString;

