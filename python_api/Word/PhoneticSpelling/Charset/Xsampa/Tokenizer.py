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
  test = sys.argv[1]
  p = WordPhoneticSpellingCharsetOSXttsTokenizer();
  print p.get_phonemes(test)
#tokenizer = ThisClass()
#characters = tokenizer.tokenize(word.as_string)
#word.characters_set(characters)

