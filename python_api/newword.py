#!/usr/bin/python2.7
import re
import urllib
import urllib2
class WordBuilder():
  def __init__(self, s):
    self.characters = s
    self._sanitized_characters = self.santize_characters(s)
    self._phonemes = self._fetch_phonemes(); 

  @staticmethod  
  def santize_characters(s):
    return re.sub(r"[^a-zA-Z0-9\s\-']", '', s)
  
  #ok what should some of the methods be?
  def from_string(string):
    # fetch
    return [ Word(), ... ] wait, what else would the Word come from if not from string? here I'll map this out
  def _fetch_phonemes(self):
    string = urllib.quote(self._sanitized_characters, '')
    url = "http://devel.chimecrisis.com/phonemes/{}".format(string)
    response = urllib2.urlopen(url).read()
    return re.sub(r"\n", '', response);

  
def tokenizerOSX(s):



Object Word 
  - has phonetic spellings (OSXtts, xsampa) with special pronunciation characters
  - has VC spelling (OSXtts, xsampa)
  - has syllable divisions (4 different ones) 
  - has original spelling (characters from string)

and that's it
also the way i did it the last time was that I identified all the special character types in the phonetic spellings

ok so it' a bit complicated to think about then it's all in text, but general idea is to have base classes like:
Word,
Token,
syllable
character and so on 
and have builder\fetcher classes, which can transform or add additional info into class, so it can be used like:

my $word = Word->new("hello");
my $tokenizer = Tokenizer::CoolOne->new();
$tokenizer->tokenize($word);
print Dumper $word->tokens();

my $token = $word->tokens->[0];
print Dumper $token->characters;

and so on.

how long do you think this would take to write in perl? not sure, depends on how many things need to be done and work together,
it's easier to see what you need if you just draw it on paper, how things relate to each other, do you need several sets of tokens for example,
or like one thing can have two possible views, etc.
ahh I see. one thing can have two views. here's the end result
http://devel.chimecrisis.com/syllables

ok so should I go back to the description of word, and make syllable, as a sub-model or something?
so let's try to write example from user point of view 



#ok this is not quite the way it works...but its helping
#first we have a string of chars
#we break the string into individual words of chars
"hello there" -> "hello", "there"

my $string_example = "example"
my $string = Syllables::String->new($string_example);
print Dumper $string->words; # Syllables::Word
#right?

#ok next we need to convert this to phonetic spellings
_heHl10W OR well h.4l_oo #some other spelling

my $phonetic = Syllables::Phonetic::MaryTTS->new();
$phonetic->add_phonetic($word); #  $word->add_phonetic(), $word->phonetics() etc
print Dumper $word->phonetics; # [ Syllable::Phonetic, ]
print Dumper $word->phonetics->[0]->characters # [ Syllable::Phonetic::Character { symbol: "h" } ], # $char->phoneme_type(), $char->type()

#from there we need to separate pronunciation marks etc, from consonants and vowels
#its very important that consonants and vowels are labeled
[[{"type":"PROSODIC_CONTROL","symbol":"_"},{"type":"PHONEME","symbol":"h","phoneme_type":"C"},{"type":"PHONEME","symbol":"EH","phoneme_type":"V"},{"type":"PHONEME","symbol":"l","phoneme_type":"C"},{"type":"PROSODIC_CONTROL","symbol":"1"},{"type":"PHONEME","symbol":"OW","phoneme_type":"V"},{"type":"PUNCTUATION_DATA","symbol":"."}]]


#from there we need a CVString (just the word in consonants and vowels only)
CVCV

$word->phonetics->[0]->as_cv; # CCV   # inside: as_cv { return join "", map { $_->as_cv } $self->characters }


#ok finally we can take this, and apply the algorithms to create syllables, and the Syllables
#will eventually have
#pitch 
#duration.....OR better yet

my $algo = Syllables::Algo::Webster->new()
$algo->make_syllables($word);
#I think I'm learning what I didn't understand...a pattern that I didn't get

#these methods $algo->make_syllables($word) are CHANGING the internal structure of word, like acting on it? yes ahhh
#well what is that similar to in procedural programming, besides my $word =~ s/this/that/g; or something?
# well in a way, here you just add additional info about word. it may be written in sort of word oriented way, where you have:
# $word->get_phonetic(), and it will use algo to get it, but that's hard to extend, as oyu need to edit word class each time, so it's better
#to have algo as separate object which adds additional info like here.
# I see what you're saying...seems like python has things sort of like

Word.addsyllables(Word.strategy.marytts) something like that? yeah that can work too, it just a bit more methods to write so 
start with a mutation type strategy, and then if it's confusing, add simplifying handles into it? yes ok cool I sort of get it
alright I'll do my best. Thanks a lot no problems




#note will have pitch and duration and syllable....

#sorry, terrible thing is that I have a tough time thinking in any way besides procedural so do you understand the basic
#way this goes down? alright




my $algo = Syllables::Algo::Webster->new();
$algo->tokenize($string)
print Dumper $string->syllables_as_string; #    _hEH - l1OW.
print Dumper $string->syllables; # [ Syllables::Word::Syllable, ... ]

my $algo_pitch = Syllables::Algo::PitchAlgo->new();
$algo->set_pitches($string);
print Dumper $string->syllables; # [ Syllables::Word::Syllable { pitch => 10, duaction => 20 } ]


foreach my $syllable ($string->syllables){
    # render sound here 
    print Dumper $syllable->pitch, $syllable->duration;
}

# something like this? (maybe String is not required, but seems like necessary if string have several words)


