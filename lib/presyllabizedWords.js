#!/usr/bin/env node
var test_string = process.argv[2] || 'test';  //'_s1AXrpIHkOW.';

//does this go in syllabizer as well? yes ok I'll try to finish this up
//so after this is all done, and I have words, how do I make something
//that maps words to notes,
//
//
//
//basically it needs to be such that if I have a midi file,
//the midi file gets transformed into pitches and durations
//that's not hard and there are external libs that I should use for that
//
//
//
//once I have that, and I have words, I just need to map the syllables from the
//words to the notes. Do I create a class call SyllableMapper? eah something like that
//
//ok and I can call it something like this
//
//SyllableMapper.from_string_and_midi(lyrics_string, midifile)
//and it can tie everything together internally? yep
//
//so those are sort of controller functions...should the controller
//be its own class? well yeah SyllableMapper I mean
//
//maybe it creates something that has syllable+pitch+durations
//in a class called SyllableMusic
//
//and to access it
//controller = SyllableMusicController()
//new_map = controller._from_string_and_midi(lyrics_string, midifile)
//something like this?
//well it can be same layout as phonetic spelling,
//controller = WordSyllableMusic(midi="file.mid")
//controller.process(word)
//print word.as_repr("midi_notes")
//
//something like this ok but how would the controller instance know
//what pitch and duration to map to the syllable? I get that it 
//takes word objects, or strings, and unpacks them into words, 
//
//
//just wondering how to tie together the two object types basically
//maybe like this seems good enough ok I'll do my best thanks a lot no problems


function checkWord(word){
  var presyllabized_words = require("./data/presyllabized_words.json");
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
