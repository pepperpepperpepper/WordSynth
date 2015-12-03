class WordPhoneticSpellingCharacter(object):
    def __init__(self, representations):
        # tts', 'phoneme_type', 'symbol', 'type', 'description'
        self._repr = representations
        self.pitch = None
        self.duration = None

    def __str__(self):
        return (
            "<Character obj:\n" +
            "\tpitch: {}\n" +
            "\tduration: {}\n" +
            "\t--representations--\n" +
            "\tphoneme_type: {}\n" +
            "\tsymbol: {}\n" +
            "\ttype: {}\n" +
            "\tdescription: {}\n" +
            "\ttts: {}\n>"
        ).format(
            self.pitch,
            self.duration,
            self.as_repr("phoneme_type"),
            self.as_repr("symbol"),
            self.as_repr("type"),
            self.as_repr("description"),
            self.as_repr("tts")
        )

    def __repr__(self):
        return str(self)

    def as_repr(self, repr_name):
        return self._repr.get(repr_name, "")

    def is_vowel(self):
        return self._repr.get("phoneme_type") == "V"

    def is_consonant(self):
        return self._repr.get("phoneme_type") == "C"

    def representations(self):
        return self._repr.keys()

    def tts(self):
        return self.as_repr("tts")
