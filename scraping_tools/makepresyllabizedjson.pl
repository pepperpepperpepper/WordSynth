#!/usr/bin/env perl

use File::Slurp;
use Data::Dumper;
use JSON;
my $filename = "presyllabized_words.json";
my @lines = read_file("presyllabized");
my $presyllabized_hash = {};

foreach my $line(@lines){
  chomp($line);
  my ($word, $positions) = split("\t", $line);
  my @positions_arr = split(/,/, $positions);
  $presyllabized_hash->{$word} = \@positions_arr;

}
open F, ">$filename" or die $!;
print Dumper encode_json($presyllabized_hash);
print F encode_json($presyllabized_hash);

close(F);
