import simplejson as json
DATAFILE = "data/syllabize_learning.json"
class SyllabizerLearning():
  def __init__(self):
    self.datafile = DATAFILE
  #throw up to parent class
  def make_syllables(self, word):
    self.data = json.loads(self.datafile)
    self.positions = word.phonetic_VCstring in keys self.data ? self.data[word.phonetic_VCstring] : None
    
      
    if (learned_data){
      return learned_data[0]['positions'];
    }else{
      return false;
    }
