#!/usr/bin/env python

import os, cgi

url_parameters = cgi.FieldStorage()
category = url_parameters.getvalue('category', 'vocabulary').strip()
title = url_parameters.getvalue('title', 'gre1').strip();

cwd = os.getcwd()
full_file_path = os.path.join(cwd, 'static', category, title)

header = '''
<!DOCTYPE html>
<html>
<head>
    <title>GRE</title>
    <link rel='stylesheet' type='text/css' href='../style/main.css'>
    <script src="http://code.jquery.com/jquery-2.2.0.min.js"></script>
    <script src="../style/mainlib.js"></script>
    <script src="../style/learn.js"></script>
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
with open(full_file_path) as wordfile:
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
