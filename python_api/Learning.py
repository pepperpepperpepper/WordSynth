import simplejson as json
DATAFILE = "data/syllabize_learning.json"
class SyllabizerLearning():
  def __init__(self):
    self.datafile = DATAFILE
  #throw up to parent class
  def make_syllables(self, word):
    self.data = json.loads(self.datafile)
    learned_data = word.phonetic_VCstring in keys self.data ? self.data[word.phonetic_vcstring] : None
    if not learned_data: return

    self.positions = learned_data[0]['positions']
    word.syllables = self.divide_word_by_positions(word)
  def divide_word_by_positions(word): 
    word.tokens.foreach( #function here
