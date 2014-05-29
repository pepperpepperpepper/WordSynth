#!/usr/bin/perl
use Data::Dumper;
use File::Slurp;
use JSON;
use LWP::UserAgent; 
use Encode qw/decode encode/;
use utf8;
use Exporter qw(import);

our @EXPORT_OK = qw(merriamSimpleSearch);
sub merriamSimpleSearch{
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
  my $syll_map = { 
    "string" => "",
    "position" => []
  };

  my $current_position = 0;
  return $syll_string;
}
#print Dumper merriamSimpleSearch($ARGV[0]);
1;
