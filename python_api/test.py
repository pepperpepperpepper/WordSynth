#!/usr/bin/python2.7 

from Word import Word
from Word.String import WordString
from Word.PhoneticSpelling.Phonetizer.OSXtts import WordPhoneticSpellingPhonetizerOSXtts 
from Word.Syllables.Syllabizer.Learning import WordSyllablesSyllabizerLearning 
from Word.Syllables.Syllabizer.Learningwithaccent import WordSyllablesSyllabizerLearningwithaccent 
from Word.Syllables.Syllabizer.Trouvain import WordSyllablesSyllabizerTrouvain 
 
#from Syllabizer.Trouvain import SyllabizerTrouvain

t = WordString("whatever this is a test string")

firstword = t.words[0]
phonetic = WordPhoneticSpellingPhonetizerOSXtts() 
phonetic.process(firstword) 

print firstword.phonetic_spelling().as_repr("phoneme_type") 
syllabizer = WordSyllablesSyllabizerTrouvain()
syllabizer.create_syllables(firstword)
print firstword.syllables()
print firstword.syllables().as_repr("symbol")
#print firstword
#print t.chars
#newlist = map(lambda x: x.as_string, t.words)
#print newlist
