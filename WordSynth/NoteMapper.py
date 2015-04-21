import pprint
import sys

class NoteMapper(object):
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
    return character;
  def _set_vowel_duration(self,characters, vowel, notes):
    consonants_prev = filter(lambda x: x.is_consonant(), characters[0:characters.index(vowel)])
    consonants_after = filter(lambda x: x.is_consonant(), characters[characters.index(vowel)+1:])
    vowel_notes = map(lambda x: self._add_note_to_vowel(vowel, x), notes )
    vowel_notes[0].duration -= sum(map(lambda x: x.duration, consonants_prev))  
    vowel_notes[-1].duration -= sum(map(lambda x: x.duration, consonants_after))
    return vowel_notes
  def _set_consonant_duration(self,character):
    print "in set"
    print character._repr.get("phoneme_type"); #somehting wrong here...can't print character type? only one character is coming back...something seems broken? yeah
    print "in set 2" # it's none for some reason for other chars bad...these characters aren't getting set correctly
    #do you think it's a problem with the syllable class? yeah could be, need to add prints there and check if phoneme_type is set for all chars.
    # I still feel we should get rid of wordsyllable entirely. just makes it a bit confusing for me and I think I don't need it...
    #I could add it back if I need it later? sure
    if character.is_consonant():
      character.duration = self.CONSONANT_DURATION 
    else: 
      character.duration = None;
    print character.duration;
    return character
  def note_map(self, syllable, notes): 
    if not syllable:
      raise ValueError("Must provide syllable")
    if not len(notes):
#    if note in kwargs:
#      notes = [note]
#    elif notes in kwargs:
#      pass
#    else:
      raise ValueError("Must provide notes")
    notes = map(lambda x: self._get_pitch_and_duration(x), notes)
    total_duration = sum(el['duration'] for el in notes)
    characters = syllable.characters();
    total_vowels = len(filter(lambda x: x.is_vowel(), characters))    
    if total_vowels > 1:
      raise ValueError("Syllabification produced a syllable with {} vowels".format(total_vowels))
    characters = map(lambda x: self._set_consonant_duration(x), characters ) #sets a static duration
    characters = map(lambda x: self._set_vowel_duration(characters, x, notes) if x.is_vowel() else x, characters)
    for i in characters[0:2]:
      print i.duration
    sys.exit(0);
    #return [item for sublist in characters for item in sublist] #all this oneliner does it flatten the list. 
    

#example
# _____________________________________________________________________________________________________________________
#|                  |                                |             |                                |                  | 
#|consonant_duration|note_duration-consonant_duration|note_duration|note_duration-consonant_duration|consonant_duration|
#|__________________|________________________________|_____________|________________________________|__________________|
    #the first note's duration must be decreased by the sum of all preceding consonant_durations
    #the last note's duration must be decreased by the sum of all consonant_durations that come after


