import urllib2
import simplejson as json
import sys
from Word.PhoneticSpelling import WordPhoneticSpelling
from Word.PhoneticSpelling.Character import WordPhoneticSpellingCharacter

#also I shouldn't have set the VCstring thing here, right? yes, it's just a representation, not a source data so 
#where do we make the as VCString function? it's already done here? no
class WordPhoneticSpellingCharsetOSXtts():
  def __init__(self):
    self._urlbase = "http://devel.chimecrisis.com/tokens"
  def process(self, word):
    data_raw = self._fetch_word_values()
    phonetic = WordPhoneticSpelling(**{ 
      'characters': map( 
        lambda d: WordPhoneticSpellingCharacter(d),
        data_raw
      )
    })
    word.phonetic_spelling_set(phonetic)
  def _make_url(self, word):
    return "{}/{}".format(self._urlbase, word.as_string)
  def _fetch_word_values(self, word):
    return json.loads(self.get_request(self._make_url(word)))[0]
  @staticmethod
  def get_request(url):
    return urllib2.urlopen(url).read()
