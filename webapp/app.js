#!/usr/bin/env node
//this is for express3
var express = require('express');
var execSync = require('exec-sync'); 
var app = express();
//{{{config
app.enable('trust proxy'); //for nginx
var bodyParser = require('body-parser');
app.use(express.logger('dev'));
app.use(express.bodyParser());
app.set('views', __dirname + '/views');
app.use("/js", express.static(__dirname + '/views/js'));
app.use("/css", express.static(__dirname + '/views/css'));
app.engine('html', require('ejs').renderFile);
//}}}

//{{{ routes
app.get('/template', function (req, res)
{
    res.render('template.html');
});
app.get('/syllables', function(req, res){
  res.render('syllables.html');
});

app.get('/tokens/:word', function(req, res){
  res.send(sendTokens(decodeURIComponent(req.param('word'))))
})

app.get('/phonemes/:word', function(req, res){
  var word = sanitize(decodeURIComponent(req.param('word')))
  res.send(sendPhonemes(word))
})

app.get('/', function(req, res){
  res.send('WHAAAATUPPPPP');
});

//}}}

var trouvain = require("../lib/trouvain.js");
var syllabizeLearning = require("../lib/syllabizeLearning.js");
var syllabizeLearning_withaccent = require("../lib/syllabizeLearning_withaccent.js");
var tokenizer = require("../lib/tokenizer.js");
var idxToHyphen = require("../lib/idxToHyphen.js");

function sanitize(s){
  s.replace(/[^\w\s\-']/gi, '')
  return s
}

function sendPhonemes(w){
  return execSync('phonemes \"'+w+'\"');
}

function sendTokens(s){
  var tokens_arr = []
  var words = s.split(/\s/)
  words.filter(function(w){
    if(w)
      return w;
  } )
  words = words.map(function(word){
    return tokenizer(word)
  })
  return JSON.stringify(words)
}

function processLyrics(lyrics){
  var presyllabizedWords = require("../lib/presyllabizedWords.js");
  var lyrics = lyrics.split(/\s/);
  //remove empties
  lyrics.filter(function(l) { 
    if (l){
      return l;
    }
  });
  lyrics = lyrics.map(function(word){
    var tokens = tokenizer(word);
    return { 
      presyllabizedWords : idxToHyphen(tokens, presyllabizedWords(word)),
      trouvain : idxToHyphen(tokens, trouvain(tokens)),
      syllabizeLearning : idxToHyphen(tokens, syllabizeLearning(tokens)),
      syllabizeLearning_withaccent : idxToHyphen(tokens, syllabizeLearning_withaccent(tokens))
    }
  });
  return JSON.stringify(lyrics);
}



app.post('/processSyllables', function (req, res)
{
  //req.body, req.query, req.params
  var lyrics = req.body.lyrics;
  if (! lyrics){
    res.send(200, { newlyrics: '{}' });
  }else{
//    console.log(req.body.lyrics);
    res.send(200, { syllabized_words: processLyrics(lyrics) });
  }
});

var server = app.listen(3333, function() {
    console.log('Listening on port %d', server.address().port);
});
