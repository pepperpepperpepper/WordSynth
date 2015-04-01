class SingingSyllable(object):
  def __init__(self, syllable=None, **kwargs):
    if not syllable:
      raise ValueError "Must provide syllable"
    self._syllable = syllable
    if note in kwargs:
      self._notes = [note]
    elif notes in kwargs:
      self._notes = notes
    else:
      raise ValueError "Must provide notes"
    self._singing_characters = None
    

m = MediaContainer(syllable, notes);
mapper = NoteMapper()
mapper.apply(m)
renderer = RendererAudio(format="mp3")
renderer.render(m)


