#!/usr/bin/python
# -*- coding: utf-8 -*

import re
import pprint


def countLines():
    """Count Lines of File."""
    counter = 0

    with open('bc.processed.csv', 'r') as readfile:
        for line in readfile:
            counter += 1

    print counter


def findSubcorpora():
    """Find Lines with Subcorpus-Tags and print the Line Nr."""
    counter = 0

    with open('bc.processed.csv', 'r') as readfile:
        for line in readfile:
            counter += 1
            if re.match('^<subcorpus', line):
                print(str(counter) + '\t' + line + '\n')
                # print(counter, line)


def printLineNumbers():
    """Make a new File with the Information."""
    counter = 0

    with open('bc.processed.csv', 'r') as readfile,\
            open('linesubcorpusinfo.txt', 'w') as writefile:
        for line in readfile:
            counter += 1
            if re.match('^<subcorpus', line):
                writefile.write(str(counter) + '\t' + line + '\n')
                # print(counter, line)

        divided4 = counter / 4
        divided3 = counter / 3
        divided2 = counter / 2
        writefile.write('\n' + 'No. of Lines: ' + str(counter) + '\n')
        writefile.write('Divided by 4: ' + str(divided4) + '\n')
        writefile.write('Divided by 3: ' + str(divided3) + '\n')
        writefile.write('Divided by 2: ' + str(divided2) + '\n')
        writefile.write('---------------------' + '\n')
        writefile.write('No. 1: ' + '1' + '\n')
        writefile.write('No. 2: ' + str(divided4) + '\t' + str(divided3) +
                        '\t' + str(divided2) + '\n')
        writefile.write('No. 3: ' + str(divided4 * 2) + '\t' +
                        str(divided3 * 2) + '\n')
        writefile.write('No. 4: ' + str(divided4 * 3) + '\n')

        print('No. of Lines:', str(counter))
        print('Divided by 4:', str(divided4))
        print('-------------------------')
        print('No. 1: ', '1')
        print('No. 2: ', str(divided4), str(divided3), str(divided2))
        print('No. 3: ', str(divided4 * 2), str(divided3 * 2))
        print('No. 4: ', str(divided4 * 3))


def makeNewFiles():
    """Make four new Files."""
    counter = 0

    with open('bc.processed.csv', 'r') as readfile,\
            open('bc.processed1.csv', 'w') as fileone,\
            open('bc.processed2.csv', 'w') as filetwo,\
            open('bc.processed3.csv', 'w') as filethree,\
            open('bc.processed4.csv', 'w') as filefour:

        for line in readfile:
            counter += 1
            if 1 <= counter <= 2404258:
                fileone.write(line)
            elif 2404259 <= counter <= 29082756:
                filetwo.write(line)
            elif 29082757 <= counter <= 40616955:
                filethree.write(line)
            elif 40616956 <= counter <= 47848267:
                filefour.write(line)
            else:
                print('ERROR: ', counter)


makeNewFiles()
