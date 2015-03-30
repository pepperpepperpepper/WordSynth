#!/usr/bin/python2.7
import sys
import urllib2
import urllib
import re
import simplejson
from xml.dom import minidom

class WordPhoneticSpellingCharsetOSXttsTokenizer(object):
  def __init__(self):
    self._url = "http://localhost:59125/process"
    self._consonant_vowel_map_data = "data/consonant_vowel_map_osxtts.json"
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
    def get_inner_phonemes(node):
      return map(lambda x: x.attributes['p'].value, node.getElementsByTagName("ph"))
    
    data = self.post_request(self._url, self._make_marytts_params(s))
    print data
    tree = minidom.parseString(data)
    syllables = tree.getElementsByTagName('syllable')
    for el in syllables:
      print get_inner_phonemes(el)
#      print map(lambda x: x, el.attributes.keys())
    return 


#ok so as I said before, I think my syllabizer works better than the one in marytts,
#but marytts has syllables already, basically what I'm doing is turning it into 
#VC strings, and comparing, I can do tests, compare to the accuracy of the other 
#tokenizer and decide if this strategy is good after finishing. There's two issues...
#with osxtts the accent marking is in a different place
#ok so the accent is the 1, put next to the vowel
#in maryttsxml, it just says that the syllable is accented, but doesn't tell you 
#where to put the accent
#I can parse that xml to make it look a little bit like the other data...for instance, add 
#a 1 before the vowel sound if the syllable has an accent, or at least add the accent character...
#does that seem like a reasonable compromise? I only need it for one type of syllabification
#chimecrisis.com/syllables  basically the one with the accent. Not sure whether it's even more accurate

#also not sure if it's useful to have different types at all, I guess I'm just sort of experimenting,
#but I want to make sure that I can wrap the code all together in an organized place, because
#there are some cool things I want to use these syllables for now...does that make sense?
#well a bit, so accent can be in character, or in whole syllable, depends on how much data you get. not sure if that's good idea
#to try to restore accent on character then you know that syllable has accent. I think that the other tts engine
#just dealt with accents by placing the marker in front of stressed vowels. All syllables have some sort of vowel sound...I can check easily

#~mAY _t1EHst _w1AXrdz.

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
  test = "my test words" 
  p = WordPhoneticSpellingCharsetOSXttsTokenizer();
  print p.get_phonemes(test)
#tokenizer = ThisClass()
#characters = tokenizer.tokenize(word.as_string)
#word.characters_set(characters)

