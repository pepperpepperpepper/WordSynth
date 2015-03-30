import urllib2
import urllib
import re
import simplejson
from Word.PhoneticSpelling import WordPhoneticSpelling
from Word.PhoneticSpelling.Character import WordPhoneticSpellingCharacter
class WordPhoneticSpellingPhonetizerOSXtts(object):
  def __init__(self, s):
    self._urlbase = "http://devel.chimecrisis.com/phonemes"
    self._regexp = re.compile(r'("|\)|\.|,|\()?' + #PUNCTUATION DATA\
      r'(~|1|=|2|_|\+|\s)?' + #PROSODIC CONTROL\
      r'(%|@|AE|EY|AO|AX|IY|EH|IH|AY|IX|AA|UW|UH|UX|OW|AW|OY|b|C|d|D|f|g|h|J|k|l|m|n|N|p|r|s|S|t|T|v|w|y|z|Z)?') # PHONEMES
    self._consonant_vowel_map_data = "data/consonant_vowel_map_osxtts.json"
    self.consonant_vowel_map = json.loads(self._consonant_vowel_map_data) 

  def process(self, word):
    phonemes_string = get_phonemes_string(word.as_string)  
    characters = []
    matches = re.findall(phonemes_string)
    for match in matches:
      if match[0]: characters.append(WordPhoneticSpellingCharacter({ "type": "PUNCTUATION_DATA", "symbol": match[0] })) 
      if match[1]: characters.append(WordPhoneticSpellingCharacter({ "type": "PROSODIC_CONTROL", "symbol": match[1] } ))
      if match[2]: characters.append(WordPhoneticSpellingCharacter({ "type": "PHONEMES", "symbol": match[2], "phoneme_type": self.consonant_vowel_map[match[2]] } ))
    word.phonetic_spelling_set(WordPhoneticSpelling(characters=characters))

  @staticmethod
  def get_phonemes(s):
    url = "{}/{}".format(self._urlbase, urllib.quote(s))
    return get_request(url)

  @staticmethod
  def get_request(url):
    return urllib2.urlopen(url).read()
