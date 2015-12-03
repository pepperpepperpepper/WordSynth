#!/usr/bin/python2.7
import inspect
import unittest
from Word.String import WordString
from TTS.Marytts import TTSMarytts
from TTS.OSXtts import TTSOSXtts
from Word.Syllabizer.Learning import WordSyllabizerLearning
from Word.Syllabizer.Marytts import WordSyllabizerMarytts
from Word.Syllabizer.Trouvain import WordSyllabizerTrouvain


class SyllabizersTests(object):
    def logPoint(self):
        'utility method to trace control flow'
        callingFunction = inspect.stack()[1][3]
        currentTest = self.id().split('.')[-1]
        print 'in %s - %s()' % (currentTest, callingFunction)

    def setUp_common(self, TTS):
        self.logPoint()
        self.test_string = "friendship chimichanga this is a test string"
        self.wordstring = WordString(self.test_string)
        self.first_word = self.wordstring.words[0]
        tts = TTS()
        tts.phonetize(self.first_word)

    def test_phonetizer(self, expected_result):
        self.logPoint()
        self.assertEqual(
            self.first_word.phonetic_spelling().as_repr("phoneme_type"),
            expected_result
        )

    def test_syllabizer_learning(self, expected_result):
        self.logPoint()
        syllabizer = WordSyllabizerLearning()
        syllabizer.create_syllables(self.first_word)
        self.assertEqual(
            map(lambda x: x.as_repr("symbol"), self.first_word.syllables()),
            expected_result
        )

    def test_syllabizer_marytts(self, expected_result):
        self.logPoint()
        syllabizer = WordSyllabizerMarytts()
        syllabizer.create_syllables(self.first_word)
        self.assertEqual(
            map(lambda x: x.as_repr("symbol"), self.first_word.syllables()),
            expected_result
        )

    def test_syllabizer_trouvain(self, expected_result):
        self.logPoint()
        syllabizer = WordSyllabizerTrouvain()
        syllabizer.create_syllables(self.first_word)
        self.assertEqual(
            map(lambda x: x.as_repr("symbol"), self.first_word.syllables()),
            expected_result
        )


class TestTTSMaryttsSyllabizers(unittest.TestCase, SyllabizersTests):
    def setUp(self):
        super(TestTTSMaryttsSyllabizers, self).setUp_common(TTSMarytts)

    def test_phonetizer(self):
        super(TestTTSMaryttsSyllabizers, self).test_phonetizer("CCVCCCVC")

    def test_syllabizer_learning(self):
        super(TestTTSMaryttsSyllabizers, self).test_syllabizer_learning(
            ['frEnd', 'SIp']
        )

    def test_syllabizer_marytts(self):
        super(TestTTSMaryttsSyllabizers, self).test_syllabizer_marytts(
            ['frEn', 'dSIp']
        )

    def test_syllabizer_trouvain(self):
        super(TestTTSMaryttsSyllabizers, self).test_syllabizer_trouvain(
            ['frE', 'ndSIp']
        )


class TestTTSOSXttsSyllabizers(unittest.TestCase, SyllabizersTests):
    def setUp(self):
        super(TestTTSOSXttsSyllabizers, self).setUp_common(TTSOSXtts)

    def test_phonetizer(self):
        super(TestTTSOSXttsSyllabizers, self).test_phonetizer("CCVCCCVC")

    def test_syllabizer_learning(self):
        super(TestTTSOSXttsSyllabizers, self).test_syllabizer_learning(
            ['_fr1EHnd', 'SIHp.'])

    def test_syllabizer_marytts(self):
        super(TestTTSOSXttsSyllabizers, self).test_syllabizer_marytts(
            ['frEn', 'dSIp']
        )

    def test_syllabizer_trouvain(self):
        super(TestTTSOSXttsSyllabizers, self).test_syllabizer_trouvain(
            ['_fr1EH', 'ndSIHp.']
        )

if __name__ == '__main__':
    unittest.main()
