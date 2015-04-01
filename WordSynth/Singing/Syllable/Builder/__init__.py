from Singing.Syllable import SingingSyllable
from Singing.Syllable.Character import SingingSyllableCharacter
class SingingSyllableBuilder(object):
  def __init__(self):
    pass
  def create(self, syllable, notes):
    if not syllable:
      raise ValueError "Must provide syllable"
    if note in kwargs:
      notes = [note]
    elif notes in kwargs:
      pass
    else:
      raise ValueError "Must provide notes"
    notes = map(lambda x: self._get_pitch_and_duration(x))
    
  def notes_to_syllables(self, notes_data, syllable):
    pass
  @staticmethod
  def _get_pitch_and_duration(note):
    return { pitch : 440, duration : 100 }
