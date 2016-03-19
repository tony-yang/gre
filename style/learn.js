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
        word_counter,
        start_flashcard_button = $( '#start-flashcard' ),
        flashcards_div = $( '#flashcards' ),
        word_flashcard = $( '#word-flashcard' ),
        resume_button = $( '#flashcard-control .resume' ),
        previous_button = $( '#flashcard-control .previous' ),
        next_button = $( '#flashcard-control .next' ),
        pause_button = $( '#flashcard-control .pause' );
    flashcard_initiate();
    var word_list_content = word_list.children().toArray();
    word_list_content = word_shuffle(word_list_content);

    var flashcard_interval = 6000; // 6 seconds
    next_word();
    play_flashcard();

    var start_flashcard;
    function play_flashcard() {
      start_flashcard = setInterval(next_word, flashcard_interval);
    };

    function stop_flashcard() {
      clearInterval(start_flashcard);
    };

    $( 'body' ).on('click', '#flashcard-control .stop', function() {
      stop_flashcard();
      flashcard_done();
    });

    $( 'body' ).on('click', '#flashcard-control .pause', function() {
      stop_flashcard();
      pause_button.hide();
      resume_button.show();
      previous_button.show();
      next_button.show();
    });

    $( 'body' ).on('click', '#flashcard-control .resume', function() {
      play_flashcard();
      resume_button.hide();
      previous_button.hide();
      next_button.hide();
      pause_button.show();
    });

    $( 'body' ).on('click', '#flashcard-control .previous', function() {
      if (word_counter >= 4) {
        word_counter -= 4;
      } else if (word_counter == 2) {
        word_counter -= 2;
      }
      next_word();
    });

    $( 'body' ).on('click', '#flashcard-control .next', function() {
      next_word();
    });

    function next_word() {
      var total_word_count = word_list_content.length / 2;
      var current_word_count = word_counter / 2 + 1;
      var word_html = word_list_content[word_counter];
      console.log(word_html.outerHTML);
      word_counter += 1;
      var word = word_html.children[0].innerHTML;
      var definition_html = word_list_content[word_counter];
      console.log(definition_html.outerHTML);
      word_counter += 1;
      var flashcard_content = '<div class="word_count">Progress ' + current_word_count + '/' + total_word_count + '</div>';
      flashcard_content += '<dl>' + word_html.outerHTML +
                            definition_html.outerHTML + '</dl>';
      word_flashcard.html(flashcard_content);
      get_dictionary(word)

      // If all words in the lists are done, we are good
      if (word_list_content.length === 0) {
        clearInterval(start_flashcard);
        setTimeout(flashcard_done, flashcard_interval);
      }
    };

    function flashcard_initiate() {
      word_counter = 0;
      flashcards_div.show();
      word_list.hide();
      start_flashcard_button.hide();
    };

    function flashcard_done() {
      flashcards_div.hide();
      word_list.show();
      start_flashcard_button.show();
    };

    function word_shuffle(word_list) {
      var from_pointer = 0,
          to_pointer = Math.floor((Math.random() * word_list.length / 2)) * 2;
      var swap_counter;
      for (swap_counter = 0; swap_counter < word_list.length / 4; swap_counter++) {
        var swap_word = word_list[from_pointer];
        word_list[from_pointer] = word_list[to_pointer];
        word_list[to_pointer] = swap_word;

        var swap_definition = word_list[from_pointer + 1];
        word_list[from_pointer + 1] = word_list[to_pointer + 1];
        word_list[to_pointer + 1] = swap_definition;

        from_pointer = ((from_pointer + 1) * 2) % word_list.length;
        to_pointer = ((to_pointer + 1) * 3 - 1) % word_list.length;
      }

      return word_list;
    };
  };

  if ( $( '#word-flashcard' ).length ) {
    flashcards();
  }

  $( 'body' ).on('click', '#start-flashcard span', function() {
    flashcards();
  })
});
