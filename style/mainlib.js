var get_dictionary = function( word, definition ) {
  // console.log(word);
  var url = '';
  if ( typeof definition !== 'undefined' && definition !== '' ) {
    url = 'dictionary_word_sound_wrapper.py?word=' + word + '&definition=' + definition;
  } else {
    url = 'dictionary_word_sound_wrapper.py?word=' + word;
  }

  // console.log(url);
  $.get( url, function (response) {
    // console.log( response );
    $( '#sound' ).html( response.word_sound );
    var word_detail = '<h2 class="word">' + response.word + '</h2>' +
    '<div class="pronunciation">' + response.word_pronunciation + '</div>' +
    '<div class="definition">' + response.word_definition + '</div>';
    $( '#word-detail-content' ).html( word_detail );
  });
};

var search_word = function( eventObject ) {
  eventObject.preventDefault();
  var word = $( '#search-word' ).val();
  var definition = $( '#search-definition' ).val();
  $( '#search-word' ).select();
  $( '#search-definition' ).val('#definition');
  get_dictionary(word, definition);

  var word_html = '<dt><a class="word" href="#' + word + '">' + word + '</a></dt>';
  word_html += '<dd>' + definition + '</dd>'
  $( '#word-list' ).prepend( word_html );
};
