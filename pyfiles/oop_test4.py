# -*- coding: utf-8 -*-
"""Docstring."""

import sys
import getopt


class FileOperation(object):
    """docstring for FileOperation."""

    def __init__(self, outputfile='test.out'):
        """Docstring."""
        self.inputfile = ''
        self.outputfile = outputfile

    def specifyInputfile(self, inputfile):
        """Docstring."""
        self.inputfile = inputfile
        # self.outputfile = outputfile
        return self.inputfile

    # def specifyOutputfile(self, outputfile):
    #     """Docstring."""
    #     self.outputfile = outputfile
    #     return self.outputfile

    def displayFilenames(self):
        """Docstring."""
        print self.inputfile
        print self.outputfile

a = FileOperation()
a.specifyInputfile('intest')
# a.specifyOutputfile('outtest')
a.displayFilenames()
