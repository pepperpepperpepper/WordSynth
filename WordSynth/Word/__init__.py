class Word(object):
  def __init__(self, s):
    self.as_string = s
    self._phonetic_spelling = None
    self._syllables = None
  def __str__(self):
    return str({
      "syllables" : str(self.syllables()),
      "phonetic_spelling" : str(self.phonetic_spelling()),
      "as_string" : self.as_string
    })
  def phonetic_spelling_set(self, characters):
    self._phonetic_spelling = characters
  def phonetic_spelling(self):
    return self._phonetic_spelling
  def syllables_set(self, syllables):
    self._syllables = syllables
  def syllables(self):
    return self._syllables
