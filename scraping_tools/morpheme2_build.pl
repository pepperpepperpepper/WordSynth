#!/usr/bin/perl
use File::Slurp;
use Data::Dumper;
my $filename = "morphemes2";
my $page = `curl http://www.prefixsuffix.com/rootchart.php?navblks=1011000`;
my @lines = grep{/abs/} split(/\n/, $page);
my $table = $lines[0];
my @parts = grep{/\S/} split(/<\/?td\/?>/, $table);
my $morpheme_list = [];
for (my $i = 0; $i < scalar(@parts); $i++){
  if ($parts[$i] =~ /class=/){
    my $morpheme_data = {
        morpheme => $parts[($i+1)],
        explanation => $parts[($i+2)],
        examples => $parts[($i+3)]
    };
    if ($morpheme_data->{morpheme} =~ m/^\s?\-/){
      $morpheme_data->{morpheme_type} = "suffix";
    };
    push (@$morpheme_list, $morpheme_data);
  }
}
#printing
foreach my $morpheme_data (@$morpheme_list){
  my $to_print = sprintf("%s\t%s\t%s\t%s\n", 
    $morpheme_data->{morpheme},
    $morpheme_data->{explanation},
    $morpheme_data->{examples},
    $morpheme_data->{morpheme_type} || "");
    append_file($filename, $to_print);
}
print Dumper $morpheme_list;
