#!/usr/bin/python2.7 

from Word import Word
from Word.String import WordString
from Word.PhoneticSpelling.Charset.OSXtts import WordPhoneticSpellingCharsetOSXtts 
from Word.Syllables.Syllabizer.Learning import WordSyllablesSyllabizerLearning 
from Word.Syllables.Syllabizer.Learningwithaccent import WordSyllablesSyllabizerLearningwithaccent 
 
#from Syllabizer.Trouvain import SyllabizerTrouvain

t = WordString("whatever this is a test string")

firstword = t.words[0]
phonetic = WordPhoneticSpellingCharsetOSXtts() 
phonetic.process(firstword) 


#print firstword.phonetic_spelling().as_repr("phoneme_type") 
#syllabizer = WordSyllablesSyllabizerLearning()
#syllabizer.create_syllables(firstword)
#print firstword.syllables().as_repr("symbol")
#print firstword
#print t.chars
#newlist = map(lambda x: x.as_string, t.words)
#print newlist
syllabizer = WordSyllablesSyllabizerLearningwithaccent()
syllabizer.create_syllables(firstword)

print firstword.syllables().as_repr("symbol")
