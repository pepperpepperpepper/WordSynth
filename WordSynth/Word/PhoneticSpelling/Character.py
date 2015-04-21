class WordPhoneticSpellingCharacter(object):
  def __init__(self, representations):  
    self._repr = representations
    self.pitch = None;
    self.duration = None;
  def as_repr(self, repr_name):
    return self._repr.get(repr_name, "")
  def is_vowel(self):
    return self._repr.get("phoneme_type") == "V"
  def is_consonant(self):
    return self._repr.get("phoneme_type") == "C"
  def representations(self):
    return self._repr.keys()
  def tts(self): 
    return self.as_repr("tts");
