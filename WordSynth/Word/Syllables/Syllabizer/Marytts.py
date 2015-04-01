import simplejson as json
from Word.Syllable import WordSyllable
from Word.Syllables import WordSyllables
from Word.Syllables.Syllabizer import WordSyllablesSyllabizer
from TTS.Marytts import TTSMarytts 
class WordSyllablesSyllabizerMarytts(WordSyllablesSyllabizer):
  def __init__(self):
    pass;
  def create_syllables(self, word):
    tts = TTSMarytts()
    syllables = map(lambda x: WordSyllable(characters=x), tts.syllabize(word.as_string))
    word.syllables_set( WordSyllables( syllables = syllables ) )
