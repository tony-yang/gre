$( document ).ready(function() {
  $( 'body' ).on('click', 'a.word', function( eventObject ) {
    eventObject.preventDefault();
    var element = $( this );
    word = element.html();
    get_dictionary(word);
  }); // End $( 'body' ).on('click', 'a' ...

  $( 'body' ).on('click', 'span', function( eventObject ) {
    eventObject.preventDefault();
    var element = $( this );
    word = element.html();
    get_dictionary(word);
  }); // End $( 'body' ).on('click', 'span' ...
});
