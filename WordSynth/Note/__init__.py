import sys
from abjad import Note, Duration, pitchtools


class Note(object):
  def __init__(self, pitch, duration):
    self.pitch = pitch #pitch in hertz
    self.duration = duration #duration in milliseconds
  def __str__(self):
     return "<Note Object:  pitch:{} hz, duration:{}>".format(self.pitch, self.duration)
  def __repr__(self):
    return str(self)
  @classmethod
  def from_music(cls, midi_note, duration, tempo):
    """expects duration in decimal"""
    pitch = freq = 440 * 2^((midi_note-69)/12) 
    d = duration * tempo;
    return cls(pitch, d);
  @classmethod
  def from_abjad(cls, note, tempo):
    #calculate tempo here
    d = note.written_duration
    duration = d.numerator * tempo * d.denominator/4
    pitch = pitchtools.NamedPitch(note.note_head).hertz
    return cls(pitch, duration)
  @classmethod
  def from_music21():
    raise "Not Yet Implemented"
    #Num is a fraction of a beat
    #(num / (tempo * 1/60)) * 1000
    #music21 note.duration * tempo (from music21.tempo tempoinstance.number * durationinstance.quarterLength
    #BPM -> BPS (FIRST CONVERT BPM to BEATS PER MILLISECOND ) divide tempo by 6000
