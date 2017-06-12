#!/usr/bin/python
# -*- coding: utf-8 -*

import re


def countLength():
    """Count Length of File."""
    counter = 0

    with open('bc.processed3.csv', 'r') as openfile:
        for line in openfile:
            counter += 1
            if counter == 1:
                print line

        print('Length: ', counter)


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


def makeNewTwo():
    """Split Nr. 2."""
    counter = 0
    subcorpusend = '</subcorpus>'

    with open('bc.processed2.csv', 'r') as openfiletwo,\
            open('bc.processed2-1.csv', 'w') as fileone,\
            open('bc.processed2-2.csv', 'w') as filetwo,\
            open('bc.processed2-3.csv', 'w') as filethree,\
            open('bc.processed2-4.csv', 'w') as filefour:

        for line in openfiletwo:
            counter += 1
            if counter == 1:
                fileone.write(line)
                filetwo.write(line)
                filethree.write(line)
                filefour.write(line)
            elif 2 <= counter <= 6663153:
                fileone.write(line)
            elif 6663154 <= counter <= 13394161:
                filetwo.write(line)
            elif 13394162 <= counter <= 20008475:
                filethree.write(line)
            elif 20008476 <= counter <= 26678497:
                filefour.write(line)
            elif counter == 26678498:
                print('Last Line reached Two: ', counter)
            else:
                print('ERROR Two: ', counter)

        fileone.write(subcorpusend)
        filetwo.write(subcorpusend)
        filethree.write(subcorpusend)
        filefour.write(subcorpusend)


def makeNewThree():
    """Split Nr. 3."""
    counter = 0
    subcorpusend = '</subcorpus>'

    with open('bc.processed3.csv', 'r') as openfiletwo,\
            open('bc.processed3-1.csv', 'w') as fileone,\
            open('bc.processed3-2.csv', 'w') as filetwo:

        for line in openfiletwo:
            counter += 1
            if counter == 1:
                fileone.write(line)
                filetwo.write(line)
            elif 2 <= counter <= 5767659:
                fileone.write(line)
            elif 5767660 <= counter <= 11534198:
                filetwo.write(line)
            elif counter == 11534199:
                print('Last Line reached Three: ', counter)
            else:
                print('ERROR Three: ', counter)

        fileone.write(subcorpusend)
        filetwo.write(subcorpusend)


makeNewTwo()
makeNewThree()
