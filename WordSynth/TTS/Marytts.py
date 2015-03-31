#!/usr/bin/python2.7
import sys
import urllib2
import urllib
import re
import simplejson as json
from xml.dom import minidom
from Word.PhoneticSpelling import WordPhoneticSpelling
from Word.PhoneticSpelling.Character import WordPhoneticSpellingCharacter

class TTSMarytts(object):
  def __init__(self):
    self._url = "http://localhost:59125/process"
    self.char_data_load("data/marytts_xsampa_char_data.json")
  def char_data_load(self, filename):
    char_data_file = open(filename, "r");
    self._char_data = json.loads(char_data_file.read());
    char_data_file.close();
  @property
  def char_data(self):
    return self._char_data
  

  def _make_marytts_params(self, s):
    return {
      'INPUT_TYPE' : 'TEXT', 
      'OUTPUT_TYPE': 'ALLOPHONES',
      'INPUT_TEXT' : s,
      'LOCALE' : 'en_US'
    }
  def syllabize(self, word):
    #new request to mary here, retrieving syllables to syllabize word...
    #something like that? yes ok so does the syllabizer class Marytts have to raise an error if the phonemes 
    #are not from mary originally? or not yet, because maybe I can make a translater at some point? yeah for now an error, later can be fixed.
    #so how 
  
  def get_phonemes(self, s):
    characters = []
    def get_inner_phonemes(node):
      return map(lambda x: x.attributes['p'].value, node.getElementsByTagName("ph"))
    data = self.post_request(self._url, self._make_marytts_params(s))
#so the good news is that we solved that problem, and I can fix this up and make it work better
#what about keeping the syllables made originally by mary? well you don't need to keep them, there will be just 
#method in this class "syllabize" which can get you syllables for any word. I don't mean keep them like
#in persistant storage, I just meant here I am taking the phonemes out of the syllables to use with 
#the other syllabizers. that's cool, but I sort of feel like I should also somehow use mary's own syllabizer as an option
# guess one idea would be, to have a syllabizer called Marytts and that would just query mary again? right, it will call 
#tts.syllabize() where is this tts.syllabize method? in this class ok but it's not in the other tts class, right? right



# SyllabizeLoadringwithacent - rewrite to use syllable.has_accent (if possible)
# OSXtts - tts.word_as_string -  return _t1EH ..., tts.word_restore_accents() - check syllable.has_accent, if yes - restore "1" as character 
# MaryTTS - tts.word_as_string, syllable.has_accent - set flag that syllable has accent
# MaryTTS - syllabize() function, phonetize() - call syllablze() and map { $_->phonemes } to return only phonemes.
# something like this.
# ok should we look at Syllabizelearningwithaccent ? alright

 
    tree = minidom.parseString(data)
    syllables = tree.getElementsByTagName('syllable')
    for syllable in syllables:
      accent_added = False;
      phonemes = get_inner_phonemes(syllable)
      for i in phonemes:
        char_data_curr = self.char_data[i]
        if char_data_curr.get("phoneme_type", "") == 'V' and \
          "accent" in syllable.attributes.keys() \
          and not accent_added:
            characters.append(
              WordPhoneticSpellingCharacter(
                {"type": "ACCENT", "symbol": syllable.attributes['accent'].value}
              )
            )
            accent_added = True
        characters.append(WordPhoneticSpellingCharacter(char_data_curr))
    return characters
  def phonetize(self, word):
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

