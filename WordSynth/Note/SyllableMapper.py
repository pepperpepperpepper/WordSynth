import copy
import collections
from Word.Syllable import WordSyllable

DEFAULT_CONSONANT_DURATION = 20  # milliseconds


class NoteSyllableMapper(object):
    def __init__(self, **kwargs):
        if 'consonant_duration' in kwargs:
            self.consonant_duration = kwargs['consonant_duration']
        else:
            self.consonant_duration = DEFAULT_CONSONANT_DURATION

    def _add_note_to_vowel(self, character, note):
        """adds frequency information and duration to the character class"""
        character.pitch = note.pitch
        character.duration = note.duration
        return copy.copy(character)  # FIXME maybe need deepcopy

    def _map_notes_to_vowel(self, characters, vowel, notes):
        """adds notes to a vowel, adding duration and pitch
        returns vowel_notes...
        copies of the vowel character if necessary, in an array"""
        consonants_prev = filter(
            lambda x: x.is_consonant(), characters[0:characters.index(vowel)])
        consonants_after = filter(
            lambda x: x.is_consonant(), characters[characters.index(vowel)+1:])
        vowel_notes = map(
            lambda x: self._add_note_to_vowel(vowel, x), notes)
        vowel_notes[0].duration -= sum(
            map(lambda x: x.duration, consonants_prev))
        vowel_notes[-1].duration -= sum(
            map(lambda x: x.duration, consonants_after))
        return vowel_notes

    def _set_consonant_duration(self, character):
        """adds the necessary duration to the character"""
        if character.is_consonant():
            character.duration = self.consonant_duration
        else:
            character.duration = None
        return character

    def _flatten(self, l):
        """necessary for flattening the vowel_notes"""
        for el in l:
            if isinstance(el, collections.Iterable) and not \
                    isinstance(el, basestring):
                for sub in self._flatten(el):
                    yield sub
            else:
                yield el

    def map_notes_to_syllable(self, syllable, notes):
        """combines the above methods to add notes to a syllable
        see the diagram for the intended distribution effect
        transforms the syllable object in place adding notes to it"""
        if not type(syllable) is WordSyllable:
            raise ValueError("Must provide syllable")
        if not len(notes):
            raise ValueError("Must provide notes")
        # total_duration = sum(el.duration for el in notes)
        characters = syllable.characters()
        total_vowels = len(
            filter(lambda x: x.is_vowel(), syllable.characters()))
        if total_vowels > 1:
            raise ValueError(
                "Syllabification produced a syllable with {} vowels".format(
                    total_vowels))
        characters = map(
            lambda x: self._set_consonant_duration(x), syllable.characters()
        )  # sets a static duration
        characters = map(
            lambda x: self._map_notes_to_vowel(
                syllable.characters(), x, notes
            ) if x.is_vowel() else x, syllable.characters())
        syllable.characters_set(list(self._flatten(characters)))
        # example
        #  _____________________________________________________________________________________________________________________
        # |                  |                                |             |                                |                  |
        # |consonant_duration|note_duration-consonant_duration|note_duration|note_duration-consonant_duration|consonant_duration|
        # |__________________|________________________________|_____________|________________________________|__________________|
        # the first note's duration must be decreased by the sum of all preceding consonant_durations
        # the last note's duration must be decreased by the sum of all consonant_durations that come after

if __name__ == "__main__":
    nm = NoteSyllableMapper()
