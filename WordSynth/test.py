#!/usr/bin/python2.7 
import inspect
 
import unittest
import sys
from Word import Word
from Word.String import WordString
from TTS.Marytts import TTSMarytts 
from TTS.OSXtts import TTSOSXtts 
from Word.Syllabizer.Learning import WordSyllabizerLearning 
from Word.Syllabizer.Marytts import WordSyllabizerMarytts 
from Word.Syllabizer.Trouvain import WordSyllabizerTrouvain 
from NoteMapper import NoteMapper; 

class TestTTSMaryttsSyllabizers(unittest.TestCase):
    def logPoint(self):
      'utility method to trace control flow'
      callingFunction = inspect.stack()[1][3]
      currentTest = self.id().split('.')[-1]
      print 'in %s - %s()' % (currentTest, callingFunction)

    def setUp(self):
      self.logPoint();
      self.test_string = "friendship chimichanga this is a test string"
      self.wordstring = WordString(self.test_string)
      self.first_word = self.wordstring.words[0]
      tts = TTSMarytts();
      tts.phonetize(self.first_word)
       
    def test_phonetizer(self):
      self.logPoint()
      self.assertEqual(
        self.first_word.phonetic_spelling().as_repr("phoneme_type"), 
        "CCVCCCVC"      
      )
    def test_syllabizer_learning(self):
      self.logPoint();
      syllabizer = WordSyllabizerLearning()
      syllabizer.create_syllables(self.first_word)
      self.assertEqual(
        map(lambda x: x.as_repr("symbol"), self.first_word.syllables()),
        ['frEnd', 'SIp']
      )

    def test_syllabizer_marytts(self):
      self.logPoint();
      syllabizer = WordSyllabizerMarytts()
      syllabizer.create_syllables(self.first_word)
      self.assertEqual(
        map(lambda x: x.as_repr("symbol"), self.first_word.syllables()),
        ['frEn','dSIp']
      )

    def test_syllabizer_trouvain(self):
      self.logPoint();
      syllabizer = WordSyllabizerTrouvain()
      syllabizer.create_syllables(self.first_word)
      self.assertEqual(
        map(lambda x: x.as_repr("symbol"), self.first_word.syllables()),
        ['frE', 'ndSIp']
      )

class TestTTSOSXttsSyllabizers(unittest.TestCase):
    def logPoint(self):
      'utility method to trace control flow'
      callingFunction = inspect.stack()[1][3]
      currentTest = self.id().split('.')[-1]
      print 'in %s - %s()' % (currentTest, callingFunction)

    def setUp(self):
      self.logPoint();
      self.test_string = "friendship chimichanga this is a test string"
      self.wordstring = WordString(self.test_string)
      self.first_word = self.wordstring.words[0]
      tts = TTSOSXtts();
      tts.phonetize(self.first_word)
       
    def test_phonetizer(self):
      self.logPoint()
      self.assertEqual(
        self.first_word.phonetic_spelling().as_repr("phoneme_type"), 
        "CCVCCCVC"      
      )
    def test_syllabizer_learning(self):
      self.logPoint();
      syllabizer = WordSyllabizerLearning()
      syllabizer.create_syllables(self.first_word)
      self.assertEqual(
        map(lambda x: x.as_repr("symbol"), self.first_word.syllables()),
        ['_fr1EHnd', 'SIHp.'] 
      )

    def test_syllabizer_marytts(self):
      self.logPoint();
      syllabizer = WordSyllabizerMarytts()
      syllabizer.create_syllables(self.first_word)
      self.assertEqual(
        map(lambda x: x.as_repr("symbol"), self.first_word.syllables()),
        ['frEn','dSIp']
      )

    def test_syllabizer_trouvain(self):
      self.logPoint();
      syllabizer = WordSyllabizerTrouvain()
      syllabizer.create_syllables(self.first_word)
      self.assertEqual(
        map(lambda x: x.as_repr("symbol"), self.first_word.syllables()),
        ['_fr1EH', 'ndSIHp.']
      )

if __name__ == '__main__':
  unittest.main(); 
  sys.exit(0)

tts = TTSOSXtts()
tts.phonetize(firstword) 
syllabizer = WordSyllabizerLearning()
syllabizer.create_syllables(firstword)
print firstword.syllables()

note_mapper = NoteMapper();


map(lambda x: note_mapper.note_map(x, [1,2,3])
  , firstword.syllables());
