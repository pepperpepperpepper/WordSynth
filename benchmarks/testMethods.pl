#!/usr/bin/perl
use Data::Dumper;
use File::Slurp;
use JSON;

my $word = $ARGV[0] || "example";
chomp($word);

our $testdir = "tests";

sub testMethod {
  my $method_command = shift;
  my $word = shift;
  my $cmd = sprintf("%s %s", $method_command, $word);
  my $result = `time $cmd 2>&1`;
  $result =~ s/\'//g;
  @results = split('\n', $result);
  chomp @results;
  my $positions = $results[0];
  my $time_info = $results[1];
  my @times = grep { /\S/ } split(/\s+/, $time_info);
  return $times[0], $results[0];
#  my @output = ($times[0], $results[0]);
#  return \@output;
  
}

sub testKnownWords{
  my $word = shift;
  my $cmd = "node ./$testdir/testKnownWords.js";
  return testMethod($cmd, $word);
}

sub testVCStringPlain{
  my $word = shift;
  my $cmd = "node ./$testdir/testSyllabizeLearning.js";
  return testMethod($cmd, $word);
}

sub testVCStringAccented{
  my $word = shift;
  my $cmd = "node ./$testdir/testSyllabizeLearning_withaccent.js";
  return testMethod($cmd, $word);
}


sub testTrouvain{
  my $word = shift;
  my $cmd = "node ./$testdir/testTrouvain.js";
  return testMethod($cmd, $word);
}

sub main{
  my @known_words_test = testKnownWords $word;
  my @vcstring_plain_test = testVCStringPlain $word;
  my @vcstring_accented_test =  testVCStringAccented $word;
  my @test_trouvain_test = testTrouvain $word;

  #NOTE: you don't have to convert types because they are all strings
  #print results in tab delineated form
  #if ! $known_words_test[1] do not print
  #vcstring_plain_accuracy\tvcstring_accented_accuracy\ttrouvain_accuracy\tfastest
  #
  my @analysis = ();
  if (! $known_words_test[1] || ($known_words_test[1] =~ /false/)){
    return;
  }
  if ($vcstring_plain_test[1] eq $known_words_test[1]){
    push(@analysis, 1);
  }else{
    push(@analysis, 0);
  }

  if ($vcstring_accented_test[1] eq $known_words_test[1]){
    push(@analysis, 1);
  }else{
    push(@analysis, 0);
  }


  if ($test_trouvain_test[1] eq $known_words_test[1]){
    push(@analysis, 1);
  }else{
    push(@analysis, 0);
  }
  my $speediest = "vc_plain";
  if ($vcstring_accented_test[0] < $vcstring_plain_test[0]){
    $speediest = "vcstring_accented";
  }elsif($test_trouvain_test[0] < $vcstring_plain_test[0]){
    $speediest = "trouvain";
  }
  push (@analysis, $speediest);
  my $to_print = sprintf("%s\t%s\t%s\t%s\t%s\n", $word, @analysis);
  print  $to_print;
}
main();
