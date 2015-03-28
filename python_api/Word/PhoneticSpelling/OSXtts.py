import urllib2
import simplejson as json
import sys
class WordPhoneticSpellingOSXtts():
  def __init__(self):
    self._urlbase = "http://devel.chimecrisis.com/tokens"
    self.word = None
  def create(self, word):
    self.word = word
    word.phonetic_tokens = self._fetch_word_values()
    word.phonetic_spelling = self._tokens_to_spelling()
    word.phonetic_vcstring = self._tokens_to_vcstring() 
  def _make_url(self):
    return "{}/{}".format(self._urlbase, self.word.as_string)
  def _fetch_word_values(self):
    return json.loads(self.get_request(self._make_url()))[0]
  def _tokens_to_spelling(self):
    return "".join(map(lambda x: x['symbol'], self.word.phonetic_tokens))
  def _tokens_to_vcstring(self):
    return "".join(
      map(lambda x: x['phoneme_type'],
        filter(lambda x: x['type'] == 'PHONEME', self.word.phonetic_tokens)
      )
    )
  @staticmethod
  def get_request(url):
    return urllib2.urlopen(url).read()
