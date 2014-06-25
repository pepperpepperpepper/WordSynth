if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}

function updateProgress(percent){
  $("div.progress").removeClass("dontshowme");
  $("span.progress-help").removeClass("dontshowme");
  $("span#progress-percent").html(percent.toString());
  $("div.progress-bar").width(percent + "%");
  return false; 
}
function hideProgress(){
  $("div.progress").addClass("dontshowme");
  $("span.progress-help").addClass("dontshowme");
  $("div.progress-bar").width("0%");
  $("span#progress-percent").html('0');
  return false;
}

function makeTableRow(original_word, header_name, data_string, class_name){
    var to_print = "<tr class=\"{0}\"> <th>{1}</th><th>{2}</th><th>{3}</th>".format(
      class_name,
      original_word,
      header_name,
      data_string)
   to_print += "</tr>"
   return to_print;
}

function formatWordResult(original_words, syllabized_words){
  $("table.results").removeClass("dontshowme");
  for (i in syllabized_words){
  
    console.log(original_words[i]);
    var newrows = [
      
      makeTableRow(original_words[i], "Merriam Webster", syllabized_words[i]["presyllabizedWords"],"presyllabizedWords"),
      makeTableRow(original_words[i], "Simple Scripted Rules", syllabized_words[i]["trouvain"],"trouvain"),
      makeTableRow(original_words[i], "Computer Learning 1",    syllabized_words[i]["syllabizeLearning"],"syllabizeLearning"),
      makeTableRow(original_words[i], "Computer Learning 2",    syllabized_words[i]["syllabizeLearning_withaccent"],"syllabizeLearning_withaccent"),
    ]
    newrows.forEach(function(newrow){
      $("table.results > tbody").append(newrow);
    });

  };
  return false;
}

function processLyrics(lyrics){
  var request = $.ajax({
    url: "/processSyllables",
    type: "POST",
    data: { 'lyrics' : lyrics },
    dataType: "json"
  });
  
  request.done(function( resp ) {
    console.log(resp);

    var original_words = lyrics.split(/\s/);

    formatWordResult(original_words, JSON.parse(resp.syllabized_words));
    
  });
  
  request.fail(function( jqXHR, textStatus ) {
    alert( "Request failed: " + textStatus );
  });
}
$(document).ready(function(){
  var table_header = $("table.results > tbody").html();

  $( "form.lyrics" ).submit(function( event ) {
    var textarea = $("textarea.lyrics-test");
    var text = textarea.val();
    $("table.results > tbody").html(table_header)
    processLyrics(text);
    event.preventDefault();
  });
});
