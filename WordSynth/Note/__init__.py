import sys
from abjad import Note, Duration, pitchtools


class Note(object):
  def __init__(self, pitch, duration):
    self.pitch = pitch
    self.duration = duration 
  @classmethod
  def from_music(cls, midi_note, duration, tempo):
    raise "Not Yet Implemented"
  @classmethod
  def from_abjad(cls, note, tempo):
    #calculate tempo here
    d = note.written_duration
    duration = d.numerator * tempo * d.denominator/4
    pitch = pitchtools.NamedPitch(note.note_head).hertz
    return cls(pitch, duration)
