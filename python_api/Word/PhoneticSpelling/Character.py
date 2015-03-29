class WordPhoneticSpellingCharacter:
  def __init__(self, representation):  
    self._repr = representation
  def as_repr(self, repr_name):
    return self._repr.get(repr_name, "")

