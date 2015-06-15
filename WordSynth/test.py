#!/usr/bin/python2.7
from Word import Word
from Word.String import WordString
from TTS.Marytts import TTSMarytts 
from TTS.OSXtts import TTSOSXtts 
from Word.Syllabizer.Learning import WordSyllabizerLearning 
from Word.Syllabizer.Marytts import WordSyllabizerMarytts 
from Word.Syllabizer.Trouvain import WordSyllabizerTrouvain 
from Note import Note
from Note.SyllableMapper import NoteSyllableMapper

if __name__ == "__main__":
  word = Word("hello");
  tts = TTSOSXtts()
  tts.phonetize(word)
  syllabizer = WordSyllabizerLearning()
  syllabizer.create_syllables(word);
  notes = []
  for i in [ 20, 17, 24 ]: 
    notes.append(Note.from_music(i, .25, 60));
  
  nm = NoteSyllableMapper();
  
  syllable = word.syllables()[0]
  nm.map_notes_to_syllable(syllable, notes)


  print syllable.characters()
  print notes


#  note_mapper = NoteMapper();
#  syllables = map(lambda x: note_mapper.stream_map(x, [ 1, 2, 3 ]), word.syllables()) 
#  for syllable in word.syllables():
#    print syllable.as_repr("symbol") 
#    for character in syllable.characters():
#      print "--pitch: {}".format( character.pitch)
#      print "--duration: {}".format(character.duration)
  
