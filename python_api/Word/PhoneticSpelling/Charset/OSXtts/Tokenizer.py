import urllib2
import urllib
import re
import simplejson
class WordPhoneticSpellingCharsetOSXttsTokenizer(object):
  def __init__(self, s):
    self._urlbase = "http://devel.chimecrisis.com/phonemes"
    self._regexp = re.compile(r'("|\)|\.|,|\()?' + #PUNCTUATION DATA\
      r'(~|1|=|2|_|\+|\s)?' + #PROSODIC CONTROL\
      r'(%|@|AE|EY|AO|AX|IY|EH|IH|AY|IX|AA|UW|UH|UX|OW|AW|OY|b|C|d|D|f|g|h|J|k|l|m|n|N|p|r|s|S|t|T|v|w|y|z|Z)?') # PHONEMES
    self._consonant_vowel_map_data = "data/consonant_vowel_map_osxtts.json"
  def tokenize(self, s)
    consonant_vowel_map = json.loads(self._consonant_vowel_map_data) 
    phonemes = get_phonemes(s)  
    self._phonemes_string = None
    results = []
    matches = re.findall(self._phonemes_string)
    for match in matches:
      if match[0]: results.append({ "type": "PUNCTUATION_DATA", "symbol": match[0] } )
      if match[1]: results.append({ "type": "PROSODIC_CONTROL", "symbol": match[1] } )
      if match[2]: results.append({ "type": "PHONEMES", "symbol": match[2], "phoneme_type": consonant_vowel_map[match[2]] } )
    return results
  @staticmethod
  def get_phonemes(s):
    url = "{}/{}".format(self._urlbase, urllib.quote(s))
    return get_request(url)
  @staticmethod
  def get_request(url):
    return urllib2.urlopen(url).read()

#tokenizer = ThisClass()
#characters = tokenizer.tokenize(word.as_string)
#word.characters_set(characters)

