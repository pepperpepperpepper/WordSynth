from Word.Syllabizer import WordSyllabizer
from Word.PhoneticSpelling.Character import WordPhoneticSpellingCharacter

class Cursor(object):
  def __init__(self, character, characters):
    super(Cursor, self).__init__()
    self.character = character
    self.characters = characters
    self.position = 0
    self.syllable_break = False 
    self.prev_symbols = []
    self.next_symbols = []
    self.prev_phonemes = []
    self.next_phonemes = []
  def prev_symbols_set(self):
    self.prev_symbols = reversed(self.characters[0:self.position])
  def next_symbols_set(self):
    self.next_symbols = reversed(self.characters[self.position:len(self.characters)])
  def prev_phonemes_set(self): 
    self.prev_phonemes = filter(lambda x: x.as_repr("type") == "PHONEME", self.prev_symbols);
  def next_phonemes_set(self): 
    self.next_phonemes = filter(lambda x: x.as_repr("type") == "PHONEME", self.next_symbols);
  def prev(self):
    if self.position > 0:
      self.position -= 1
    return self.characters[self.position]
  def next(self):
    if self.position < len(self.characters):
      self.position += 1
    return self.characters[self.position]
  def reset(self):
    self.prev_symbols_set()
    self.next_symbols_set()
    self.prev_phonemes_set()
    self.next_phonemes_set()
import sys
class WordSyllabizerTrouvain(WordSyllabizer): 
  def __init__(self):
    pass
  def _get_positions(self, word):
    return self._apply_rules(word.phonetic_spelling().characters())

  def _apply_rules(self, characters):
    tokens = map(lambda x: Cursor(x, characters), characters)
    self._rule2(tokens)
    self._rule3(tokens)
    return self._create_separation_points(tokens)

  def _rule2(self, tokens): #FIXME (only works with osxtts)
    for i in range(0, len(tokens)):
      if (i + 1) < len(tokens) and \
        tokens[i].character.as_repr("phoneme_type") == "1" and \
        tokens[i+1].character.as_repr("phoneme_type") == "V":
          tokens[i].position = i
          tokens[i].reset()
          p = 1
          while p < len(tokens[i].next_phonemes) and \
            tokens[i].next_phonemes[p].character.as_repr("TYPE") == 'C':
              p += 1
          if (p > 2 and tokens[i].next_phonemes[p]):
            while (tokens[i].character.as_repr("TYPE") != 'C'):
              i += 1
            tokens[i].syllable_break = True
    return tokens

  def _rule3(self, tokens):
    first_vowel = False 
    consonant_middle = False 
    second_vowel = False 
    first_vowel_position = None 
    consonant_middle_position = None
    for i in range(0, len(tokens)):
      if tokens[i].character.as_repr("phoneme_type") == 'V':   
        if not first_vowel:
          first_vowel = True
          first_vowel_position = i
        if first_vowel and consonant_middle:
          second_vowel = True
          tokens[first_vowel_position].position = first_vowel_position
          tokens[first_vowel_position].reset()
          if not len(tokens[first_vowel_position].prev_phonemes):
            tokens[consonant_middle_position].syllable_break = True
          else:
            tokens[first_vowel_position].syllable_break = True
          first_vowel = True
          first_vowel_position = i
          consonant_middle = False
      if tokens[i].character.as_repr("phoneme_type") == 'C':
        if first_vowel:
          if tokens[i].syllable_break:
            first_vowel = False 
            consonant_middle = False 
          else:
            consonant_middle = True
            if not consonant_middle_position:
              consonant_middle_position = i
    return tokens
  def _create_separation_points(self, tokens):
    separation_points = []
    position = 1;
    for i in range(0, len(tokens)):
      if tokens[i].syllable_break:
        separation_points.append(position)
      if tokens[i].character.as_repr('type') == 'PHONEME':
        position += 1
    return separation_points

