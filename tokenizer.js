#!/usr/bin/env node
var test_string = process.argv[2] || 'test';  //'_s1AXrpIHkOW.';
var execSync = require('exec-sync'); 
var consonant_vowel_map = require('./consonant_vowel_map.json');

function tokenize(test_string){
  test_string = execSync('phonemes '+test_string);
  var regexp = new RegExp(
    "(\"|\\)|\\.|,|\\(|\\s|)?" + // PUNCTUATION_DATA
    "(~|1|=|2|_|\\+|)?" + // PROSODIC CONTROL
    "(%|@|AE|EY|AO|AX|IY|EH|IH|AY|IX|AA|UW|UH|UX|OW|AW|OY|b|C|d|D|f|g|h|J|k|l|m|n|N|p|r|s|S|t|T|v|w|y|z|Z)?", // PHONEMES
    "g" //flag
    );

  var results = [];
  while((matches = regexp.exec(test_string)) && matches[0] !== ''){
    if (matches[1]){
      results.push({ 
        "type" : "PUNCTUATION_DATA",
        "symbol" : matches[1]
      });
    }
    if (matches[2]){
      results.push({ 
        "type" : "PROSODIC_CONTROL",
        "symbol" : matches[2]
      });
    }
    if (matches[3]){
      results.push({
          "type" : "PHONEME", 
          "symbol" : matches[3], 
          "phoneme_type" : consonant_vowel_map[matches[3]]
      });
    }
  }
  return results;
}
//console.log(tokenize(test_string));
//tokenize(test_string);
module.exports = tokenize;
