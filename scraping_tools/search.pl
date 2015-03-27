#!/usr/bin/perl
use Data::Dumper;
use File::Slurp;
use JSON;
use LWP::UserAgent; 
use Encode qw/decode encode/;
use utf8;

use MerriamSimple qw(merriamSimpleSearch);
our $DEBUG = 1;

our $rules = get_regexp();

sub merriamSyllables{
  
  my $word = shift;
  $word = lc($word);
  my $ua = LWP::UserAgent->new();
  my $res = $ua->get("http://www.merriam-webster.com/dictionary/$word");
  my $search = $res->decoded_content || decode("utf8", $res->content); 
  
  my @lines = split(/\n/, $search);
  my @real = grep{/h1/} @lines;
  my $section = ($real[0] =~ />([a-zA-Z]+)</)[0];
  my @lines = grep(/class="pr"/, @lines);
  if (! @lines || $section !~ /$word/ig){
    print STDERR "can't look this up in webster dictionary\n";
    return 0;
  }
  my $line = @lines[0];
  $line =~ /class="pr"(.*)/;
  $line = $1;
  my @matches = ($line =~ />([^<]+)</ig);
  my $syll_string = join('', @matches);
  my $syll_string = ($syll_string =~ m/\\([^\s\\]+)[\s\\]/)[0];
  my $syll_string = ($syll_string =~ m/(^[^,]+).*/)[0];
  if ($syll_string =~ m/^-/){
    print STDERR "pronunciation useless due to its being incomplete\n";
    return 0;
  }
  my $syll_map = { 
    "string" => "",
    "position" => []
  };
  my $current_position = 0;
  print Dumper $syll_string;
  while( ($syll_string =~ /$rules->{regexp}/g)){
    my $matched = [ grep { defined $+{$_} } @{ $rules->{keys} } ];
    print Dumper $1, $matched; #what does $+ mean? return named capture from regexp got it
    if ($matched->[0] eq 'syllable'){
      if ($current_position && $syll_map->{position}->[-1] != $current_position){
        push (@{$syll_map->{position}}, $current_position);
        next;
      }
    }elsif($matched->[0] eq 'syllabic_vowel'){
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
    
  print Dumper $syll_map;
  return $syll_map;
}

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

sub main{
  my $word = $ARGV[0];
  my $syll_map = merriamSyllables($word);
  my $original = merriamSimpleSearch($word);
  if (!$original || !$syll_map){
    return 0;
  }
  if ($DEBUG){
    my $mac_version = `node createVCString.js $word`; 
    my $results = sprintf("%s\t%s\t%s\t%s\t%s\n", 
      $word, $syll_map->{string}, join(",", @{$syll_map->{position}}) || "0", $original, $mac_version);
    append_file('still_needed.out', $results); 
  }
}
main();
