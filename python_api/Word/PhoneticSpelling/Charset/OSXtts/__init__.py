from Word.PhoneticSpelling.Charset import WordPhoneticSpellingCharset 
from Word.PhoneticSpelling.Charset.OSXtts.Tokenizer import WordPhoneticSpellingCharsetOSXttsTokenizer 
class WordPhoneticSpellingCharsetOSXtts(WordPhoneticSpellingCharset):
  def __init__(self):
    self.tokenizer = WordPhoneticSpellingCharsetOSXttsTokenizer()
