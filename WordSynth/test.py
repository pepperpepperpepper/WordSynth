#!/usr/bin/python2.7 

from Word import Word
from Word.String import WordString
from TTS.Marytts import TTSMarytts 
from TTS.OSXtts import TTSOSXtts 
from Word.Syllables.Syllabizer.Learning import WordSyllablesSyllabizerLearning 
from Word.Syllables.Syllabizer.Marytts import WordSyllablesSyllabizerMarytts 
from Word.Syllables.Syllabizer.Trouvain import WordSyllablesSyllabizerTrouvain 
 
#from Syllabizer.Trouvain import SyllabizerTrouvain

t = WordString("imaged chimichanga this is a test string")

firstword = t.words[0]
tts = TTSMarytts() 
tts.phonetize(firstword) 

print firstword.phonetic_spelling().as_repr("phoneme_type") 
syllabizer = WordSyllablesSyllabizerMarytts()
syllabizer.create_syllables(firstword)
print firstword.syllables()
print firstword.syllables().as_repr("symbol")
tts = TTSOSXtts()
tts.phonetize(firstword) 
syllabizer = WordSyllablesSyllabizerLearning()
syllabizer.create_syllables(firstword)
print firstword.syllables()
print firstword.syllables().as_repr("symbol")
