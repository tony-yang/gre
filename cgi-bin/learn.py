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

    $( 'body' ).on('click', 'a', function( eventObject ) {
        eventObject.preventDefault();
        var element = $( this );
        word = element.html();
        get_dictionary(word);
    }); // End $( 'a' ).click
})
    </script>

</head>
'''
print('Content-type: text/html\n')

print(header)
print('<body>')
print('<h1>GRE</h1>')

print('<div id="sound">Sound</div>')

print('<div id="main-words">')
print('<dl id="word-list">')
cwd = os.getcwd()
wordfile = open(os.path.join(cwd, 'static/vocabulary/gre1'))
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
