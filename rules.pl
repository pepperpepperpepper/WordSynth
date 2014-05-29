use JSON;
use utf8;
#my $rules = {
# 'syllable' => /'"-/,
# 'optional' => /()/, #not using
# 'variant' => /,;÷/, #not using
# 'unstressed'=> /&/,
# 'syllabic_vowel' => a,A, ä,[a'],au,e,'E,"E,E,i,I,O,o,[oe],[0E],oi,ü,u,[ue],
# 'unsyllabic_consonant' =>b, ch, d ,f,g,h,j,k, [k],l,m,n,[n],p,r,s,sh,t,th,[th],v,W
# 'compound_unsyllabic' = > hw,[ng]
#
#
my $rules = {
  'syllable' => ["'", '"','-', "ˈ" ],
  'optional' => [ qw/( )/ ], #not using
  'variant' => [qw/ , ; ÷/] , #not using
  'unstressed'=> [qw/ & /],
  'syllabic_vowel' => [ qw/a A ä [a'] au e 'E "E E i I O o [oe] [0E] oi ü u [ue] ə/],
  'unsyllabic_consonant' => [ qw/b ch d f g h j k [k] l m n [n] p r s sh t th [th] v W/],
  'compound_unsyllabic' => [ qw/hw [ng]/ ],
};
#that's ok? yes
#like this? yeah, also you can write like this: and so on, just simpler
print encode_json($rules);
