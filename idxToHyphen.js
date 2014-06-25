#!/usr/bin/env node
//var syllabizeLearning = require("./syllabizeLearning.js");
//var tokens = 
//[ { type: 'PROSODIC_CONTROL', symbol: '_' },
//  { type: 'PHONEME', symbol: 't', phoneme_type: 'C' },
//  { type: 'PROSODIC_CONTROL', symbol: '1' },
//  { type: 'PHONEME', symbol: 'EH', phoneme_type: 'V' },
//  { type: 'PHONEME', symbol: 's', phoneme_type: 'C' },
//  { type: 'PHONEME', symbol: 't', phoneme_type: 'C' },
//  { type: 'PROSODIC_CONTROL', symbol: '=' },
//  { type: 'PHONEME', symbol: 'IH', phoneme_type: 'V' },
//  { type: 'PHONEME', symbol: 'N', phoneme_type: 'C' },
//  { type: 'PUNCTUATION_DATA', symbol: '.' } ];
//
//var separation_points = syllabizeLearning("testing");

function separateSyllables(tokens, separation_points){
    if (! separation_points){
    return [ tokens ];
  }
  var syllables = [];
  var syllable = [];
  var phoneme_count = 0; 
  tokens.forEach(function(token){
    syllable.push(token);
    if (token['type'] == 'PHONEME'){
      phoneme_count++;
      if (phoneme_count == separation_points[0]){
        syllables.push(syllable);
        syllable = [];
        separation_points.shift();
      }
    }
  });
  syllables.push(syllable); 
  return syllables;
}

function printSyllableString(syllables){
  var to_print = "";
  for (var i = 0; i < syllables.length; i++){
    syllables[i].forEach(function(token){
      to_print += token['symbol'];
    });
    if (i < (syllables.length - 1)){
      to_print += " - ";
    }
  };
  return to_print;
}

function idxToHyphen(tokens, separation_points){
  
  var syllables = separateSyllables(tokens, separation_points)
  return printSyllableString(syllables)

}



module.exports = idxToHyphen;
