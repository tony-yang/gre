#!/usr/bin/env python

import os

header = '''
<!DOCTYPE html>
<html>
<head>
    <title>GRE</title>
    <link rel='stylesheet' type='text/css' href='../style/main.css'>

    <script src="http://code.jquery.com/jquery-2.2.0.min.js"></script>
    <script>
$( document ).ready(function() {
    var get_dictionary = function( word ) {
        // console.log(word);
        $.get( 'dictionary_word_sound_wrapper.py?word=' + word, function (response) {
            console.log( response );
            $( '#sound' ).html( response.word_sound );
            var word_detail = '<h2 class="word">' + response.word + '</h2>' +
                                '<div class="pronunciation">' + response.word_pronunciation + '</div>' +
                                '<div class="definition">' + response.word_definition + '</div>';
            $( '#word-detail-content' ).html( word_detail );
        });
    };

    $( 'a' ).click(function( eventObject ) {
        eventObject.preventDefault();
        var element = $( this );
        word = element.html();
        get_dictionary(word);
    }); // End $( 'a' ).click

    $( '#search' ).click(function( eventObject ) {
        eventObject.preventDefault();
        var word = $( '#search-word' ).val();
        get_dictionary(word);
    });

    $( '.input' ).keypress(function( eventObject ) {
        if (eventObject.which == 13) {
            eventObject.preventDefault();
            var word = $( '#search-word' ).val();
            $( '#search-word' ).select();
            get_dictionary(word);
        }
    });

    $( 'body' ).click(function( e ) {
        $( '#search-word' ).select();
    });
})
    </script>
</head>
'''
print('Content-type: text/html\n')

print(header)
print('<body>')
print('<h1>GRE</h1>')

search_form = '''
<div id='word-search-form'>
<form method='get' action=''>
    <input type='text' name='search-word' id='search-word' class='input'>
    <input type='text' name='definition' value='#definition' class='input'>
    <input type='button' value='Search', name='search' id='search'>
</form>
</div>
'''

print(search_form)

print('<div id="sound">Sound</div>')

print('<div id="main-words">')
print('<dl id="word-list">')
cwd = os.getcwd()
wordfile = open(os.path.join(cwd, 'static/gre1'))
for line in wordfile:
    word = line.strip()
    url_reference = 'http://dictionary.reference.com/browse/' + word
    print('<dt><a class="word" href="%s">%s</a></dt>' % (url_reference, word))
    word_definition = wordfile.__next__().strip()
    print('<dd>%s</dd>' % word_definition)
print('</dl>') # Closing #word-list
print('</div>') # Closing #main_word

print('<div id="word-detail">')
print('<div id="word-detail-content"><h2>Word Detail</h2></div>')
print('</div>') # Closing #word-detail

print('</body>')

print('</html>')
