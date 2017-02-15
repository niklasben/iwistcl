# -*- coding: utf-8 -*-
"""Removes a defined character from every line.

-------------------------------------------------------------------------------
I thought he knew the context of what I was talking about
-> http://programmingexcuses.com/
"""

import re


with open('files/synsets_path_only.csv', 'r') as openfile,\
        open('files/synsets_path_only_stripped.csv', 'w') as writefile:
    for line in openfile:
        line = re.sub('\"', '', line)
        line = re.sub('],', '];', line)
        line = re.sub('\[', '', line)
        line = re.sub(']', '', line)
        line = re.sub('#1,', '#1;', line)
        line = re.sub('#2,', '#2;', line)
        # print line
        writefile.write(line)

with open('files/word_synset.csv', 'r') as openfile,\
        open('files/word_synset_stripped.csv', 'w') as writefile:
    for line in openfile:
        line = re.sub('\"', '', line)
        line = re.sub('],', '];', line)
        line = re.sub('\[', '', line)
        line = re.sub(']', '', line)
        line = re.sub('#1,', '#1;', line)
        line = line.replace(',', ';', 1)
        # print line
        writefile.write(line)
