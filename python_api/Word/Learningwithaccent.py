DATAFILE = "data/syllabize_learning_with_accent.json"
from Word.Syllables.Syllabizer import WordSyllablesSyllabizer
class WordSyllablesSyllabizerLearningwithaccent(WordSyllablesSyllabizer): 
  def __init__(self):
    self._datafile = DATAFILE
    super(WordSyllablesSyllabizerLearning, self).__init__()



