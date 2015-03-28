class WordSyllable():
  def __init__(self, **kwargs):
    self._characters = None 
    self.characters_set(kwargs.get('characters', []))

  def characters(self):
    return self._characters
  def characters_set(self, characters):
    self._characters = characters

  def as_repr(self, repr_name, **kwargs):
    join_str = kwargs.get("join_str", "")
    return join_str.join( map(lambda c: c.as_repr(repr_name, **kwargs), self.characters()) )
 

