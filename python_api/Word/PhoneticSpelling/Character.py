class WordPhoneticSpellingCharacter:
  def __init__(self, representations):  
    self._repr = representations
  def __getattr__(self, attr):
    return self.as_repr(attr)
  def as_repr(self, repr_name):
    return self._repr.get(repr_name, "")
  def representations(self):
    return self._repr.keys()
