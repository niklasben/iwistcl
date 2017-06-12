#!/usr/bin/python
# -*- coding: utf-8 -*

import pprint
import re


def countTwo():
    counterTwo = 0
    with open('bc.processed2.csv', 'r') as openfiletwo:
        for line in openfiletwo:
            counterTwo += 1

    print counterTwo


def findSubcorpora():
    """Find Lines with Subcorpus-Tags and print the Line Nr."""
    counterTwo = 0

    with open('bc.processed2.csv', 'r') as readfile:
        for line in readfile:
            counterTwo += 1
            if re.match('^<subcorpus', line):
                print(str(counterTwo) + '\t' + line + '\n')


def findDocumentsTwo():
    """Find Lines with Document-Tags and print the Line Nr."""
    lineTwo = 0
    counterTwo = 0

    with open('bc.processed2.csv', 'r') as readfile,\
            open('documentsTwo.txt', 'w') as writefile:
        for line in readfile:
            lineTwo += 1
            if re.match('^<document', line):
                counterTwo += 1
                writefile.write(str(counterTwo) + '\t' +
                                str(lineTwo) + '\t' + line)

        divided4 = counterTwo / 4
        lines4 = lineTwo / 4
        writefile.write('\n' + '--------------------------------' + '\n')
        writefile.write('divided4: ' + str(divided4) + '\n')
        writefile.write('lines divided by 4: ' + str(lines4) + '\n')
        writefile.write('--------------------------------' + '\n')
        writefile.write('1: ' + '1\n')
        writefile.write('2: ' + str(lines4) + '\n')
        writefile.write('3: ' + str((lines4 * 2)) + '\n')
        writefile.write('4: ' + str((lines4 * 3)))
        print('divided4: ' + str(divided4))
        print('lines divided by 4: ' + str(lines4))


def findDocumentsThree():
    """Find Lines with Document-Tags and print the Line Nr."""
    lineTwo = 0
    counterTwo = 0

    with open('bc.processed3.csv', 'r') as readfile,\
            open('documentsThree.txt', 'w') as writefile:
        for line in readfile:
            lineTwo += 1
            if re.match('^<document', line):
                counterTwo += 1
                writefile.write(str(counterTwo) + '\t' +
                                str(lineTwo) + '\t' + line)

        divided2 = counterTwo / 2
        lines2 = lineTwo / 2
        writefile.write('\n' + '--------------------------------' + '\n')
        writefile.write('divided2: ' + str(divided2) + '\n')
        writefile.write('lines divided by 2: ' + str(lines2) + '\n')
        writefile.write('--------------------------------' + '\n')
        writefile.write('1: ' + '1\n')
        writefile.write('2: ' + str(lines2))
        print('divided2: ' + str(divided2))
        print('lines divided by 2: ' + str(lines2))


findDocumentsTwo()
findDocumentsThree()


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
