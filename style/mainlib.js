var save_to_local_storage = function(word, response) {
  if (response.word_definition != '' && response.word_definition != 'undefined' &&
      response.word_definition != '<div class="def-content">Error Fetching Data [timed out]</div>' &&
      response.word_definition != '<div class="def-content">Error Fetching Data [HTTP Error 404: Not Found]</div>') {
        try {
          sessionStorage.setItem(word, JSON.stringify(response));
        } catch(e) {
          if (e.message.indexOf('exceeded the quota') > -1) {
            console.log(e);
            sessionStorage.clear();
            sessionStorage.setItem(word, JSON.stringify(response));
          }
        }
  }
};

var build_dictionary_cache = function(word) {
  var url = 'dictionary_word_sound_wrapper.py?word=' + word;
  if ( !sessionStorage.getItem(word) ) {
    $.get( url, function (response) {
      save_to_local_storage(word, response);
    });
  }
};

var get_dictionary = function( word, definition ) {
  var url = '';
  if ( typeof definition !== 'undefined' && (definition !== '' || definition !== '#definition') ) {
    url = 'dictionary_word_sound_wrapper.py?word=' + word + '&definition=' + definition;
  } else {
    url = 'dictionary_word_sound_wrapper.py?word=' + word;
  }

  function create_sound_and_word_detail(response) {
    $( '#sound' ).html( response.word_sound );
    var word_detail = '<h2 class="word">' + response.word + '</h2>' +
    '<div class="pronunciation">' + response.word_pronunciation + '</div>' +
    '<div class="vocabulary-com-definition">' + response.vocabulary_com_definition + '</div>' +
    '<div class="definition">' + response.word_definition + '</div>';
    $( '#word-detail-content' ).html( word_detail );
  }

  if ( sessionStorage.getItem(word) && (typeof definition == 'undefined' || definition == '' || definition == '#definition' )) {
    // console.log('Found ' + word + ' in cache');
    response = sessionStorage.getItem(word);
    create_sound_and_word_detail(JSON.parse(response));
  } else {
    $.get( url, function (response) {
      // console.log('Request ' + word + ' from remote');
      // console.log(response)
      save_to_local_storage(word, response);
      create_sound_and_word_detail(response);
    });
  }
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

var update_vocabulary_list = function( word_number, word, action, filename ) {
  var url = '';
  if ( typeof word_number !== 'undefined' || typeof word !== 'undefined' || typeof action !== 'undefined' && typeof filename !== 'undefined' ) {
    url = 'vocabulary_learning_progress.py?word=' + word + '&wordnum=' + word_number + '&action=' + action + '&filename=' + filename;
  }

  $.get( url, function (response) {
    // console.log( response );
  });
};

var get_url_parameter_by_name = function(name) {
  var parameters = window.location.search.substring(1).toLowerCase();
  var parameters_array = parameters.split('&');
  var i, parameter;

  for (i = 0; i < parameters_array.length; i++) {
    parameter = parameters_array[i].split('=');
    if (parameter[0] === name) {
      return parameter[1] === 'undefined' ? true : parameter[1];
    }
  }
};
