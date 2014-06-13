#!/usr/bin/env node
var test_string = process.argv[2] || 'test';  //'_s1AXrpIHkOW.';
var execSync = require('exec-sync'); 
var consonant_vowel_map = require('./consonant_vowel_map.json');
var tokenize = require('./tokenizer.js');
var createVCString = require ("./createVCString.js");



function printSyllables(sylls){
  var result = [];
  sylls.forEach(function(syll){
    var s = "";
    syll.forEach(function(el){
      s += el['symbol'];
    })
    result.push(s);
  })
  return result.join(' - ');
}



var syllables = [];
var results = tokenize(test_string);

//remove the period
//if (results[results.length-1]['symbol'] == '.'){
//  results.pop(results.length-1);
//}
//for (var i = 0; i < results.length; i++){
//  var current_token = results[i];
//  var prev_token = ( i >= 1 )? results[i-1] : 0;
//  var prev_phoneme;
//  var next_phoneme;
//  var syll;
//  if ((i+1) < results.length){
//    var n = 1;
//    //find next phoneme
//    while (results[i+n]['type'] != 'PHONEME' && ((i+n) < results.length)){
//      n++;
//    }
//    next_phoneme = results[i+n];
//  }else{
//    next_phoneme = 0;
//  }
//
//
//  if (current_token['type'] == 'PHONEME'){
//    if (prev_phoneme && prev_phoneme['phoneme_type'] == 'V'){
//      if (current_token['phoneme_type'] == 'C'){
//        console.log("this is current_token", current_token);
//        if (next_phoneme && next_phoneme['phoneme_type'] != 'C'){
//          syllables.push(results.splice(0,i));  
//          i = 0;
//        }else if(next_phoneme && next_phoneme['phoneme_type'] == 'C'){
//          i++;
//          syllables.push(results.splice(0,i));  
//          i = 0;
//        
//        }
//      
//        
//      }
//      if (current_token['type'] == 'PHONEME' && current_token['phoneme_type'] == 'V'){
//        syllables.push(results.splice(0,i));  
//        i = 0;
//      }else if(!next_phoneme){// && current_token[2] == 'PHONEME' && current_token[2] == 'C'){
//        syllables.push(results); 
//      }
//    }else if (!next_phoneme){
//      syllables.push(results);
//    }
//  
//    prev_phoneme = results[i];
//  }
//
//}
//
//
console.log(printSyllables(syllables));
