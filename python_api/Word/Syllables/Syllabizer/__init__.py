import simplejson as json
from Word.Syllables import WordSyllables 
from Word.Syllable import WordSyllable 
class WordSyllablesSyllabizer():
  def __init__(self):
    self.data = json.loads(self._datafile)
  def create_syllables(self, word):
    separation_points = self._get_positions(word)
    phoneme_count = 0  
    syllables = []
    characters_curr = [];
    for c in  word.phonetic_spelling.characters
      characters_curr.append(c)
      if( c.as_repr("type") == 'PHONEME'):
        phoneme_count += 1
        if (phoneme_count == separation_points[0]):
          syllables.append(
              WordSyllable(
                  characters=characters_curr
              )
          )
          characters_curr = []
          separation_points.pop(0)
    word.syllables_set( WordSyllables( syllables = syllables ) )
  def _get_positions(self, word):
    vc_string = word.phonetic_spelling.vc_string()
    learned_data = self.data.get(vc_string, None)
    if not learned_data: 
      raise ValueError
    return learned_data[0]['positions'] 

