$( document ).ready(function() {
  $( 'body' ).on('click', 'a.word', function( eventObject ) {
    eventObject.preventDefault();
    var element = $( this );
    var word = element.html();
    get_dictionary(word);
  }); // End $( 'body' ).on('click', 'a' ...

  $( 'body' ).on('click', 'p span', function( eventObject ) {
    eventObject.preventDefault();
    var element = $( this );
    var word = element.html();
    get_dictionary(word);
  }); // End $( 'body' ).on('click', 'span' ...

  $( 'body' ).on('click', 'span.learned-word, span.unlearned-word', function( e ) {
    e.preventDefault();
    var element = $( this );
    var class_args = element.attr('class').split(' ');
    var word_number = class_args[0];
    var word = class_args[1];
    var action = element.html();
    var filename = get_url_parameter_by_name('title');
    update_vocabulary_list(word_number, word, action, filename);
    element.parent().attr('class', 'removed');
    element.parent().next().attr('class', 'removed');
  }); // End span.learned-word and span.unlearned-word click

  // When the vocabular learn page is loaded, get the list of vocabulary
  // create a overlay to represent a flashcard, and load the vocabulary
  // one by one with certain seconds of delay. Each word will be shown width
  // pronunciation and definiton.
  // Either all words have gone through once or the cancel button is clicked
  // The flashcard will disappear and the regular list will come back
  var flashcards = function() {
    var word_list = $( '#word-list' ),
        start_flashcard_button = $( '#start-flashcard' ),
        flashcards_div = $( '#flashcards' ),
        word_flashcard = $( '#word-flashcard' );
    flashcard_started();
    var word_list_content = word_list.children().toArray();
    var random_word_list_content;
    // TODO: build randomization in the flashcard

    var flashcard_interval = 6000; // 6 seconds
    next_word();
    var start_flashcard = setInterval(next_word, flashcard_interval);

    $( 'body' ).on('click', '#flashcard-stop span', function() {
      clearInterval(start_flashcard);
      flashcard_done();
    });

    function next_word() {
      var word_html = word_list_content.shift();
      var word = word_html.children[0].innerHTML;
      var definition_html = word_list_content.shift();
      var flashcard_content = '<dl>' + word_html.outerHTML +
                              definition_html.outerHTML + '</dl>';
      word_flashcard.html(flashcard_content);
      get_dictionary(word)

      // If all words in the lists are done, we are good
      if (word_list_content.length === 0) {
        clearInterval(start_flashcard);
        setTimeout(flashcard_done, flashcard_interval);
      }
    };

    function flashcard_started() {
      flashcards_div.show();
      word_list.hide();
      start_flashcard_button.hide();
    };

    function flashcard_done() {
      flashcards_div.hide();
      word_list.show();
      start_flashcard_button.show();
    };
  };

  if ( $( '#word-flashcard' ) ) {
    flashcards();
  }

  $( 'body' ).on('click', '#start-flashcard span', function() {
    flashcards();
  })
});
