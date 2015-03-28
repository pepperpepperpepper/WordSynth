#!/usr/bin/python2.7 
import re
my $string = Syllables::String->new($string_example);
print Dumper $string->words; # Syllables::Word #so string is meant to be just a wrapper around Word? yes ok
class String():
#ok first, this is more or less correct, right? _make_words should create Word classes I see...hmm
  def __init__(self, s):
    self.chars = s
    self._sanitized = santize_characters(s)
    self._make_words()
  @staticmethod  
  def santize_characters(s):
    return re.sub(r"[^a-zA-Z0-9\s\-']", '', s)
  def _make_words(self):
    self.words = re.findall(r'\S+',self._sanitized)
