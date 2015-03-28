#!/usr/bin/python2.7 
#my $phonetic = Syllables::Phonetic::MaryTTS->new();
#$phonetic->add_phonetic($word); #  $word->add_phonetic(), $word->phonetics() etc
#print Dumper $word->phonetics; # [ Syllable::Phonetic, ]
#print Dumper $word->phonetics->[0]->characters # [ Syllable::Phonetic::Character { symbol: "h" } ], # $char->phoneme_type(), $char->type()



class OSXtts():
  def __init__(self):
  def create_phonetics(self, word):
    phonetic = SyllablesPhonetic()
    data_raw = self._get_tokens(word.as_string)
    #foreach my $char_raw (@$data_raw){
    #  my $char = Syllables::Phonetic::Character($char_raw);
    #  push @{ $phonetic->characters }, $char;
    #}
    word.phonetics.append(phonetic)
    
  #so assuming this is the data, what does the rest of this sort of look like? so need to have two classes, Phonetics and Character, which can hold data
  #def _get_phonemes(self):
  #  phonemes = "_t1EHst";
  def _get_tokens(self):
    tokens = [{"type":"PROSODIC_CONTROL","symbol":"_"},{"type":"PHONEME","symbol":"t","phoneme_type":"C"},{"type":"PROSODIC_CONTROL","symbol":"1"},{"type":"PHONEME","symbol":"EH","phoneme_type":"V"},{"type":"PHONEME","symbol":"s","phoneme_type":"C"},{"type":"PHONEME","symbol":"t","phoneme_type":"C"},{"type":"PUNCTUATION_DATA","symbol":"."}]

#so marytts class will use SyllablesPhonetic and SyllablesPhoneticCharacter as well? yes ok cool I can make this work, I get it
#I have been running john against the phonemes command on OSX for months now, trying to detatch the need for OSX at all to generate the
#phonetic spelling. what do you think I should do with the data? put it in one big hash? it's 0.5 gb well try to improve it a bit, there most likely
#can be extracted rules which cover a lot of samples, and everything else can be as exceptions in hash. so study it, see how it is working as best I can? yep
#got it...for that Phonemes converter, I should use OOP too, right? yep

#any idea what it might look like, or be called, the class? like class TextToPhonemes or something? or is that procedural again... OSXRecostructed or something like it
#ok...ultimately the conversion is sort of a procedural process though, right? I mean it can be a class with methods etc, but this task is sort of 
#procedural? yes like pipeline can we go over a mock example, no code is really necessary



class OSXRecostructed:
  sub new(self, s):
    this.string = s
    
  sub exceptions_lookup
  sub rules_lookup
  sub numeric_test #tests if its a number that can be converted without the hash
  sub process {
    my $word = @_;

    while($word){
      if(... numbers .. ){
      }
      if(my $res = $self->exceptions_lookup($word)){
        push @phonemes, $res;
        $word = substr($word, ...)
      }
      if(my $res = $self->rules_lookup($word)){
        push @phonemes, $res;
        $word = substr($word, ...)
      } 
      
    }
  }
what would the other function sort of look like, 
sort of like this? something like this wouldn't exceptions lookup come as a last else statement? or something? no, they override rules, so should be chcked first
oh so you're saying, look it up in exceptions first, if it's not in the hash, then with rules, if unable to use rules, just send an error? yep
ok is process called from new? no, just standalone object which can be called why not tie it into new? there can be many words to process, we don't want to load 
everything each time we want to process new word.
ok so how do you imagine this thing being invoked?
my $algo = OSXRecustructed->new()
my $word = Word->new();
$algo->process($word);
print Dumper $word->phonemes;
  ok I get it. thanks a lot no problems

# in other files:
class SyllablesPhonetic(object):
  def __init__(self):
    pass
  def characters(self, *params): 
    return self.characters
  def as_string(self):
    #return join "", map { $_->symbol } $self->characters;

class SyllablesPhoneticCharacter(object):
  def __init__(self):
  def type(self):
  def symbol(self):
  def phoneme_type(self):
