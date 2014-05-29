#!/usr/bin/env node

//var ARGS = process.argv.slice(2);
var execSync = require('exec-sync'); 
var consonant_vowel_map = require('./consonant_vowel_map.json');


function phonemize(test_string){

  test_string = execSync('phonemes '+test_string);

  var regexp = new RegExp(
    "(\"|\\)|\\.|,|\\(|)?" + // PUNCTUATION_DATA
    "(~|1|=|2|_|\\+|)?" + // PROSODIC CONTROL
    "(%|@|AE|EY|AO|AX|IY|EH|IH|AY|IX|AA|UW|UH|UX|OW|AW|OY|b|C|d|D|f|g|h|J|k|l|m|n|N|p|r|s|S|t|T|v|w|y|z|Z)?", // PHONEMES
    "g" //flag
    );

  var results = [];
  while((matches = regexp.exec(test_string)) && matches[0] !== ''){
    if (matches[1]){
      results.push([matches[1], "PUNCTUATION_DATA"]);
    }
    if (matches[2]){
      results.push([matches[2], "PROSODIC_CONTROL"]);
    }
    if (matches[3]){
      results.push([matches[3], "PHONEME", consonant_vowel_map[matches[3]]]);
    }
  }
  return results;
}
module.exports = phonemize;

//console.log(phonemize(ARGS[0]));
