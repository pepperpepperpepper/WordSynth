#!/usr/bin/env node
//NOT YET IMPLEMENTED: multiple vocal tracks
var fs = require('fs');
var prettyjson = require('prettyjson');
var midiJson = require('./lib/midi-json.js');

//CONSTANTS
RAPID_COMPOSER_FILES = [
  './rapidcomposer_examples/rapid_composer_test2.mid',
  './rapidcomposer_examples/rapid_composer_test3.mid',
  './rapidcomposer_examples/rapid_demo1.mid',
];
EXAMPLE_FILE = RAPID_COMPOSER_FILES[2];
VOCAL_TRACK_LABELS = [
  "Voice",
  "Vocal",
  "vox"
].map(function(str){ return new RegExp(str, "i") });
NOTE_CONVERSION_TABLE = require('./lib/midi_note_to_frequency.json');


//CONVENIENCE FUNCTIONS -->
function error(error_string){
  process.stderr.write('ERROR: '+error_string);
  process.exit(1);
}
//-->

//UTILS-->
function calculateTimeLength(start_clocks, end_clocks, tempo, division){
  var secToMilisec = function (seconds){ return 1000* seconds };
  var midiTimeToSeconds = function (length_in_clocks, division, tempo){
    return length_in_clocks/division * (tempo/1000000);
  }
  return secToMilisec(midiTimeToSeconds((end_clocks - start_clocks), division, tempo));
}
function translateMidiNote(midi_note){
  return NOTE_CONVERSION_TABLE[midi_note];
}
function checkSourceIntegrity(midi_data){
  if (! midi_data[0].type.match(/Header/)) error("Incorrect header in midifile");
  return midi_data;
}
function evaluateSilence(current_note, previous_note, division, tempo){
  var start = previous_note != undefined ? previous_note.end_clocks : 0;
  var end = current_note.start_clocks;
  var length = calculateTimeLength( start, end, tempo, division);
  return length ? { type: "silence", length_milliseconds: length } : false;
}
//-->


//MAIN ACTION
function loadData(file_path){  
  var midi_data = midiJson(file_path);
  //is anything fucked up about the file?
  checkSourceIntegrity(midi_data);
  //is the file multitrack midi?
  var note_events = []; //what we'll be adding to
  var current_note = {};

  var multitrack = midi_data[0]["nTracks"] > 1 ? true : false;
  var division = midi_data[0]["division"]
  //main loop
  var vocal_track_no, tempo, previous_note, total_time;
  var total_notes = 0;
  for (i in midi_data) {
    var midi_event = midi_data[i];
    //we don't know which track is the vocal track yet, not until it shows up
    vocal_track_no = midi_event.type.match(/Title_t/) && 
        VOCAL_TRACK_LABELS.some(function(label){ return midi_event.value.match(label) }) ? midi_event.track_no : vocal_track_no;
    tempo = (midi_event.type.match(/Tempo/i)) ? midi_event.number : tempo;
    if ( vocal_track_no && midi_event.track_no == vocal_track_no){ //now we know what it is...time to iterate
      switch (midi_event.type){
        case 'Note_on_c':

          current_note.type = "note";
          current_note.start_clocks = midi_event.abs_time;
          current_note.midi_note = midi_event.note
          current_note.velocity = midi_event.vel//unnecessary, but why not
          //current_note.aftertouch = ...not sure how to get this to happen with rapidcomposer
          //current_note.channel = midi_event.channel //WTF is this for???
          total_notes++;
          var silence = evaluateSilence(current_note, previous_note, division, tempo);
          if (silence) note_events.push(silence);
          break;
        case 'Note_off_c':
          current_note.end_clocks = midi_event.abs_time 
          if (! tempo){ error("wasn't able to determine tempo from MIDI file") }
          current_note.length_milliseconds = calculateTimeLength(current_note.start_clocks, current_note.end_clocks, tempo, division);
          current_note.info = translateMidiNote(current_note.midi_note);
          note_events.push(current_note);
          previous_note = current_note;
          current_note = {} //reset
          break;
        case 'End_track':
          total_time = midi_event.abs_time 
          current_note.start_clocks = midi_event.abs_time;
          var silence = evaluateSilence(current_note, previous_note, division, tempo);
          if (silence) note_events.push(silence);
      }
    }
  };
  
  return { 
    tempo: tempo, 
    division: division,
    note_events: note_events, 
    total_time: calculateTimeLength(0, total_time, tempo, division),
    total_notes: total_notes
    }
}

function cache(file_path){
  var new_filename = "./cached/" + re.match(/^[^\.]+/)[0] + "_midi_cache.json";
  var midi_data = JSON.stringify(main(file_path));
  fs.appendFileSync(new_filename, midi_data, function(exit){
    process.stderr.write("created "+new_filename + "\n");
  })
}



function main(file_path){
  return loadData(file_path);
}
if (require.main === module) {
  var ARGS = process.argv.slice(2);
  var file_path = (ARGS.length)? ARGS[0] : EXAMPLE_FILE
  //FIXME add cache function here
//  console.log( prettyjson.render((main(file_path))));
  console.log(JSON.stringify(main(file_path)));
}
module.exports = main;
