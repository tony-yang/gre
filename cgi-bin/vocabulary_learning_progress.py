#!/usr/bin/env python

# This file updates the vocabulary file
# For a word learned, it will mark the word and its definition
# from 0 to 1

import cgi, json, os, os.path

url_parameters = cgi.FieldStorage()
word = url_parameters.getvalue('word', '').strip()
word_number = int(url_parameters.getvalue('wordnum', '').strip())
action = url_parameters.getvalue('action', '').strip()
filename = url_parameters.getvalue('filename', '').strip()

if action != '' and word != '' and word_number != '' and filename != '':
    cwd = os.getcwd()
    file_path = os.path.join(cwd, 'static/vocabulary', filename)

    with open(file_path, 'r+') as word_file:
        word_file.seek(0)
        number_of_line_skip = (word_number - 1) * 2
        for i in range(number_of_line_skip):
            word_file.readline()

        word_file.seek(word_file.tell())
        if action.lower() == 'learned':
            word_file.write('1')
            word_file.flush()
            word_file.readline()
            word_file.seek(word_file.tell())
            word_file.write('1')
            word_file.flush()
        elif action.lower() == 'unlearn':
            word_file.write('0')
            word_file.flush()
            word_file.readline()
            word_file.seek(word_file.tell())
            word_file.write('0')
            word_file.flush()


response = {'word': word,
            'word_number': word_number,
            'action': action,
            'filename': filename}
json_response = json.dumps(response)

print('Content-type: application/json\n')
print(json_response)
