#!/usr/bin/env node
//this is for express3
var express = require('express');
var app = express();
app.enable('trust proxy'); //for nginx

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
var server = app.listen(3333, function() {
    console.log('Listening on port %d', server.address().port);
});
