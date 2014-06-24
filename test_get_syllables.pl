#!/usr/bin/env perl
use JSON;
use Data::Dumper;
my $VCString = $ARGV[0];

$VCString =~ s/[^VC]//g;
my $filename = 'syllablesdb.json';

my $json_text = do {
   open(my $json_fh, "<:encoding(UTF-8)", $filename)
      or die("Can't open \$filename\": $!\n");
   local $/;
   <$json_fh>
};

my $json = JSON->new;
my $syllablesdb = $json->decode($json_text);
print $VCString . "\n";
print  join(",", @{$syllablesdb->{$VCString}[0]->{positions}}). "\n";

