#!/usr/bin/env node

var test_string = process.argv[2] || 'caramellonianish';  

var syllables_data = require("./syllablesdb.json");
var createVCString = require ("./createVCString.js");
var tokenize = require('./tokenizer.js');


function determineSeparationPoints(tokens){
  var VC_string = createVCString(tokens);
  VC_string = VC_string.replace(/[^VC]/g, ''); 
  var learned_data = syllables_data[VC_string] || undefined;//add if exists
  if (learned_data){
    return learned_data[0]['positions'];
  }else{
    return false;
  }
}


function separateSyllables(tokens){
  var separation_points = determineSeparationPoints(tokens);
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
var main = function(){
  var tokens = tokenize(test_string);
  var syllables = separateSyllables(tokens);
  console.log(printSyllableString(syllables));
}

if (require.main === module) {
    main();
}
module.exports = determineSeparationPoints;
