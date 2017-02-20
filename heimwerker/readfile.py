# -*- coding: utf-8 -*-

import re


with open('bc-testfile.csv', 'r') as readfile:
    for line in readfile:
        line = line.replace(' ', '\t')
        cols = line.split('\t')

        cols = filter(None, cols)
        if len(cols) > 1:
            # print cols
            if re.match('<.', cols[0]):
                pass
            else:
                print cols[0] + '\t' + cols[1]
