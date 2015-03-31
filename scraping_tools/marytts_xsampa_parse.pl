#!/usr/bin/perl 
use utf8;
use JSON;
use File::Slurp;
use Data::Dumper;
use Cwd 'abs_path';
use File::Basename;
use HTML::Entities;
use Text::Unidecode;

my $OUTFILE = "marytts_xsampa_char_data.json";
my @lines = read_file(dirname(abs_path($0)).'/xsampa');
my $chars = {};
for ( my $i = 0; $i < @lines; $i++ ) {
  if ($lines[$i] =~ m@<tt@){ 
    $lines[$i] =~ m@>([^<]+)<@g;
    my $char = unidecode(decode_entities($1));
    $lines[$i + 3] =~ m@>([^<]+)<@;
    my $description = $1;
    my $data = { symbol => $char, description => $description };
    if ($description =~ m/vowel|schwa/i){
      $data->{type} = "PHONEME";
      $data->{phoneme_type} = 'V'; 
    }elsif($description =~ m/(?:fricative|plosive|trill|approximant|alveolar|nasal
      |glottal|click|dental|flap|velarized)/ix){
      $data->{type} = "PHONEME";
      $data->{phoneme_type} = 'C'; 
    }elsif($description =~ m/(?:tone|root|voice|step|group|long|stress|palat|aspirat|round|short|labial
      |laminal|raise|rise|lower|fall|lateral|audible|central|apical|ejective|pharyn|retract|primary|rhotac
      |linking|advanced)/xi){
      $data->{type} = "PROSODIC_CONTROL";
    }else{
      $data->{type} = "OTHER";
    };
    $chars->{$char} = $data;
    $i += 4;
  }
}
write_file($OUTFILE, JSON->new->utf8(1)->encode($chars))

