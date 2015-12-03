from Word.Syllabizer import WordSyllabizer
DATAFILE = "share/syllabize_learning.json"


class WordSyllabizerLearning(WordSyllabizer):
    def __init__(self):
        self._datafile = DATAFILE
        super(WordSyllabizerLearning, self).__init__()
