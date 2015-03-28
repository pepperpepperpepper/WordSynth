class WordSyllables():
  def __init__(self, **kwargs):
    self._syllables = None 
    self.syllables_set(kwargs.get('syllables', []))

  def syllables(self):
    return self._syllables
  def syllables_set(self, syllables):
    self._syllables = syllables

  def as_repr(self, repr_name, **kwargs):
    join_str = kwargs.get("join_str", "-")
    return join_str.join( map(lambda c: c.as_repr(repr_name, **kwargs), self.syllables()) )
 

