#!/usr/bin/env python

import os, cgi

url_parameters = cgi.FieldStorage()
category = url_parameters.getvalue('category', 'index').strip()
title = url_parameters.getvalue('title', '').strip();
get_param_vocabulary = url_parameters.getvalue('vocabulary', '').strip()

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

navigation = '''
<div id="nav">
    <ul>
        <li><a href="index.py">Home</a></li>
        <li><a href="learn.py">Learn</a></li>
    </ul>
</div>
'''

def create_list_index(list_name, current_path, files, vocabulary_level=''):
    content = '<h3 id="%s-nav">%s</h3><ul id="%s-index">' % (list_name, list_name, list_name)
    if vocabulary_level:
        for filename in files:
            content_url = 'learn.py?category=%s&title=%s&vocabulary=%s' % (current_path, filename, vocabulary_level)
            content += '<li><a href="%s">%s</a></li>' % (content_url, filename)
        content += '</ul>'
    else:
        for filename in files:
            content_url = 'learn.py?category=%s&title=%s' % (current_path, filename)
            content += '<li><a href="%s">%s</a></li>' % (content_url, filename)
        content += '</ul>'
    return content

def create_content():
    cwd = os.getcwd()
    full_file_path = os.path.join(cwd, 'static', category, title)
    content = ''

    if category == 'vocabulary':
        if get_param_vocabulary == 'new':
            content += '<div id="start-flashcard"><span>Start Flashcards</span></div>'
            content += '<div id="flashcards"><div id="flashcard-stop"><span>Stop</span></div><div id="word-flashcard"></div></div>'

        content += '<dl id="word-list">'
        with open(full_file_path) as wordfile:
            word_counter = 0
            for line in wordfile:
                word = line.strip()
                try:
                    word_definition = wordfile.__next__().strip()
                except StopIteration:
                    word_definition = '0 NA'

                word_counter += 1
                url_reference = 'http://dictionary.reference.com/browse/' + word[2:]

                if word[:1] == '0' and get_param_vocabulary == 'new':
                    content += '<dt><a class="%s word" href="%s">%s</a><span class="%s %s learned-word">Learned</span></dt>' % (word_counter, url_reference, word[2:], word_counter, word[2:])
                    content += '<dd>%s</dd>' % word_definition[2:]
                elif word[:1] == '1' and get_param_vocabulary == 'learned':
                    content += '<dt><a class="%s word" href="%s">%s</a><span class="%s %s unlearned-word">Unlearn</span></dt>' % (word_counter, url_reference, word[2:], word_counter, word[2:])
                    content += '<dd>%s</dd>' % word_definition[2:]
                elif not get_param_vocabulary:
                    content += '<dt><a class="%s word" href="%s">%s</a></dt>' % (word_counter, url_reference, word[2:])
                    content += '<dd>%s</dd>' % word_definition[2:]
        content += '</dl>'
    elif category == 'passage' or category == 'books':
        content = '<div id="word-list">'
        with open(full_file_path) as wordfile:
            story = wordfile.read().strip()
            paragraphs = story.splitlines()
            paragraphs = [' '.join(['<span>' + word + '</span>' for word in line.split(' ')]) for line in paragraphs]
            paragraphs = ['<p>' + line + '</p>' for line in paragraphs]

            content += '\n'.join(paragraphs)
        content += '</div>'
    elif category == 'index':
        content = '<div id="learn-nav">'
        static_path = os.path.join(cwd, 'static')
        for path, dirs, files in os.walk(static_path):
            current_path = os.path.split(path)[-1]
            if current_path == 'static':
                content += '<h2>Index</h2>'
            elif current_path == 'vocabulary':
                list_name = 'new-vocabulary'
                vocabulary_level = 'new'
                content += create_list_index(list_name, current_path, files, vocabulary_level)

                list_name = 'learned-vocabulary'
                vocabulary_level = 'learned'
                content += create_list_index(list_name, current_path, files, vocabulary_level)

                list_name = 'full-list-vocabulary'
                content += create_list_index(list_name, current_path, files)
            else:
                list_name = current_path
                content += create_list_index(list_name, current_path, files)

        content += '</div>'


    return content

print('Content-type: text/html\n')

print(header)

print('<body>')
print('<h1>GRE</h1>')
print(navigation)

print('<div id="sound">Sound</div>')

print('<div id="main-words">')

print(create_content())

print('</div>') # Closing #main_word

print('<div id="word-detail">')
print('<div id="word-detail-content"><h2>Word Detail</h2></div>')
print('</div>') # Closing #word-detail

print('</body>')
print('</html>')
