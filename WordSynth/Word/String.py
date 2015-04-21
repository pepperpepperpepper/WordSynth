import re
from Word import Word

class WordString(object):
  def __init__(self, s):
    self._chars = s
    self._sanitized = self.santize_characters(s)
    self._words = []
    self._make_words()
  @staticmethod  
  def santize_characters(s):
    return re.sub(r"[^a-zA-Z0-9\s\-']", '', s)
  def _make_words(self):
    splitted_strings = re.findall(r'\S+',self._sanitized)
    self._words = map(lambda x: Word(x) , splitted_strings)
  @property
  def words(self):
    return self._words; 
  @property
  def chars(self):
    return self._chars; 
