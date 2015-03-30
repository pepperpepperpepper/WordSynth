DATAFILE = "data/syllabize_learning_with_accent.json"
from Word.Syllables.Syllabizer import WordSyllablesSyllabizer
class WordSyllablesSyllabizerLearningwithaccent(WordSyllablesSyllabizer): 
  def __init__(self):
    self._datafile = DATAFILE
    super(WordSyllablesSyllabizerLearningwithaccent, self).__init__()
  def _build_vc_string(self, word):
    def get_sym(c):
      if c.as_repr("symbol") == '1': 
        return c.as_repr("symbol")
      else:
        return c.as_repr("phoneme_type")
    return "".join( map(lambda c: get_sym(c), word.phonetic_spelling().characters()))


