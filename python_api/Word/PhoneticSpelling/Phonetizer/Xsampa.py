#!/usr/bin/python2.7
import sys
import urllib2
import urllib
import re
import simplejson as json
from xml.dom import minidom
from Word.PhoneticSpelling import WordPhoneticSpelling
from Word.PhoneticSpelling.Character import WordPhoneticSpellingCharacter

class WordPhoneticSpellingPhonetizerXsampa(object):
  def __init__(self):
    self._url = "http://localhost:59125/process"
    self._char_data_file = open("data/marytts_xsampa_char_data.json", "r");
    self.char_data_map = json.loads(self._char_data_file.read());
    self._char_data_file.close();
  def tokenize(self, s):
    pass
  def _make_marytts_params(self, s):
    return {
      'INPUT_TYPE' : 'TEXT', 
      'OUTPUT_TYPE': 'ALLOPHONES',
      'INPUT_TEXT' : s,
      'LOCALE' : 'en_US'
    }
  def get_phonemes(self, s):
    characters = []
    def get_inner_phonemes(node):
      return map(lambda x: x.attributes['p'].value, node.getElementsByTagName("ph"))
    data = self.post_request(self._url, self._make_marytts_params(s))
    print data
    tree = minidom.parseString(data)
    syllables = tree.getElementsByTagName('syllable')
    for syllable in syllables:
      accent_added = False;
      phonemes = get_inner_phonemes(syllable)
      if "accent" in syllable.attributes.keys():
        print "YOOO"
      for i in phonemes:
        char_data = self.char_data_map[i]
        if char_data.get("phoneme_type", "") == 'V' and \
          "accent" in syllable.attributes.keys() \
          and not accent_added:
            characters.append(
              WordPhoneticSpellingCharacter(
                {"type": "ACCENT", "symbol": syllable.attributes['accent'].value}
              )
            )
            accent_added = True
        characters.append(WordPhoneticSpellingCharacter(char_data))
    return characters
  def process(self, word):
    word.phonetic_spelling_set(
      WordPhoneticSpelling(
        characters=self.get_phonemes(word.as_string)
      )
    )
    
#{{{ POST REQUEST
  @staticmethod
  def post_request(url, params):
      params = urllib.urlencode(params)
      sys.stderr.write(params)
      headers = {
          "Content-type": "application/x-www-form-urlencoded",
      }
      try:
          req = urllib2.Request(url, params, headers)
          response = urllib2.urlopen(req)
          return response.read()
      except Exception as e:
          sys.stderr.write(str(e))
          raise
#}}}
if __name__ == "__main__":
  test = "ok this is my test"
#  test = sys.argv[1] 
  p = WordPhoneticSpellingPhonetizerXsampa();
  print p.get_phonemes(test)
#tokenizer = ThisClass()
#characters = tokenizer.tokenize(word.as_string)
#word.characters_set(characters)

