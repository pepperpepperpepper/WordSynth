from Word.Syllables.Syllabizer import WordSyllablesSyllabizer
from Word.PhoneticSpelling.Character import WordPhoneticSpellingCharacter

class Cursor(Object):
  def __init__(self, character, characters):
    super(Cursor, self).__init__()
    self.character = character
    self.characters = characters
    self.position = 0
    self.syllable_break = False 
    self.prev_symbols = []
    self.next_symbols = []
    self.prev_phonemes = []
    self.next_phonemes = []
    def prev_symbols_set(self):
      self.prev_symbols = reversed(characters[0:self.position])
    def next_symbols_set(self):
      self.next_symbols = reversed(characters[self.position:len(characters)])
    def prev_phonemes_set(self): 
      self.prev_phonemes = filter(lambda x: x.as_repr("type") == "PHONEME", self.prev_symbols);
    def next_phonemes_set(self): 
      self.next_phonemes = filter(lambda x: x.as_repr("type") == "PHONEME", self.next_symbols);
    def prev(self):
      if self.position > 0:
        self.position -= 1
      return self.characters[self.position]
    def next(self):
      if self.position < len(self.characters):
        self.position += 1
      return self.characters[self.position]
    def reset(self):
      self.prev_symbols_set()
      self.next_symbols_set()
      self.prev_phonemes_set()
      self.next_phonemes_set()
  
class WordSyllablesSyllabizerTrouvain(WordSyllablesSyllabizer): 
  def __init__(self):
    pass
  def _get_positions(self, word):
  def _apply_rules(self, word.phonetic_spelling.characters):
    tokens = map(lambda x: Cursor(x), word.phonetic_spelling.characters)
  #well this requires a syllable_break array, didn't see that above, 

  def _rule2(self, tokens): #FIXME (only works with osxtts)
    for i in range(0, len(tokens)):
      if (i + 1) < len(tokens) and \
        tokens[i].character.as_repr("SYMBOL") == "1" and \
        tokens[i+1].character.as_repr("phoneme_type") == "V":
          tokens[i].position = i
          tokens[i].reset()
          var p = 1
          while(p < len(tokens[i].next_phonemes) and \
            tokens[i].next_phonemes[p].character.as_repr("TYPE") == 'C':
              p++
          if (p > 2 && tokens[i].next_phonemes[p]):
            while (tokens[i].character.as_repr("TYPE") != 'C'):
              i++
            tokens[i].syllable_break = True

#ok so I finish this by taking these boolean set breakpoints and turning them into a positions array? yep ok I can do that. good news is that this is pretty much done after that...
#there was one more script, merriam

  //RULE 3
  //if this doesn't work, try altering RULE 4
  var first_vowel = 0;
  var consonant_middle = 0;
  var second_vowel = 0;
  var first_vowel_position = 0;
  var consonant_middle_position = 0;
  for (var i = 0; i < tokens.length; i++){
    if (tokens[i].phoneme_type == 'V'){
      if (! first_vowel){
        first_vowel = 1;
        first_vowel_position = i
      }
    
      if (first_vowel && consonant_middle){

        second_vowel = 1;
        if (debug){
          console.log("Using rule 3");
          console.log("on this : ");
          console.log(tokens[first_vowel_position].symbol)
          console.log(first_vowel_position);
        }
        tokens[first_vowel_position].cursor = first_vowel_position;
        tokens[first_vowel_position].reset();
        if (! tokens[first_vowel_position].prev_phonemes.length){
          tokens[consonant_middle_position].syllable_break = 1;
        }else{
          tokens[first_vowel_position].syllable_break = 1;
        }
        first_vowel = 1;
        first_vowel_position = i;
        consonant_middle = 0;

      }

//_IHgz1AEmpAXl.
//_IHg - z1AEm - pAXl.
    }
    if (tokens[i].phoneme_type == 'C'){
      if (first_vowel){
        if (tokens[i].syllable_break){
          first_vowel = 0;
          consonant_middle = 0;
        }else{
          consonant_middle = 1;
          if (! consonant_middle_position){
            consonant_middle_position = i;
          }
        }
      }
    }
  } 

  //RULE 4 // Doesn't seem to be working
//  for (var i = 0; i < tokens.length; i++){
//    if (tokens[i].syllable_break && tokens[i].phoneme_type == 'V'){
//      if (tokens[i+1].symbol == 'n'){
//        tokens[i].syllable_break = 0;
//        tokens[i+1].syllable_break = 1;
//        if (debug){
//          console.log("Using rule 4");
//          console.log("on this : ");
//          console.log(tokens[i+1].symbol)
//        }
//      }
//    }
//  }
  return tokens;
}


function createPoints(tokens){
  var points = [];
  var position = 1;
  for (var i = 0; i < tokens.length; i++){
     
    if (tokens[i].syllable_break){
      points.push(position);
    }
    if (tokens[i].type == 'PHONEME' ){//|| (tokens[i]['type'] == 'PROSODIC_CONTROL' && tokens[i]['symbol'] == '1' )){
      position++;
    }
  }
  return points;
}

function getSyllablePoints(tokens){
  var tokens = applyRules(tokens);
  return createPoints(tokens);
}


var main = function(){
  var tokens = tokenize(test_string); 
  tokens = applyRules(tokens, 1); //with debug
  for (i in tokens){
    if (tokens[i].syllable_break == 1 && tokens[i].symbol != " "){
      console.log(tokens[i].print()); 
    }
  }
  createPoints(tokens);
}

if (require.main === module) {
    main();
}
module.exports = getSyllablePoints;


