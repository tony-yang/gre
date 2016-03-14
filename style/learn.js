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
  })
});
