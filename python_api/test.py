#!/usr/bin/python2.7 
from Word import Word
from Word.String import WordString
from Word.PhoneticSpelling.OSXtts import WordPhoneticSpellingOSXtts 
 
#from Syllabizer.Trouvain import SyllabizerTrouvain

t = WordString("whatever this is a test string")

firstword = t.words[0]
phonetic = WordPhoneticSpellingCharsetOSXtts() 
phonetic.process(firstword) 


print firstword.phonetic_spelling.as_repr("phoneme_type") 



print t.chars
newlist = map(lambda x: x.as_string, t.words)
print newlist
