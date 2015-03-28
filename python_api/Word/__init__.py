#!/usr/bin/python2.7
class Word(object):
  def __init__(self, s):
    self.as_string = s
    self.phonetic_tokens = None
    self.phonetic_spelling = None
    self.phonetic_vcstring = None
    self.syllables = None
#    self._string = s
#    self._phonetic_tokens = None
#    self._phonetic_spelling = None
#  @property
#  def as_string(self):
#    return self._string

#  @property
#  def phonetic_tokens(self):
#    return self._phonetic_tokens
#  @phonetic_tokens.setter
#  def phonetic_tokens(self, t):
#    self._phonetic_tokens = t
#
#  @property
#  def phonetic_spelling(self):
#    return self._phonetic_spelling
#  @phonetic_spelling.setter
#  def phonetic_spelling(self, t):
#    self._phonetic_spelling = t
