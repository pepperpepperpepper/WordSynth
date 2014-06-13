#!/usr/bin/perl
use File::Slurp;
use Data::Dumper;
use JSON;
use Array::Utils qw(:all);




#if ( array_diff(@$list1, @$list2) ) {
$Data::Dumper::Maxdepth->{120};
my @lines = read_file('SCRAPE_RESULTS/all_results');


my @parts;
my $pattern, $to_push;
my $db_hash = {};
my @positions;
my $pushed = 0; 
foreach my $line(@lines){
  @parts = split(/\t/, $line);#values aren't getting lost here...
  $pattern = $parts[1];
  @positions = split(/,/, $parts[2]); # and they lost exactly here actually
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
          positions => [ @positions ],  # like this it will work
        }
      );
    }
  }else{ #create new
    $db_hash->{$pattern} = [];
    push(@{$db_hash->{$pattern}}, 
      {
        count => 1, 
        positions => [ @positions ]
      }
    );
  }
};
foreach my $k (keys %$db_hash){
  my $arr = $db_hash->{$k};
  my @new_arr = sort {$b->{count} <=> $a->{count} } @{$arr};
  $db_hash->{$k} = \@new_arr;
}
#write to file...
open(DATA, ">syllablesdb2.json") or die "Couldn't open file syllables.json, $!";

my $json_string =  encode_json($db_hash);
#print Dumper $json_string;
print DATA $json_string;
close(DATA);

#print Dumper $db_hash->{$test}->[0];
#print scalar (keys %$db_hash);
#print Dumper $db_hash;
