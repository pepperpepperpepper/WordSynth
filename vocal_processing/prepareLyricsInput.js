#!/usr/bin/env node
EXAMPLE_FILE = false; // for debug put a file here;

var fs = require('fs');
var prettyjson = require('prettyjson')
var wordToSyllables = require('./lib/syllables/syllables_simple.js')

//UTIL-->
function read_file(file_path){
  return fs.readFileSync(file_path).toString()
}
//-->

function loadLyricsFile(file_path){
  var lyrics_file = read_file(file_path);
  var lyrics =  lyrics_file.split(/[\s\n\-]/)
    .filter(function(word){ if (word.match(/[a-zA-Z]/)) return word.replace(/[^A-Za-z]/ig, "") })
  var word_idx = 0;
  var syllables_idx = 0;
  var total_syllables = 0;
  var lyrics_data = lyrics.map(function(word) { 
    var syll_data = wordToSyllables(word);
    for (i in syll_data.syllables){
      syll_data.syllables[i]["syllables_idx"] = syllables_idx;
      syllables_idx++;
      total_syllables++;
    };
    syll_data.parent_word = word;
    syll_data.word_idx = word_idx;
    word_idx++;
    return syll_data;
  });
  return { 
    lyrics : lyrics_file,
    lyrics_data : lyrics_data,
    total_syllables: total_syllables
  }
}


function cache(file_path){
  var new_filename = "./cached/" + re.match(/^[^\.]+/)[0] + "_lyrics_cache.json";
  var lyrics_data = JSON.stringify(main(file_path));
  fs.appendFileSync(new_filename, lyrics_data, function(exit){
    process.stderr.write("created "+new_filename + "\n");
  })
}

function main(file_path){
  return loadLyricsFile(file_path);
}
if (require.main === module) {
  var ARGS = process.argv.slice(2);
  var file_path = (ARGS.length)? ARGS[0] : EXAMPLE_FILE;
  if (! file_path){
    console.log("ERROR: supply a file as an argument");
    process.exit(1);
  }
  //FIXME add cache function here
//  console.log( prettyjson.render((main(file_path))));
  console.log(JSON.stringify(main(file_path)));
}
module.exports = main
