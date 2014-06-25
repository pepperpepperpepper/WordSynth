#!/usr/bin/env node
//this is for express3
var express = require('express');
var app = express();
app.enable('trust proxy'); //for nginx
var bodyParser = require('body-parser');


//var lyricsSyllabizer = require("lyricsSyllabizer.js");

//app.use(app.router);
//{{{
app.use(express.logger('dev'));

app.use(express.bodyParser());


app.set('views', __dirname + '/views');
app.use("/js", express.static(__dirname + '/views/js'));
app.use("/css", express.static(__dirname + '/views/css'));
//app.set('js', __dirname + '/views/js');
app.engine('html', require('ejs').renderFile);


app.get('/template', function (req, res)
{
    res.render('template.html');
});

app.get('/test', function (req, res)
{
    res.render('test.html');
});

app.get('/syllables', function(req, res){
  res.render('syllables.html');
});

app.get('/', function(req, res){
  res.send('WHAAAATUPPPPP');
});

//}}}


var presyllabizedWords = require("../presyllabizedWords.js");
var trouvain = require("../trouvain.js");
var syllabizeLearning = require("../syllabizeLearning.js");
var syllabizeLearning_withaccent = require("../syllabizeLearning_withaccent.js");
var tokenizer = require("../tokenizer.js");
var idxToHyphen = require("../idxToHyphen.js");

function processLyrics(lyrics){
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
//      presyllabizedWords : idxToHyphen(presyllabizedWords(word)),
//      trouvain : idxToHyphen(trouvain(word)),
//      syllabizeLearning : idxToHyphen(syllabizeLearning(word)),
//      syllabizeLearning_withaccent : idxToHyphen(syllabizeLearning_withaccent(word))
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
//  console.log("this is param", req.param);
//  console.log(req.param("data"));
//  console.log(req.params);
  var lyrics = req.body.lyrics;
  if (! lyrics){
    res.send(200, { newlyrics: '{}' });
  }else{
    console.log(req.body.lyrics);
  //  console.log(req.query);
    res.send(200, { syllabized_words: processLyrics(lyrics) });
  }
});

var server = app.listen(3333, function() {
    console.log('Listening on port %d', server.address().port);
});
