#!/bin/bash
export NODE_MODULE_LIST="exec-sync\
 prettyjson"; 

buildMidi-json(){
  cd lib/midi-json;
  make;
  if [ $? -eq 1 ]; then
    echo "ERROR: Could not build midi-json" >&2;
    exit 1;
  fi;
  cd ../../;
  if [ -e bin/midi-json ]; then unlink bin/midi-json; fi; 
  ln -s ../lib/midi-json/midi-json bin/midi-json;
  if [ $? -eq 1 ]; then
    echo "ERROR: Could not link midi-json" >&2;
    exit 1;
  fi;
}
installNodeModules(){
  for i in $NODE_MODULE_LIST; do
    npm install $i; 
  done;

}

buildMidi-json;
installNodeModules;
