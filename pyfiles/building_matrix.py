# -*- coding: utf-8 -*-
"""Building 2-Tupels of Strings.

Reads Words from a Wile in a List and writes every possible Word-Combination in
a new File.

-------------------------------------------------------------------------------
It works for me
-> http://programmingexcuses.com/
"""

terms = [line.rstrip('\n') for line in open('files/terme_sorted.txt', 'r')]

with open('files/term_pairs.txt', 'w') as writefile:
    for word_one in terms:
        for word_two in terms:
            writefile.write(word_one + ', ' + word_two + '\n')
