#!/usr/bin/env node

var test_string = process.argv[2] || 'dildo';  

var syllables_data = require("./syllablesdb.json");
var createVCString = require ("./createVCString.js");
var tokenize = require('./tokenizer.js');


function determineSeparationPoints(test_string){
  var VC_string = createVCString(test_string);
  var learned_data = syllables_data[VC_string] || {};//add if exists
  var most_likely = { count: 0, positions: undefined  };
  learned_data.forEach(function(data){
    if (data['count'] > most_likely['count']){
      most_likely = data;
    }
  });
  return most_likely['positions'];
}


function separateSyllables(test_string){
  var tokens = tokenize(test_string);
  var separation_points = determineSeparationPoints(test_string);
    if (! separation_points){
    return [ tokens ];
  }
  var syllables = [];
  var syllable = [];
  var phoneme_count = 0; //starts at 1 for some reason. guess I messed this up
  tokens.forEach(function(token){
    syllable.push(token);
    if (token[1] == 'PHONEME'){
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
var syllables = separateSyllables(test_string);
console.log(syllables.length)
console.log(syllables[0]);
console.log(syllables[1]);
console.log(syllables[2]);
