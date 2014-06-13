#!/usr/bin/env node
var presyllabized_words = require("./presyllabized_words.json");
function checkWord(word){
  return presyllabized_words[word] || undefined;
}
module.exports = checkWord;
