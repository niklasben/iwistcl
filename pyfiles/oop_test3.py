# -*- coding: utf-8 -*-
"""Docstring."""

import sys
import getopt


class FileInput(object):
    """docstring for FileInput."""

    inputfile = ''
    outputfile = ''

    def __init__(self, inputfile, outputfile):
        """Docstring."""
        # super(, self).__init__()
        self.inputfile = inputfile
        self.outputfile = outputfile

    def main(self, argv):
        """Test."""
        # inputfile = ''
        # outputfile = ''
        try:
            opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        except getopt.GetoptError:
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h' or '--help':
                print 'test.py -i <inputfile> -o <outputfile>'
                sys.exit()
            elif opt in ("-i", "--ifile"):
                self.inputfile = arg
            elif opt in ("-o", "--ofile"):
                self.outputfile = arg

    if __name__ == "__main__":
        main(sys.argv[1:])

    def displayFile(self):
        """Docstring."""
        print 'Input file is:', self.inputfile
        print 'Output file is:', self.oututfile


FileInput.main()
