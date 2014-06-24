#!/usr/bin/env node
var presyllabized_words = require("./presyllabized_words.json");
var test_string = process.argv[2] || 'test';  //'_s1AXrpIHkOW.';
function checkWord(word){
  return presyllabized_words[word] || false;
}

var main = function(){
  console.log(checkWord(test_string));
}

if (require.main === module) {
    main();
}

module.exports = checkWord;
