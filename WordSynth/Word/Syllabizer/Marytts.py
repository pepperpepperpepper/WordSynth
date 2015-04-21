import simplejson as json
from Word.Syllable import WordSyllable
from Word.Syllabizer import WordSyllabizer
from TTS.Marytts import TTSMarytts 
class WordSyllabizerMarytts(WordSyllabizer):
  def __init__(self):
    pass;
  def create_syllables(self, word):
    tts = TTSMarytts()
    syllables = map(lambda x: WordSyllable(characters=x), tts.syllabize(word.as_string))
    word.syllables_set( syllables )
