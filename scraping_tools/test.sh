#!/bin/bash
if [ -e test.out ]; then 
  rm test.out;
fi;
cat CORNCOB |
  while read a; do 
    b=$(phonemes "$a"); 
    c=$(node createVCString.js "$a"); 
    echo "$a""\t""$b""\t""$c" |
      tee -a test.out; done
