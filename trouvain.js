#!/usr/bin/env node
var tokenize = require('./tokenizer.js');
var test_string = process.argv[2] || 'example';  //'_s1AXrpIHkOW.';

function applyRules(test_string, debug){
  debug = typeof debug !== 'undefined' ? debug : 0;
  var tokens = tokenize(test_string); 
  function Token(token){
    var that = this;
    Object.keys(token).map(function(key){ that[key] = token[key] });
  }
  for (i in tokens){
    tokens[i].cursor = 0; 
    tokens[i].prev_tokens = []; //0 //false
    tokens[i].next_tokens = []; //0 //false
    tokens[i].prev_phonemes = []; //0 //false
    tokens[i].next_phonemes = []; //0 //false
    tokens[i].syllable_break = 0;
    tokens[i] = new Token(tokens[i]);
  } 
  Token.prototype.set_prev_tokens = function(){ 
    this.prev_tokens = tokens.slice(0, this.cursor).reverse();
    };
  Token.prototype.set_next_tokens = function(){
    this.next_tokens = tokens.slice(this.cursor, tokens.length);
    };
  Token.prototype.set_prev_phonemes = function(){ 
    this.prev_phonemes = 
      this.prev_tokens.filter( function(t){  if (t.type == "PHONEME"){return t}});
    };
  Token.prototype.set_next_phonemes = function(){ 
    this.next_phonemes = 
      this.next_tokens.filter( function(t){  if (t.type == "PHONEME"){return t}});
    };
  Token.prototype.prev = function(){ 
    if(this.cursor > 0){
      this.cursor--; 
      return tokens[this.cursor]; 
    }else{
      return 0; //false
    } 
  }
  Token.prototype.next = function(){ 
    if(this.cursor < tokens.length){
      this.cursor++; 
      return tokens[this.cursor]; 
    }else{
      return 0; //false
    } 
  }
  Token.prototype.reset = function(){
      this.set_next_tokens();
      this.set_prev_tokens();
      this.set_next_phonemes();
      this.set_prev_phonemes();
  }
  Token.prototype.print = function(){ //for debugging only
    var that = this;
    return {
      symbol : that.symbol,
      syllable_break : that.syllable_break,
      prev_tokens_length : that.prev_tokens.length || 0,
      next_tokens_length : that.next_tokens.length || 0,
      prev_phonemes_length : that.prev_phonemes.length || 0,
      next_phonemes_length : that.next_phonemes.length || 0
    }
  }

  //tokens[0].set_next_tokens();
  //tokens[0].set_next_phonemes();
  //console.log(tokens[0].print());
  //RULE 1  //can't use this for this tts
//  for(i in tokens){
//    if (tokens[i].symbol == " "){
//      tokens[i].syllable_break++;
//    }
//  }
  //RULE 2
  for (var i = 0; i < tokens.length; i++){
    if(((i+1) < tokens.length) && tokens[i].symbol == "1" && tokens[i+1].phoneme_type == "V"){
      tokens[i].cursor = i;
      tokens[i].reset();
      var p = 1
      while (p < tokens[i].next_phonemes.length && tokens[i].next_phonemes[p].phoneme_type == 'C' ){ // if this gives you grief, you need to change the initialization (no 0)
        p++;
      }
      if (p > 2 && tokens[i].next_phonemes[p]){
        while (tokens[i].phoneme_type != 'C'){
          i++;
        }
        if(debug){
          console.log("Using rule 2");
          console.log("on this : ");
          console.log(tokens[i].symbol)
        }
        tokens[i].syllable_break++;
      }
  //    else if (tokens[i].prev_phonemes.length > 1){
  //      p = 1;//array is reversed...looking backwards
  //      while (tokens[i].prev_phonemes[p].phoneme_type == 'C'){
  //        p++;
  //      }
  //      if (p > 2){
  //        var back = i;
  //        //this is probably wrong
  //        while (back && tokens[back].phoneme_type == 'C'){
  //          back--;
  //        }
  //        tokens[back+1].syllable_break++;
  //      }
  //    }
    }
  }

  //RULE 3
  //if this doesn't work, try altering RULE 4
  var first_vowel = 0;
  var consonant_middle = 0;
  var second_vowel = 0;
  var first_vowel_position = 0;
  var consonant_middle_position = 0;
  for (var i = 0; i < tokens.length; i++){
    if (tokens[i].phoneme_type == 'V'){
      if (! first_vowel){
        first_vowel = 1;
        first_vowel_position = i
      }
    
      if (first_vowel && consonant_middle){

        second_vowel = 1;
        if (debug){
          console.log("Using rule 3");
          console.log("on this : ");
          console.log(tokens[first_vowel_position].symbol)
          console.log(first_vowel_position);
        }
        tokens[first_vowel_position].cursor = first_vowel_position;
        tokens[first_vowel_position].reset();
        if (! tokens[first_vowel_position].prev_phonemes.length){
          tokens[consonant_middle_position].syllable_break = 1;
        }else{
          tokens[first_vowel_position].syllable_break = 1;
        }
        first_vowel = 1;
        first_vowel_position = i;
        consonant_middle = 0;

      }

//_IHgz1AEmpAXl.
//_IHg - z1AEm - pAXl.
    }
    if (tokens[i].phoneme_type == 'C'){
      if (first_vowel){
        if (tokens[i].syllable_break){
          first_vowel = 0;
          consonant_middle = 0;
        }else{
          consonant_middle = 1;
          if (! consonant_middle_position){
            consonant_middle_position = i;
          }
        }
      }
    }
  } 

  //RULE 4 // Doesn't seem to be working
//  for (var i = 0; i < tokens.length; i++){
//    if (tokens[i].syllable_break && tokens[i].phoneme_type == 'V'){
//      if (tokens[i+1].symbol == 'n'){
//        tokens[i].syllable_break = 0;
//        tokens[i+1].syllable_break = 1;
//        if (debug){
//          console.log("Using rule 4");
//          console.log("on this : ");
//          console.log(tokens[i+1].symbol)
//        }
//      }
//    }
//  }
  return tokens;
}


function createPoints(tokens){
  var points = [];
  var position = 1;
  for (var i = 0; i < tokens.length; i++){
     
//    console.log(tokens[i]);
    if (tokens[i].syllable_break){
//      console.log(tokens[i].symbol);
      points.push(position);
    }
    if (tokens[i].type == 'PHONEME' ){//|| (tokens[i]['type'] == 'PROSODIC_CONTROL' && tokens[i]['symbol'] == '1' )){
      position++;
    }
  }
  return points;
}

function getSyllablePoints(test_string){
  var tokens = applyRules(test_string);
  return createPoints(tokens);
}


var main = function(){
  tokens = applyRules(test_string, 1); //with debug
  for (i in tokens){
    if (tokens[i].syllable_break == 1 && tokens[i].symbol != " "){
      console.log(tokens[i].print()); 
    }
  }
  createPoints(tokens);
}

if (require.main === module) {
    main();
}
module.exports = getSyllablePoints;


//
//for(i in tokens){
//  if tokens[i].symbol = "N" && (tokens[i].syllable_break > tokens[i-1].syllable_break){
//    tokens[i].syllable_break--; 
//  }
//}
//
//if(syllable.tokens.last.symbol == "N"){
//  syllable.previous().push( syllable.pop() );
//}
//
//
//
