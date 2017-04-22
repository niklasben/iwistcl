#!/usr/bin/python
# -*- coding: utf-8 -*

# Import of Standard Libraries
import re
# Import of own Classes
import wiederholteSatzzeichen as wS


class RunProcess(object):
    """docstring for RunProcess."""

    def __init__(self):
        """Init Function."""
        super(RunProcess, self).__init__()

        print 'test'

        with open('bc-testfile.csv', 'r') as readfile:
            # with open('bc.annotated.csv', 'r') as readfile:
            for line in readfile:
                line = line.replace(' ', '\t')
                cols = line.split('\t')

                cols = filter(None, cols)
                if len(cols) > 1:
                    if re.match('<.', cols[0]):
                        pass
                    else:
                        wiederholteSatzzeichen = wS.WiederholteSatzzeichen(cols)
                        # print cols[0]
                        print 'exe: ' + wiederholteSatzzeichen


RunProcess()
