#!/usr/bin/env node

var test_string = process.argv[2] || 'dildo';  

var syllables_data = require("./syllablesdb.json");
var createVCString = require ("./createVCString.js");
var tokenize = require('./tokenizer.js');


function determineSeparationPoints(test_string){
  var VC_string = createVCString(test_string);
  VC_string = VC_string.replace(/[^VC]/g, ''); 
  var learned_data = syllables_data[VC_string] || {};//add if exists
  return learned_data[0]['positions'];
//  var most_likely = { count: 0, positions: undefined  };
//  learned_data.forEach(function(data){
//    if (data['count'] > most_likely['count']){
//      most_likely = data;
//    }
//  });
//  return most_likely['positions'];
}


function separateSyllables(test_string){
  var tokens = tokenize(test_string);
  var separation_points = determineSeparationPoints(test_string);
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
//console.log(tokenize(test_string));
var syllables = separateSyllables(test_string);
console.log(printSyllableString(syllables));
//console.log(syllables.length)
//console.log(syllables[0]);
//console.log(syllables[1]);
