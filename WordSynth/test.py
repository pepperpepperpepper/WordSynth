#!/usr/bin/python2.7 

from Word import Word
from Word.String import WordString
from TTS.Marytts import TTSMarytts 
from TTS.OSXtts import TTSOSXtts 
from Word.Syllabizer.Learning import WordSyllabizerLearning 
from Word.Syllabizer.Marytts import WordSyllabizerMarytts 
from Word.Syllabizer.Trouvain import WordSyllabizerTrouvain 
from NoteMapper import NoteMapper; 
#from Syllabizer.Trouvain import SyllabizerTrouvain

t = WordString("imaged chimichanga this is a test string")

firstword = t.words[0]
tts = TTSMarytts() 
tts.phonetize(firstword) 

print firstword.phonetic_spelling().as_repr("phoneme_type") 
syllabizer = WordSyllabizerMarytts()
syllabizer.create_syllables(firstword)
#print firstword.syllables()
#print firstword.syllables().as_repr("symbol")

tts = TTSOSXtts()
tts.phonetize(firstword) 
syllabizer = WordSyllabizerLearning()
syllabizer.create_syllables(firstword)
print firstword.syllables()

#weird, didn't this work before? yeah ok nevermind, let's make getters and setter, this just doesn't workww
note_mapper = NoteMapper();


map(lambda x: note_mapper.note_map(x, [1,2,3])
  , firstword.syllables());
