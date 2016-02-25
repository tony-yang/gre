#!/usr/bin/env python

# This file uses http get to get the html page and parse through the source
# code to get the mp3 file of the word, and return the mp3 file link to the
# ajax call

import urllib.request, cgi, re, json

url_parameters = cgi.FieldStorage()
word = url_parameters.getlist('word')[0].strip()
dictionary_response = urllib.request.urlopen('http://dictionary.reference.com/browse/' + word)
dictionary_html = dictionary_response.read().decode(dictionary_response.headers.get_content_charset())

mp3_file = re.search('<source.*</audio>', dictionary_html)
audio_response = '<audio controls autoplay>' + mp3_file.group(0).strip()

word_pronunciation = re.search('<span class="pron spellpron">.*</span>', dictionary_html)
word_pronunciation_response = word_pronunciation.group(0).strip()
word_definition = re.findall('<div class="def-content">(?:.|\n)*?</div>', dictionary_html)
word_definition_response = ''.join(word_definition).strip()

response = {'word': word,
            'word_sound': audio_response,
            'word_pronunciation': word_pronunciation_response,
            'word_definition': word_definition_response}
json_response = json.dumps(response)

print('Content-type: application/json\n')
print(json_response)