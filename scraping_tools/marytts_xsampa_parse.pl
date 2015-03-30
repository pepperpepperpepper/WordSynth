#!/usr/bin/perl 
use JSON;
use File::Slurp;
use Data::Dumper;
my @lines = read_file('xsampa');
my $chars = [];
for ( my $i = 0; $i < @lines; $i++ ) {
  if ($lines[$i] =~ m@<tt@){ 
    $lines[$i] =~ m@>([^<]+)<@g;
    my $char = $1;
    $char =~ s/&lt;/</g;
    $char =~ s/&gt;/>/g;
    $lines[$i + 3] =~ m@>([^<]+)<@;
    my $description = $1;
    my $data = { symbol => $char, description => $description };
    if ($description =~ m/vowel|schwa/i){
      $data->{type} = "PHONEME";
      $data->{phoneme_type} = 'V'; 
    }elsif($description =~ m/(?:fricative|plosive|trill|approximant|alveolar|nasal)/i){
      $data->{type} = "PHONEME";
      $data->{phoneme_type} = 'C'; 
    }else{ 
    };

  
    push(@$chars , $data);
    $i += 4;
  }
}
print Dumper $chars;
