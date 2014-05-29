#!/usr/bin/perl
use Data::Dumper;
use File::Slurp;
use utf8;


#my @word_list = (
#'mama',
#'papa',
#'tuesday',
#'wednesday',
#'thursday',
#'friday',
#'everyday',
#'people',
#'gotta',
#'rule',
#'la',
#'work',
#'worldliness'
#);
sub merriamSyllables{
  my $word = shift;
  my $search = `curl "http://www.merriam-webster.com/dictionary/$word"`;
  my @lines = split(/\n/, $search);
  my @lines = grep(/class="pr"/, @lines);
  if (! @lines){
    print STDERR "can't look this up in webster dictionary\n";
    return 0;
  }
  my $line = @lines[0];
  $line =~ /class="pr"(.*)/;
  $line = $1;
  my @matches = ($line =~ />([^<]+)</ig);
  my $syll_string = join('', @matches);
  my $syll_string = ($syll_string =~ m/\\(.*)\\/)[0];
  my $syll_string = ($syll_string =~ m/(^[^,]+).*/)[0];
#  2cc == ˌ  #FIXME THIS IS MESSED UP
#  e4  == ä
#  28 == (
#  29 == )
#  my $syll_string =~ s/\x{28}//g; #take out optional punctuation elements
  $syll_string =~ s/[\x{28}\x{29}]//g;
  print Dumper $syll_string; 
  if ($syll_string =~ m/\x{e4}/){
    print "howdy\n";
  }
  
  my @syllables = split(/[-\x{cb}\x{8c}\x{88}]/, $syll_string);
  my @syllables = grep {/\S/} @syllables;
  my $problem =  substr($syllables[0], 1, 2);
  return \@syllables;
}

print Dumper merriamSyllables($ARGV[0]);



#my $rules = {
# 'syllable' => /'"-ˌ/,
# 'optional' => /()/, #not using
# 'variant' => /,;÷/, #not using
# 'unstressed'=> /&/,
# 'syllabic_vowel' => a,A, ä,[a'],au,e,'E,"E,E,i,I,O,o,[oe],[0E],oi,ü,u,[ue],
# 'unsyllabic_consonant' =>b, ch, d ,f,g,h,j,k, [k],l,m,n,[n],p,r,s,sh,t,th,[th],v,W
# 'compound_unsyllabic' = > hw,[ng]
#}
