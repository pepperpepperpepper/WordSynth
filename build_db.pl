#!/usr/bin/perl
use File::Slurp;
use Data::Dumper;
use JSON;
use Array::Utils qw(:all);
#if ( array_diff(@$list1, @$list2) ) {
$Data::Dumper::Maxdepth->{120};
my @lines = read_file('all_results');
my $test = "VCCCCVCVCCVCVC";

my @parts;
my $pattern, $to_push;
my $db_hash = {};
my $pushed = 0; #ask about this

foreach my $line(@lines){
  @parts = split(/\t/, $line);
  $pattern = $parts[1];
  my @positions = split(/,/, $parts[2]);
  $to_push = \@positions;

  if (exists $db_hash->{$pattern}){
    $pushed = 0;
    foreach my $elem (@{$db_hash->{$pattern}}){
      if (!array_diff(@{$elem->{positions}}, @positions)){
        $elem->{count} += 1;
        $pushed = 1;
        last;
      };
    }
    if (! $pushed){
      push(@{$db_hash->{$pattern}},
        {
          count => 1, 
          positions => \@positions
        }
      );
    }
  }else{ #create new
    $db_hash->{$pattern} = [];
    push(@{$db_hash->{$pattern}}, 
      {
        count => 1, 
        positions => \@positions
      }
      
    );
  }

};

open(DATA, ">syllablesdb.json") or die "Couldn't open file syllables.json, $!";

my $json_string =  encode_json($db_hash);
print DATA $json_string;
close(DATA);
#print Dumper $db_hash->{$test}->[0];
#print scalar (keys %$db_hash);
#print Dumper $db_hash;
