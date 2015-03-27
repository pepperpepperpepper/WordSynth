#!/usr/bin/python2.7
import re
import urllib
import urllib2
class Word():
  def __init__(self, s):
    self.characters = s
    self._sanitized_characters = self.santize_characters(s)
    self._phonemes = self._fetch_phonemes(); 

  @staticmethod  
  def santize_characters(s):
    return re.sub(r"[^a-zA-Z0-9\s\-']", '', s)
  
  def _fetch_phonemes(self):
    string = urllib.quote(self._sanitized_characters, '')
    url = "http://devel.chimecrisis.com/phonemes/{}".format(string)
    response = urllib2.urlopen(url).read()
    return re.sub(r"\n", '', response);

  
def tokenizerOSX(s):


