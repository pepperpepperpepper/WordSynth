#!/usr/bin/python2.7
from Word import Word
from Word.String import WordString
from TTS.Marytts import TTSMarytts 
from TTS.OSXtts import TTSOSXtts 
from Word.Syllabizer.Learning import WordSyllabizerLearning 
from Word.Syllabizer.Marytts import WordSyllabizerMarytts 
from Word.Syllabizer.Trouvain import WordSyllabizerTrouvain 
from Word.Syllable.NoteMapper import WordSyllableNoteMapper

if __name__ == "__main__":
  word = Word("hello");
  tts = TTSOSXtts()
  tts.phonetize(word)
  syllabizer = WordSyllabizerLearning()
  syllabizer.create_syllables(word);
  note_mapper = NoteMapper();
  syllables = map(lambda x: note_mapper.stream_map(x, [ 1, 2, 3 ]), word.syllables()) 
  for syllable in word.syllables():
    print syllable.as_repr("symbol") 
    for character in syllable.characters():
      print "--pitch: {}".format( character.pitch)
      print "--duration: {}".format(character.duration)
  
