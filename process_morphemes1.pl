#!/usr/bin/perl
use File::Slurp;
use Data::Dumper;
use JSON;
my $filename = $ARGV[0] || 'morphemes1';
my @lines = read_file($filename);
chomp(@lines);
@lines = map { my $data = $_;
  $data =~ m/^([^\s]+)\s+([^,]+).+\s([^\s]+),?\s,?([^\s]+)\s*$/;
  my $morpheme = $1;
  my $explanation = $2;
  my $example = $3;
  my $example2 = $4;
  $example =~ s/,//g;
  $example2 =~ s/,//g;
  $morpheme =~ s/,//g;
  my $type = 0;
  if ($morpheme =~ /^-/){
    $type = "suffix";
  }elsif($morpheme =~ /-$/){
    $type = "prefix";
  };
  $morpheme =~ s/-//g;
  { 
  morpheme => $morpheme,
  explanation => $explanation,
  examples => [ $example,
    $example2 ],
  type => $type
  };
} @lines;
#ask anton
#@lines = grep {
#  my $obj = $_;
#  $obj->{morpheme} =~ $obj->{examples}->[0] || $obj->{morpheme} =~ $obj->{examples}->[1]
#} @lines;


#print Dumper @lines;
print encode_json(\@lines);
