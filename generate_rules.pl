use JSON;
use utf8;
my $RULE_FILE = "rules.json";
open(my $fh, ">", $RULE_FILE) 
  or die "cannot open > output.txt: $!";
#http://www.merriam-webster.com/pronsymbols.html this changes shit!

my $rules = {
  'stressed' => [ "ˈ" ],
  'syllable' => ["'", '"','-'],
  'variant' => [',',';','÷','/','\s'] , #not using
  'unstressed'=> [qw/ & /],
  'syllabic_vowel' => [ qw/ȯi au au̇ oi yü e 'E "E E i I O o ō [oe] [0E] ü u̇ u [ue] ə ē ā ī œ a A ä [a']/],
  'unsyllabic_consonant' => [ qw/m(p) n(t) ch sh th th zh [th] d f g h b j k [k] l m n [n] p r s t v W w ŋ z/],
  'compound_unsyllabic' => [ qw/hw [ng]/ ],
  'optional' => [ qw/( )/ ], #not using
};
print $fh encode_json($rules);
close($fh);
