DATAFILE = "data/merriam_webster.json"
from Word.Syllabizer import WordSyllabizer
class WordSyllabizerMerriamWebster(WordSyllabizer): 
  def __init__(self):
    self._datafile = DATAFILE
    super(WordSyllabizerMerriamWebster, self).__init__()
  def _get_positions(self, word):
    positions = self.data.get(word.as_string, None)
    if not positions: 
      raise ValueError("{} was not found in merriam webster data".format(word.as_string))
    return positions
