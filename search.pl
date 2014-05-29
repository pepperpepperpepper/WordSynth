#!/usr/bin/perl
use Data::Dumper;
use File::Slurp;
use JSON;
use LWP::UserAgent; #should I be using this? or LWP::UserAgent; or something
use Encode qw/decode encode/;
use utf8;

our $rules = get_regexp();

sub merriamSyllables{
  my $word = shift;
#  my $search = `curl "http://www.merriam-webster.com/dictionary/$word"`;
  my $ua = LWP::UserAgent->new();
  my $res = $ua->get("http://www.merriam-webster.com/dictionary/$word");
  my $search = $res->decoded_content || decode("utf8", $res->content); 
  
# well rules are ready i think, input ready too, how this splitting works?
# exactly the same way as the previous script. basically long regexes in loops
# ie
# https://github.com/pepperpepperpepper/MIDINEW/blob/master/tokenizer.js
# I need to label them, I can come up with other rules once I've labeled them within the string
# does that make sense? yeah i got it
  my @lines = split(/\n/, $search);
  my @lines = grep(/class="pr"/, @lines);
  if (! @lines){
    print STDERR "can't look this up in webster dictionary\n";
    return 0;
  }
  my $line = @lines[0];
  $line =~ /class="pr"(.*)/;
  $line = $1;
  my @matches = ($line =~ />([^<]+)</ig);
  my $syll_string = join('', @matches);
  my $syll_string = ($syll_string =~ m/\\(.*)\\/)[0];
  my $syll_string = ($syll_string =~ m/(^[^,]+).*/)[0];
#  $syll_string =~ s/[\x{28}\x{29}]//g;
  print Dumper $syll_string; 
#seems to be working but not printing the named capture. is that just Data::dumper's fault? no, should work, not sure wha't wrong yet
#ok. this script in general seems like the most difficult thing I've ever tried to do
  
  while( ($syll_string =~ /$rules->{regexp}/g)){
    my $matched = [ grep { defined $+{$_} } @{ $rules->{keys} } ];
    print Dumper $1, $matched; #what does $+ mean? return named capture from regexp got it
# that's better, so $+ doesn't allow to read it as hash directly, so we have to get over all keys we have in regexp and manully query
# them. that's fine. this only has to run once. it can be slow, or whatever
# I was a bit intimidated by this particular script, because of my inexperience dealing witth unicode, particularly
# is that something that I should be more accustomed to? yeah just remeber which format and encoding you are currently using, and alway convert
# into perl's unicode then importing, and convert back to utf8 then outputing. why is perl's unicode encoding different 
# from utf8? any particular reason? becuase you can encode perl's unicode ito cp1251 or any other custom codepage, so it will be wise to
# keep internal format for it and then convert o approriate. converting unicode -> cp1251 can take an intermediary step? no just if it's in perl
# you write encode("cp1251", $string). same for utf8 or UTF-16 or any other. I see..  also decode/encode_json as well as LoadFile/DumpFile for yaml
# already converting from utf8 encoded file into perl's encoding, so you don't need to use encode/decode to convert it again.
# ok so when I type
# my $string = "hello";
# in perl, is that string ascii or perl's unicode? then it's written as file, it's in ascii, then perl executing it, it will convert source
# code into perl's unicode, and this string in runtime will be in perl's unicode. interesting ok I get it
# quotemeta...what is a meta character? any charater which we use to control regexp behaviour, like () or [] groups.
# ok cool.
# well this is definitely a big help. I'm going to try to write the learning function and run this against some wordlists thanks a lot
#  no problems
#
  }
}

sub rules_to_regexp {
  my ($rules_array) = @_;
  
  return join "|", map {
    quotemeta($_)
  } @$rules_array;
}

sub get_regexp {
  my $json_string = read_file('rules.json');
  my $rules = decode_json($json_string);
  my $regexps = {
    map {
      $_ => rules_to_regexp($rules->{$_})
    } keys %$rules
  };
  my $global_regexp = "(". (join "|", map {
    sprintf("(?<%s>%s)", $_, $regexps->{$_})
  } keys %$regexps ) . ")";
  return {
    keys   => [ keys %$rules ],
    regexp => $global_regexp
  };
}

#so what now? now we need to get all input into perl's unicode. i'm not sure how this curl + perl's `` get encoding, but most likely 
#input will be just plain binary data, without decodeing. proper way of downloading will be with lwp and HTTP::Response->decoded_content method.
#
#as for now we can try quickly fix with with decode("utf8", $search), should work too if page in utf8.
#it's just a get request. I can use lwp, I just was trying to write it quickly ok
print Dumper merriamSyllables($ARGV[0]);

