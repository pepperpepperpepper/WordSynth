class Characters(object):
  def __init__(self, characters, pitch, duration):
    self.characters = characters
    self.pitch = pitch
    self.duration = duration

    



m = MediaContainer(syllable, notes);
mapper = NoteMapper()
mapper.apply(m)
renderer = RendererAudio(format="mp3")
renderer.render(m)


