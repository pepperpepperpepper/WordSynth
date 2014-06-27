#!/usr/bin/env node
//wrapper around the phonemes script
//
var test_string = process.argv[2] || 'test';  //'_s1AXrpIHkOW.';
var Promise = require("bluebird");
var childProcess = require("child_process");
function dumper(content){
  console.log(JSON.stringify(content));
}
function execute(cmd){                                                                                                         
  var promise = Promise.pending();
  var result = {};                                                                                                                
  var sh = childProcess.exec(cmd, function(error, stdout, stderr){                                                                     
//    console.log(stdout)
    result.stdout = stdout;                                                                                                   
    result.stderr = stderr;
    result.error = error;
    promise.fulfill(result);                                                                                                  
  });                                                                                                                          
//  sh.on("exit", function(){                                                                                         
//    console.log(result.stdout)
//  });                                                                                                                          
  return promise.promise                                                                                                    
}                                                                                                                              

//execute("echo bitches").then(function(result){ dumper(result) });
//DO NOT USE sh.on


function phonemes(word, callback){
  var phonemes;
  word = word.replace(/"/,"");
  execute("phonemes \""+word+"\"")
    .then(function(result) {
//  dumper(result)
    phonemes = result.stdout;
    callback(phonemes);
  });
}
var main = function(){
  phonemes(test_string, console.log);

}

if (require.main === module) {
    main();
}

module.exports = phonemes;
