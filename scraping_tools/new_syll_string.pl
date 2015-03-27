#!/usr/bin/perl
use Data::Dumper;
use JSON;
use File::Slurp;
use utf8;
our $syll_string = $ARGV[0] || 'ˈärd-ˌvärk';

our $rules = get_regexp();
sub rules_to_regexp {
  my ($rules_array) = @_;
  
  return join "|", map {
    quotemeta($_)
  } @$rules_array;
}

sub get_regexp {
  my $json_string = read_file('rules.json');
  my $rules = decode_json($json_string);
  my $regexps = {
    map {
      $_ => rules_to_regexp($rules->{$_})
    } keys %$rules
  };
  my $global_regexp = "(". (join "|", map {
    sprintf("(?<%s>%s)", $_, $regexps->{$_})
  } keys %$regexps ) . ")";
  return {
    keys   => [ keys %$rules ],
    regexp => $global_regexp
  };
}

sub make_new_VCstring{
  my $syll_string = shift;
  my $syll_map = { 
    "string" => "",
    "position" => [0]
  };
  my $current_position = 0;
  my $stressed_vowel = 0;
  while( ($syll_string =~ /$rules->{regexp}/g)){
    my $matched = [ grep { defined $+{$_} } @{ $rules->{keys} } ];
    if ($matched->[0] eq 'syllable' || $matched->[0] eq 'stressed'){
      $stressed_vowel = ($matched->[0] eq 'stressed') ? 1 : 0;
      if ($current_position && $syll_map->{position}->[-1] != $current_position){
        push (@{$syll_map->{position}}, $current_position);
        next;
      }
    }elsif($matched->[0] eq 'syllabic_vowel'){
      if ($stressed_vowel){
        $syll_map->{string} .= '1';
        $stressed_vowel = 0;
      }
      $syll_map->{string} .= 'V'; 
      $current_position++;
    }elsif($matched->[0] eq 'unsyllabic_consonant'){
      $syll_map->{string} .= 'C'; 
      $current_position++;
    }elsif($matched->[0] eq 'compound_unsyllabic'){
      $syll_map->{string} .= 'C'; 
      $current_position++;
    }elsif($matched->[0] eq 'optional'){
      next;
    }elsif($matched->[0] eq 'variant'){
      last;
    }elsif($matched->[0] eq 'unstressed'){
      next; #fix later
    }
  }
    
  return $syll_map;
}

my $syll_map = make_new_VCstring($syll_string);
print $syll_map->{string} . "\n";
