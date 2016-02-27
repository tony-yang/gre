#!/usr/bin/env python

import os

header = '''
<!DOCTYPE html>
<html>
<head>
    <title>GRE</title>
    <link rel='stylesheet' type='text/css' href='../style/main.css'>
    <script src="http://code.jquery.com/jquery-2.2.0.min.js"></script>
    <script src="../style/mainlib.js"></script>
    <script src="../style/index.js"></script>
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
    <input type='text' name='definition' id='search-definition' value='#definition' class='input'>
    <input type='button' value='Search', name='search' id='search'>
</form>
</div>
'''

print(search_form)

print('<div id="sound">Sound</div>')

print('<div id="main-words">')
print('<dl id="word-list"></dl>')
print('</div>') # Closing #main_word

print('<div id="word-detail">')
print('<div id="word-detail-content"><h2>Word Detail</h2></div>')
print('</div>') # Closing #word-detail

print('</body>')
print('</html>')
