$( document ).ready(function() {
  $( 'body' ).on('click', 'a', function( eventObject ) {
    eventObject.preventDefault();
    var element = $( this );
    word = element.html();
    get_dictionary(word);
  }); // End $( 'body' ).on('click ...
});
