#!/usr/bin/python
# -*- coding: utf-8 -*

import re


class WiederholteSatzzeichen(object):
    """docstring for WiederholteSatzzeichen."""

    # if __name__ == "main":
    def __init__(cols):
        """Init Function."""
        # super(WiederholteSatzzeichen, self).__init__()
        cols = cols
        satzzeichenList = [
            re.compile('[\?\!\.]{2,}'),
            re.compile('\+{2,4}')
        ]

        if any(satzzeichen.match(cols[0]) for satzzeichen in
               satzzeichenList):
            print 'wS: ' + cols[0]
            # return cols[0]


WiederholteSatzzeichen()
