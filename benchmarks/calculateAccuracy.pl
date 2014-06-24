#!/usr/bin/perl
use File::Slurp;
use Data::Dumper;
my $filename = $ARGV[0] || "first_benchmark.results";
my @lines = read_file($filename);
my $total = scalar(@lines);
my $accuracy = {
  vc_plain => {
    accurate => 0,
    speediest => 0,
    accuracy_percentage => 0,
    speediest_percentage => 0,
    lone_accuracy_count => 0

  },
  vc_accented => {
    accurate => 0,
    speediest => 0,
    accuracy_percentage => 0,
    speediest_percentage => 0,
    lone_accuracy_count => 0
  },
  trouvain => {
    accurate => 0,
    speediest => 0,
    accuracy_percentage => 0,
    speediest_percentage => 0,
    lone_accuracy_count => 0
  },
};
my $vc_plain_data = {
  lone_accurate_words => []
};
my $vc_accented_data = {
  lone_accurate_words => []
};
my $trouvain_data = {
  lone_accurate_words => []
};
foreach my $line (@lines){
  chomp($line);
  my @parts = split(/\t/, $line);
  
  my ($word, $vc_plain, $vc_accented, $trouvain, $speediest) = @parts;
  if ($vc_plain){
    $accuracy->{vc_plain}->{accurate} ++;
  }
  if ($vc_accented){
    $accuracy->{vc_accented}->{accurate} ++;
  }
  if ($trouvain){
    $accuracy->{trouvain}->{accurate} ++;
  }
  if ($speediest =~ /vc_plain/){
    $accuracy->{vc_plain}->{speediest} ++;
    
  }
  if ($speediest =~ /vc_accented/){
    $accuracy->{vc_accented}->{speediest} ++;
    
  }
  if ($speediest =~ /trouvain/){
    $accuracy->{trouvain}->{speediest} ++;
    
  }
  if ($vc_plain && ! $vc_accented && ! $trouvain){
    $accuracy->{vc_plain}->{lone_accuracy_count} ++;
    push(@{$vc_plain_data->{lone_accurate_words}}, $word);
  }
  if ($vc_accented && ! $vc_plain && ! $trouvain){
    $accuracy->{vc_accented}->{lone_accuracy_count} ++;
    push(@{$vc_accented_data->{lone_accurate_words}}, $word);

  }
  if ($trouvain && ! $vc_accented && ! $vc_plain){
    $accuracy->{trouvain}->{lone_accuracy_count} ++;
    push(@{$trouvain_data->{lone_accurate_words}}, $word);
  }
}


$accuracy->{vc_plain}->{accuracy_percentage} = $accuracy->{vc_plain}->{accurate} / $total;
$accuracy->{vc_accented}->{accuracy_percentage} = $accuracy->{vc_accented}->{accurate} / $total;
$accuracy->{trouvain}->{accuracy_percentage} = $accuracy->{trouvain}->{accurate} / $total;

$accuracy->{vc_plain}->{speediest_percentage} = $accuracy->{vc_plain}->{speediest} / $total;
$accuracy->{vc_accented}->{speediest_percentage} = $accuracy->{vc_accented}->{speediest} / $total;
$accuracy->{trouvain}->{speediest_percentage} = $accuracy->{trouvain}->{speediest} / $total;
print Dumper $accuracy;
#print Dumper $vc_accented_data;
