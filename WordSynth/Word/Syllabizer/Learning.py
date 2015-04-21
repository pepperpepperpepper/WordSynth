DATAFILE = "data/syllabize_learning.json"
from Word.Syllabizer import WordSyllabizer
class WordSyllabizerLearning(WordSyllabizer): 
  def __init__(self):
    self._datafile = DATAFILE
    super(WordSyllabizerLearning, self).__init__()



