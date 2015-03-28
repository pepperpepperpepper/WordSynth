class WordPhoneticSpellingCharacter:
  def __init__(self, representation):  
    this._repr = representation
  def as_repr(self, repr_name):
    return this._repr.get(repr_name, "")

