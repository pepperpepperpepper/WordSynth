#!/usr/bin/env node
var test_string = process.argv[2] || 'test';  //'_s1AXrpIHkOW.';

function checkWord(word){
  var presyllabized_words = require("./presyllabized_words.json");
  word = word.toLowerCase();
  var my_result = presyllabized_words[word];
  return presyllabized_words[word] || false;
}

var main = function(){
  console.log(checkWord(test_string));
}

if (require.main === module) {
    main();
}

module.exports = checkWord;
