import simplejson as json
from Word.Syllable import WordSyllable 
class WordSyllabizer(object):
  def __init__(self):
    self.data = self._load_from_jsonfile(self._datafile)
  def create_syllables(self, word):
    separation_points = self._get_positions(word)
    phoneme_count = 0  
    syllables = []
    characters_curr = [];
    for c in word.phonetic_spelling().characters():
      characters_curr.append(c)
      if( c.as_repr("type") == 'PHONEME'):
        phoneme_count += 1
        if (separation_points and phoneme_count == int(separation_points[0])):
          syllables.append(
              WordSyllable(
                  characters=characters_curr
              )
          )
          characters_curr = []
          separation_points.pop(0)
    syllables.append(WordSyllable(characters=characters_curr))
    word.syllables_set( syllables )
  def _get_positions(self, word):
    vc_string = self._build_vc_string(word)
    print vc_string
    learned_data = self.data.get(vc_string, None)
    if not learned_data: 
      raise ValueError("vc_string was not found in data")
    return learned_data[0]['positions'] 
  def _build_vc_string(self, word):
    return word.phonetic_spelling().vc_spelling()  
  def _load_from_jsonfile(self, filepath):
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return json.loads(data)
