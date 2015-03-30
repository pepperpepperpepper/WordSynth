from Word.PhoneticSpelling import WordPhoneticSpelling
from Word.PhoneticSpelling.Character import WordPhoneticSpellingCharacter
class WordPhoneticSpellingCharset():
  def process(self, word):
    data_raw = tokenizer.tokenize(word)
    chararacters = WordPhoneticSpelling(**{ 
      'characters': map( 
        lambda d: WordPhoneticSpellingCharacter(d),
        data_raw
      )
    })
    word.phonetic_spelling_set(chararacters)

