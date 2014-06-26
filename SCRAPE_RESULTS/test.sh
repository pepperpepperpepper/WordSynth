#!/bin/bash
rm results.out;
cat TEST_WORDS | while read a; do perl search.pl "$a"; done;
