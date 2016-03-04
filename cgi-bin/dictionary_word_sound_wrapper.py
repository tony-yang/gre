#!/usr/bin/env python

# This file uses http get to get the html page and parse through the source
# code to get the mp3 file of the word, and return the mp3 file link to the
# ajax call

import urllib.request, cgi, re, json, os, datetime, os.path

url_parameters = cgi.FieldStorage()
word = url_parameters.getvalue('word', '').strip()
punctuation = ',.!?"()[]'
word = word.translate(word.maketrans(punctuation, " " * len(punctuation)))
definition = url_parameters.getvalue('definition', '').strip();

dictionary_response = urllib.request.urlopen('http://dictionary.reference.com/browse/' + word)
dictionary_html = dictionary_response.read().decode(dictionary_response.headers.get_content_charset())

mp3_file = re.search('<source.*</audio>', dictionary_html)
audio_response = '<audio controls autoplay>'
if mp3_file:
    audio_response += mp3_file.group(0).strip()
else:
    audio_response += '</audio>'

word_pronunciation = re.search('<span class="pron spellpron">.*</span>', dictionary_html)
word_pronunciation_response = word_pronunciation.group(0).strip()
word_definition = re.findall('<div class="def-content">(?:.|\n)*?</div>', dictionary_html)
word_definition_response = ''.join(word_definition).strip()

response = {'word': word,
            'word_sound': audio_response,
            'word_pronunciation': word_pronunciation_response,
            'word_definition': word_definition_response}
json_response = json.dumps(response)

# Store the word/definition pair into a file if definition exists
if definition != '' and word_definition_response != '':
    cwd = os.getcwd()
    file_name = 'static/vocabulary/newword_' + str(datetime.date.today())

    with open(os.path.join(cwd, file_name), 'a+') as word_file:
        word_file.write(word + '\n' + definition +'\n')

print('Content-type: application/json\n')
print(json_response)
