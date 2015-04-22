#!/usr/bin/env node
// First, checks if it isn't implemented yet.
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}

var fs = require('fs');
var prettyjson = require('prettyjson');
var EXAMPLE_MIDI_FILE = 'rapidcomposer_examples/rapid_composer_test2.mid';
var EXAMPLE_LYRICS_FILE = 'lyrics_examples/1.lyrics';
var EXAMPLE_VOCAL_RANGE = 'ranges/Alex.range';
var prepareLyricsInput = require('./prepareLyricsInput.js'); 
var prepareMIDIInput = require('./prepareMIDIInput.js');
NOTE_CONVERSION_TABLE = require('./lib/midi_note_to_frequency.json');

var DEBUG = 1; //set debug to off to call regularly from the command line...for development only
//DEBUG
var MIDI_CACHE = './cached/midi_cache1.json';
var LYRICS_CACHE = './cached/lyrics_cache2.json';

function error(msg){
  process.stderr.write("ERROR: "+msg);
  process.exit(1);
}

function vocalRangeAdjust(note, range){
  if (typeof(range) == 'undefined'){
    range = loadRange(EXAMPLE_VOCAL_RANGE);
  }
  while (note.midi_note < range.bottom){
    note.midi_note = midiNoteTranspose(note.midi_note, 1)
  }
  while (note.midi_note > range.top){
    note.midi_note = midiNoteTranspose(note.midi_note, -1)
  }
  note.info = NOTE_CONVERSION_TABLE[note.midi_note];
  return note;
}

function loadRange(range_file){
  var range = fs.readFileSync(range_file).toString().split("\n");
  return { bottom: range[0], top: range[1] };
}

function midiNoteTranspose(midi_note_number, transposition_degree){
  return midi_note_number + (transposition_degree * 12);
}

function moreNotesThanSyllables(midi_data, lyrics_data){
  var msg = "Total Notes: {0}, Total Syllables{1}\nPlease adjust input data accordingly".format(
        midi_data.total_notes,
        lyrics_data.total_syllables
      );
  return error(msg);
}

function moreSyllablesThanNotes(midi_data, lyrics_data){
  var msg = "Total Notes: {0}, Total Syllables{1}\nPlease adjust input data accordingly".format(
        midi_data.total_notes,
        lyrics_data.total_syllables
      );
  return error(msg);
}

function preprocess(midi_data, lyrics_data, range_data){
  var vocal_music = { 
    note_events: [],
    total_notes: midi_data.total_notes, 
    total_time: midi_data.total_time,
    total_silence_events: undefined, //FIXME
  };
  if (lyrics_data.total_syllables > midi_data.total_notes){
    moreSyllablesThanNotes(midi_data, lyrics_data, range_data);
  }else if( lyrics_data.total_syllables < midi_data.total_notes){
    moreNotesThanSyllables(midi_data, lyrics_data, range_data);
  }else{
    var syllables_list = [];
    lyrics_data.lyrics_data.forEach(function(word){
      word.syllables.forEach(function(syllable){
        syllables_list.push(syllable.parts);
      })
    }); 
//    console.log(syllables_list)
//
    var note_for_processing = {};
    midi_data.note_events.forEach(function(note_event){
      if (note_event.type == 'note'){
        var note = vocalRangeAdjust(note_event);
        note_for_processing.note_name = note.info.note_name;
        note_for_processing.frequency_hz = note.info.frequency_hz
        note_for_processing.length_milliseconds = note.length_milliseconds
        note_for_processing.syllable = syllables_list.pop();
        vocal_music.note_events.push(note_for_processing);
        note_for_processing = {};
      }else{
        vocal_music.note_events.push(note_event);
      }
    });
  }
  return vocal_music;
};

//{{{ main function and command line stuff
function main(midi_file, lyrics_file, vocal_range_file){
  if (DEBUG){
    var midi_data = require(MIDI_CACHE); 
    var lyrics_data = require(LYRICS_CACHE); 
  }else{
    var midi_data = prepareMIDIInput(midi_file);
    var lyrics_data = prepareLyricsInput(lyrics_file);
  }
  var range_data = loadRange(vocal_range_file);
  return preprocess(midi_data, lyrics_data, range_data);
};

if (require.main === module) {
  var ARGS = process.argv.slice(2);
  var midi_file, lyrics_file, vocal_range_file;
  if (ARGS.length > 1){
    lyrics_file = ARGS[0]; 
    midi_file = ARGS[1];
  }else{
    midi_file = EXAMPLE_MIDI_FILE, 
    lyrics_file = EXAMPLE_LYRICS_FILE;
  }
  vocal_range_file = (ARGS.length > 2)? ARGS[2] : EXAMPLE_VOCAL_RANGE;
  console.log(main(midi_file, lyrics_file, vocal_range_file));
}
module.exports = main;
//}}}
