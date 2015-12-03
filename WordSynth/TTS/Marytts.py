#!/usr/bin/python2.7
import sys
import urllib2
import urllib
import simplejson as json
from xml.dom import minidom
from Word.PhoneticSpelling import WordPhoneticSpelling
from Word.PhoneticSpelling.Character import WordPhoneticSpellingCharacter
# from WordSynth.config import MARYTTS_ROUTE


class TTSMarytts(object):
    def __init__(self):
        self._url = "http://localhost:59125/process"
        self.char_data_load("share/marytts_xsampa_char_data.json")

    def char_data_load(self, filename):
        char_data_file = open(filename, "r")
        self._char_data = json.loads(char_data_file.read())
        char_data_file.close()

    @property
    def char_data(self):
        return self._char_data

    def _make_marytts_params(self, s):
        return {
            'INPUT_TYPE': 'TEXT',
            'OUTPUT_TYPE': 'ALLOPHONES',
            'INPUT_TEXT': s,
            'LOCALE': 'en_US'
        }

    def syllabize(self, s):
        return map(lambda x: self._get_phoneme_values(x),
                   self._get_syllable_nodes(s))

    def get_phonemes(self, s):
        return sum(self.syllabize(s), [])

    def _get_syllable_nodes(self, s):
        data = self.post_request(self._url, self._make_marytts_params(s))
        tree = minidom.parseString(data)
        return tree.getElementsByTagName('syllable')

    def _get_phoneme_values(self, node):
        char_data_arr = []
        for ph in node.getElementsByTagName("ph"):
            c = self.char_data[ph.attributes['p'].value]
            c.update({"tts": "Marytts"})
            char_data_arr.append(WordPhoneticSpellingCharacter(c))
        return char_data_arr

    def phonetize(self, word):
        word.phonetic_spelling_set(
            WordPhoneticSpelling(
                characters=self.get_phonemes(word.as_string)
            )
        )

    @staticmethod
    def post_request(url, params):
        params = urllib.urlencode(params)
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
        }
        try:
            req = urllib2.Request(url, params, headers)
            response = urllib2.urlopen(req)
            return response.read()
        except Exception as e:
            sys.stderr.write(str(e))
            raise
