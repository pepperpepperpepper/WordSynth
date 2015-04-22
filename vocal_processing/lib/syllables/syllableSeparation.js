#!/usr/bin/env node

function Separation(){
  var that = this;
  this.separateSyllables = function(tokens, separation_points){
    if (! separation_points)  return [ tokens ];
    var separation_points = separation_points.slice(0); //copy
    var syllables = [];
    var syllable = { parts : [] };
    var phoneme_count = 0; 
    tokens.forEach(function(token){
      syllable.parts.push(token);
      if (token['type'] == 'PHONEME'){
        phoneme_count++;
        if (phoneme_count == separation_points[0]){
          syllables.push(syllable);
          syllable = { parts : [] };
          separation_points.shift();
        }
      }
    });
    syllables.push(syllable); 
    return syllables;
  };
  this.printSyllableString = function(syllables){
    var to_print = "";
    for (var i = 0; i < syllables.length; i++){
      syllables[i]["parts"].forEach(function(token){
        to_print += token['symbol'];
      });
      if (i < (syllables.length - 1)){
        to_print += " - ";
      }
    };
    return to_print;
  };

  this.idxToHyphen = function(tokens, separation_points){
    var syllables = that.separateSyllables(tokens, separation_points)
    return that.printSyllableString(syllables)

  };
}
module.exports = new Separation();
