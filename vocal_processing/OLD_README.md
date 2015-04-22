<pre>
INPUT DATA:
start with a file on rapidcomposer
   is anything fucked up about the file?
   yes
      return error
   is it multitrack midi?
   yes
      extract track data for the vocals from the rest of the tracks
   no
      extract track data for the vocals

iteratively process track data into something usable (using a midi library, either midifile.js, midijson, midicsv, really anything)
   convert each midi note into an actual note
   convert each midi clock duration into seconds
      create an object looking like this...{ type: "note", pitch : [midinote], duration: [time in miliseconds], freq_in_hz: [freq_in_hertz], time_in_clocks: [time_in_midiclocks] }
   convert each duration of silence into an object looking something like this
      create an object looking like this...{ type: "silence", duration: [time in miliseconds] }
   build the array of the entire composition and return an object that looks something like this
   vocal_music = { note_data: [note and silence array], total_time: [total time of vocal_music in miliseconds]}
   

start with a lyrics file:
   are the lyrics separated by both syllable AND word?
   no
      separate them
   are the lyrics divided into phrases? 
   no
      NOT YET IMPLEMENTED (maybe unnecessary)
      divide them up into phrases according to a reasonable syllable_phrase length 
      determine reasonable syllable_phrase length(function)
         note this function would require phrases being present in the original midi data, at which point they are not
         NOT YET IMPLEMENTED
      
   return list of objects that look something like this:
   { syll_part: [syll_part], word: [word_it_belongs_to], word_idx: [integer] }


PRE-PROCESSING:

start with a vocal_music object:
   is anything fucked up about the vocal music object?
   yes
      return error
   take into account vocal range...
   are the notes in the vocal music object in an acceptable range for voice we are going to use?
   no
      transpose notes for voice (external function)
      inputs: voice_range, notes
          transpose midi_notes appropriately, change freq_in_hz with a hashtable lookup

   case:
       there are the same number of notes as there are syllables
           return vocal_music object
       there are more notes than there are syllables
           while (there are more notes than there are syllables)
              create multi-note syllables
                  iterate through the notes...
                  first iteration: check 32nd notes
                  second iteration: check 16th notes
                  third iteration : check 8th notes
                  is the note a 32/16/8th note?
                  yes
                        is the note followed by a silence?
                        no
                            mark note object as a multinote_syllable note
           final_check...
           are there more notes than syllables?
           yes
               return error
      there are more syllables than notes
           similar function as above, looking for notes in reverse length

   iterate through vocal_music, adding a paramter to the object called syllable_data, containing
   the syllables

   return vocal_music


on to processing!
</pre>
