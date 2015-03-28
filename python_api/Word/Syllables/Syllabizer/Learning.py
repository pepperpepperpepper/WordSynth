DATAFILE = "data/syllabize_learning.json"
from Word.Syllables.Syllabizer import WordSyllablesSyllabizer
class WordSyllablesSyllabizerLearning(WordSyllablesSyllabizer): 
  def __init__(self):
    self._datafile = DATAFILE
    super(WordSyllablesSyllabizerLearning, self).__init__()



