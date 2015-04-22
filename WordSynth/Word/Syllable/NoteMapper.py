import copy
import collections
import inspect
from Word.Syllable import WordSyllable
from Word import Word
import sys

class WordSyllableNoteMapper(object):
  def __init__(self):
    self.CONSONANT_DURATION = 20;
  def _get_pitch_and_duration(self,note): #FIXME add music21 code
    #Num is a fraction of a beat
    #(num / (tempo * 1/60)) * 1000
    #music21 note.duration * tempo (from music21.tempo tempoinstance.number * durationinstance.quarterLength
    #BPM -> BPS (FIRST CONVERT BPM to BEATS PER MILLISECOND ) divide tempo by 6000
    return { "pitch" : 440, "duration" : 100 }

  def _add_note_to_vowel(self, character, note):
    character.pitch = note['pitch']
    character.duration = note['duration']
    return copy.copy(character); #maybe need deepcopy
  def _set_vowel_duration(self,characters, vowel, notes):
    consonants_prev = filter(lambda x: x.is_consonant(), characters[0:characters.index(vowel)])
    consonants_after = filter(lambda x: x.is_consonant(), characters[characters.index(vowel)+1:])
    vowel_notes = map(lambda x: self._add_note_to_vowel(vowel, x), notes )
    vowel_notes[0].duration -= sum(map(lambda x: x.duration, consonants_prev))  
    vowel_notes[-1].duration -= sum(map(lambda x: x.duration, consonants_after))
    return vowel_notes
  def _set_consonant_duration(self,character):
    if character.is_consonant():
      character.duration = self.CONSONANT_DURATION 
    else: 
      character.duration = None;
    return character
  def _flatten(self, l): #flattens a list
      for el in l:
          if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
              for sub in self._flatten(el):
                  yield sub
          else:
              yield el

  def stream_map(self, syllable, notes): 
    if not type (syllable) is WordSyllable:
      raise ValueError("Must provide syllable")
    if not len(notes): #FIXME change to music21 stream
      raise ValueError("Must provide notes")
    notes = map(lambda x: self._get_pitch_and_duration(x), notes)
    total_duration = sum(el['duration'] for el in notes)
    characters = syllable.characters();
    total_vowels = len(filter(lambda x: x.is_vowel(), syllable.characters()))    
    if total_vowels > 1:
      raise ValueError("Syllabification produced a syllable with {} vowels".format(total_vowels))
    characters = map(lambda x: self._set_consonant_duration(x), syllable.characters() ) #sets a static duration
    characters = map(lambda x: self._set_vowel_duration(syllable.characters(), x, notes) if x.is_vowel() else x, syllable.characters())
    syllable.characters_set(list(self._flatten(characters)))
#example
# _____________________________________________________________________________________________________________________
#|                  |                                |             |                                |                  | 
#|consonant_duration|note_duration-consonant_duration|note_duration|note_duration-consonant_duration|consonant_duration|
#|__________________|________________________________|_____________|________________________________|__________________|
    #the first note's duration must be decreased by the sum of all preceding consonant_durations
    #the last note's duration must be decreased by the sum of all consonant_durations that come after

