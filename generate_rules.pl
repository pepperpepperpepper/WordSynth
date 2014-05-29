use JSON;
use utf8;
my $RULE_FILE = "rules.json";
open(my $fh, ">", $RULE_FILE) 
  or die "cannot open > output.txt: $!";

my $rules = {
  'syllable' => ["'", '"','-', "ˈ" ],
  'optional' => [ qw/( )/ ], #not using
  'variant' => [qw/ , ; ÷ \s /] , #not using
  'unstressed'=> [qw/ & /],
  'syllabic_vowel' => [ qw/ȯi au oi e 'E "E E i I O o [oe] [0E] ü u [ue] ə ē ā ī œ a A ä [a']/],
  'unsyllabic_consonant' => [ qw/b ch d f g h j k [k] l m n [n] p r s sh t th [th] v W w ŋ z/],
  'compound_unsyllabic' => [ qw/hw [ng]/ ],
};
print $fh encode_json($rules);
close($fh);
