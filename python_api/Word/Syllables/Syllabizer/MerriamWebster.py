DATAFILE = "data/merriam_webster.json"
from Word.Syllables.Syllabizer import WordSyllablesSyllabizer
class WordSyllablesSyllabizerMerriamWebster(WordSyllablesSyllabizer): 
  def __init__(self):
    self._datafile = DATAFILE
    super(WordSyllablesSyllabizerMerriamWebster, self).__init__()
  def _get_positions(self, word):
    positions = self.data.get(word.as_string, None)
    if not positions: 
      raise ValueError("{} was not found in merriam webster data".format(word.as_string))
    return positions
