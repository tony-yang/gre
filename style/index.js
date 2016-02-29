$( document ).ready(function() {
  $( 'body' ).on('click', 'a.word', function( eventObject ) {
    eventObject.preventDefault();
    var element = $( this );
    word = element.html();
    get_dictionary(word);
  }); // End $( 'body' ).on('click ...

  $( '#search' ).click(function( eventObject ) {
    search_word(eventObject);
  }); // End $( '#search' ).click

  $( '.input' ).keypress(function( eventObject ) {
    if (eventObject.which == 13) {
      search_word(eventObject);
    }
  }); // End $( '.input' ).keypress

  $( 'body' ).click(function( e ) {
    $( '#search-word' ).select();
  }); // End $( 'body' ).click
});
