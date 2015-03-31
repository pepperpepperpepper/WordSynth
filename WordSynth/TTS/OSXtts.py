import urllib2
import urllib
import re
import simplejson as json
from Word.PhoneticSpelling import WordPhoneticSpelling
from Word.PhoneticSpelling.Character import WordPhoneticSpellingCharacter
class TTSOSXtts(object):
  def __init__(self):
    self._urlbase = "http://devel.chimecrisis.com/phonemes"
    #prosodic control, phoneme and PUNCTUATION_DATA are categories that come directly from the osx tts software
    #manual, I maybe made up punctuation data as a word to cover for other characters, probably should have it just
    #say "other" I don't really remember, but 1 is definitely a prosodic control symbol that just happens to 
    #indicate an accent on a vowel (I think that 1 stands for primary stress or something)
    self._regexp = re.compile(r'("|\)|\.|,|\()?' + #PUNCTUATION DATA\
      r'(1)?' + #PROSODIC CONTROL (ACCENT)\
      r'(~|2|=|_|\+|\s)?' + #PROSODIC CONTROL\
      r'(%|@|AE|EY|AO|AX|IY|EH|IH|AY|IX|AA|UW|UH|UX|OW|AW|OY|b|C|d|D|f|g|h|J|k|l|m|n|N|p|r|s|S|t|T|v|w|y|z|Z)?') # PHONEMES
    self._consonant_vowel_map_data_file = open("data/consonant_vowel_map_osxtts.json", "r")
    self.consonant_vowel_map = json.loads(self._consonant_vowel_map_data_file.read()) 
    self._consonant_vowel_map_data_file.close() 

  def phonetize(self, word):
    phonemes_string = self.get_phonemes(word.as_string)  
    characters = []
    matches = re.findall(self._regexp, phonemes_string)
    for match in matches:
      if match[0]: characters.append(WordPhoneticSpellingCharacter({ "type": "ACCENT", "symbol": match[0], "tts": "OSXtts" })) #like this? yep ok
      if match[1]: characters.append(WordPhoneticSpellingCharacter({ "type": "PUNCTUATION_DATA", "symbol": match[1] })) 
      if match[2]: characters.append(WordPhoneticSpellingCharacter({ "type": "PROSODIC_CONTROL", "symbol": match[2] } ))
      if match[3]: characters.append(WordPhoneticSpellingCharacter({ "type": "PHONEME", "symbol": match[3], "phoneme_type": self.consonant_vowel_map[match[3]] } ))
    word.phonetic_spelling_set(WordPhoneticSpelling(characters=characters))

  def get_phonemes(self, s):
    url = "{}/{}".format(self._urlbase, urllib.quote(s))
    return self.get_request(url)

  @staticmethod
  def get_request(url):
    return urllib2.urlopen(url).read()
