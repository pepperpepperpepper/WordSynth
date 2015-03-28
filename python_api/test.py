#!/usr/bin/python2.7 
from Word import Word
from Word.String import WordString
from Word.PhoneticSpelling.OSXtts import WordPhoneticSpellingOSXtts
from Syllabizer.Trouvain import SyllabizerTrouvain

t = WordString("billyboy has a new toy")

firstword = t.words[0]
phonetic_strategy = WordPhoneticSpellingOSXtts()
phonetic_strategy.create(firstword)

print firstword.phonetic_spelling
print firstword.phonetic_vcstring

print t.chars
newlist = map(lambda x: x.as_string, t.words)
print newlist
