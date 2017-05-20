#!/usr/bin/python
# -*- coding: utf-8 -*

import re
import pprint


class HeimwerkerCorpus(object):
    """docstring for HeimwerkerCorpus."""

    def __init__(self):
        """Initial Function."""
        # super(HeimwerkerCorpus, self).__init__()
        self.readfile()

    def readfile(self):
        """Read the File."""
        # (1) Wiederholte Satzzeichen
        satzzeichenList = [
            re.compile('[\?\!\.]{2,}'),
            re.compile('\+{2,4}')
        ]

        # (2) Wiederholte Buchstaben:
        buchstabenList = [
            re.compile(
                '.*(a{3,}|e{3,}|i{3,}|o3,}|u{3,}|(ä){2,}|(ö){2,}|(ü){2,}).*'
            ),
            re.compile('.*(b{4,}|d{4,}|g{4,}|p{4,}|t{4,}|k{4,}).*'),
            re.compile('.*(f{4,}|s{4,}|v{4,}|w{4,}|z{3,}|h{3,}).*'),
            re.compile('.*(r{4,}|l{4,}|m{4,}|n{4,}).*')
        ]

        # (3) Wörter zwischen Sternchen:
        sternchenList = [
            re.compile('\*([A-ZÄÖÜ]+|[a-zäöüß]+|([A-ZÄÖÜ][a-zäöüß]+))\*')
        ]

        # (4) Emoticons und Emojis:
        emoList = [
            re.compile('(x|\:|\;|\.)(-|o)?(\(+|\)+|d|p|o|-+|\\|\/)$'),
            re.compile('(\-\_\-|\-\.\-|\.\_\.|[o^][_.-]?[O^]|O[_.]?o|o[_.]o|' +
                       'O[_.]O)$')
        ]

        # (5) Kontrahierte Formen und Verkürzungen:
        kontraList = [
            re.compile('[I|i]ss(es|et|er|e)$'),
            re.compile('[Ss]ind?s$'),
            re.compile('weeste$'),
            re.compile('[Kk]ann(s)(tes?)?$'),
            re.compile('[Hh]a(m|t|tt|ben|b|st)(s|se)$'),
            re.compile(
                '([gh]ab|ist|war|lag|ging|für|er|ihr|du|ich|wir|sie|euch|' +
                'weil|wo|damit)(\')?s$'
            ),
            re.compile('[dD]?[rR](unter|in|an|über|auf)$'),
            re.compile('iss?$'),
            re.compile('(so)?n(e(m|n|r)?)?$')
        ]

        # (6) Umgangssprache:
        umgangsList = [
            re.compile('[H|h]all[o|ö|i](le|chen)$'),
            re.compile('Gr(u|ue|ü)(s|ss|sz|ß)(e|en|chen|le)$'),
            re.compile('ciao$'),
            re.compile('h(i|ey)$'),
            re.compile('bye$'),
            re.compile('tach(chen)?$'),
            re.compile('moin(sen|moin)?$'),
            re.compile('servus$'),
            re.compile('tsch(au|ue|ü|ö)(ss|ß)?$'),
            re.compile('D|d]ing(s|er|erchen|sbums|ens|da).*'),
            re.compile('Zeugs|blöd|blöde.*|doof| doofe.*'),
            re.compile('.*idiot.*'),
            re.compile('.*bl(oe|ö)d.*'),
            re.compile('.*spuck.*'),
            re.compile('.*juck.*'),
            re.compile('.*schwafel.*'),
            re.compile('.*quatsch.*'),
            re.compile('.*kack.*'),
            re.compile('.*m(oe|ö)chtegern.*'),
            re.compile('.*klopp.*'),
            re.compile('.*geil.*'),
            re.compile('.*schei(ss|ß).*'),
            re.compile('.*kotz.*'),
            re.compile('.*macho.*'),
            re.compile('.*weib'),
            re.compile('.*kerl'),
            re.compile('.*sau'),
            re.compile('ok(ay)?'),
            re.compile('kra(ss|ß).*'),
            re.compile('übel(st)?'),
            re.compile('mutier.*'),
            re.compile('arsch.*'),
            re.compile('krisen?'),
            re.compile('lasst?'),
            re.compile('erz(ae|ä)hl.*'),
            re.compile('kauderwelsch'),
            re.compile('(ue|ü)berhaupt'),
            re.compile('wa|n(en?e?|ich)'),
            re.compile('i(rgend)?(wie|wo|was)'),
            re.compile('so(was|(wie|und)(so))'),
            re.compile('o(mm?|pp?)[ai]'),
            re.compile('schn(uppe|ickschnack)'),
            re.compile('Männe')
        ]

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
                        # if re.match('\*', cols[0]):
                            # print(next(readfile, '')).strip()
                            # print cols[0] + '\t' + cols[1]

                        # (1) Wiederholte Satzzeichen
                        if any(satzzeichen.match(cols[0]) for satzzeichen in
                               satzzeichenList):
                            # print '1: ' + cols[0] + '\t' + cols[1]
                            task1 = '1'
                        else:
                            task1 = '0'

                        # (2) Wiederholte Buchstaben
                        if any(buchstabe.match(cols[0]) for buchstabe in
                               buchstabenList):
                            # print '2: ' + cols[0] + '\t' + cols[1]
                            task2 = '1'
                        else:
                            task2 = '0'

                        # (3) Wörter zwischen Sternchen
                        if any(sternchen.match(cols[0]) for sternchen in
                               sternchenList):
                            # print '3: ' + cols[0] + '\t' + cols[1]
                            task3 = '1'
                        else:
                            task3 = '0'

                        # (4) Emoticons und Emojis
                        if any(emo.match(cols[0]) for emo in emoList):
                            # print '4: ' + cols[0] + '\t' + cols[1]
                            task4 = '1'
                        else:
                            task4 = '0'

                        # (5) Kontrahierte Formen und Verkürzungen
                        if any(kontra.match(cols[0]) for kontra in
                               kontraList):
                            # print '5.1: ' + cols[0] + '\t' + cols[1]
                            task5 = '1'

                        elif re.match('Vm.+', cols[1]):
                            if re.match('([bB]i|[wW]ir|[dD]arf|[wW]ill|' +
                                        '[mM]ag|[bB]rauch|[kK]riegt|[nN]imm|' +
                                        '([bB]e)?[kK]omm|[kK]önn|[mM]ach|' +
                                        '[mM]ein|[dD]enk|[fF]inde|[gG]eh|' +
                                        '[wW]ei)(mse|ste|sste|ßte|ts|ens|' +
                                        'tse)$', cols[0]):
                                print '5.2: ' + cols[0] + '\t' + cols[1]
                                task5 = '1'
                        else:
                            task5 = '0'

                        # (6) Umgangssprache
                        if any(umgangssprache.match(cols[0]) for
                               umgangssprache in umgangsList):
                            # print '6: ' + cols[0] + '\t' + cols[1]
                            task6 = '1'

                        elif re.match('bis$', cols[0]):
                            uebertragCols = cols[0]
                            nextline = next(readfile).strip()
                            nextcols = nextline.split('\t')
                            nextcols = filter(None, nextcols)
                            if re.match('(d[ae](nne?|mn(ae|ä)chst)|bald|' +
                                        'morgen|sp(ae|ä)ter)', nextcols[0]):
                                print cols[0] + '\t' + cols[1]
                                # print uebertragCols + ' ' + nextcols[0]

                        elif re.match('gr(ue|ü)(ss|ß)', cols[0]):
                            uebertragCols = cols[0]
                            nextline = next(readfile).strip()
                            nextcols = nextline.split('\t')
                            nextcols = filter(None, nextcols)
                            if re.match('gott$', nextcols[0]):
                                pass
                                # print uebertragCols + ' ' + nextcols[0]

                        elif re.match('macht(\')?s', cols[0]):
                            uebertragCols = cols[0]
                            nextline = next(readfile).strip()
                            nextcols = nextline.split('\t')
                            nextcols = filter(None, nextcols)
                            if re.match('gut$', nextcols[0]):
                                # pass
                                print uebertragCols + ' ' + nextcols[0]

                        elif re.match('oder$', cols[0]):
                            uebertragCols = cols[0]
                            nextline = next(readfile).strip()
                            nextcols = nextline.split('\t')
                            nextcols = filter(None, nextcols)
                            if re.match('was|wie|wo|wer|doch|auch|nicht?',
                                        nextcols[0]):
                                uebertragNextcols = nextcols[0]
                                nextnextline = next(readfile).strip()
                                nextnextcols = nextnextline.split('\t')
                                nextnextcols = filter(None, nextnextcols)
                                if re.match('nicht$', nextnextcols[0]):
                                    pass
                                    # print uebertragCols + ' ' +\
                                    #     uebertragNextcols + \
                                    #     ' ' + nextnextcols[0]
                                else:
                                    pass
                                    # print uebertragCols + ' ' +\
                                    #     uebertragNextcols

                        elif re.match('pi$', cols[0]):
                            uebertragCols = cols[0]
                            nextline = next(readfile).strip()
                            nextcols = nextline.split('\t')
                            nextcols = filter(None, nextcols)
                            if re.match('mal$', nextcols[0]):
                                pass
                                # print uebertragCols + ' ' + nextcols[0]

                        elif re.match('unter(\')?m$', cols[0]):
                            uebertragCols = cols[0]
                            nextline = next(readfile).strip()
                            nextcols = nextline.split('\t')
                            nextcols = filter(None, nextcols)
                            if re.match('strich$', nextcols[0]):
                                pass
                                # print uebertragCols + ' ' + nextcols[0]

                        elif re.match('so$', cols[0]):
                            uebertragCols = cols[0]
                            nextline = next(readfile).strip()
                            nextcols = nextline.split('\t')
                            nextcols = filter(None, nextcols)
                            if re.match('ziemlich$', nextcols[0]):
                                pass
                                # print uebertragCols + ' ' + nextcols[0]

                        elif re.match('mir$', cols[0]):
                            uebertragCols = cols[0]
                            nextline = next(readfile).strip()
                            nextcols = nextline.split('\t')
                            nextcols = filter(None, nextcols)
                            if re.match('egal$', nextcols[0]):
                                pass
                                # print uebertragCols + ' ' + nextcols[0]

                        elif re.match('wie$', cols[0]):
                            uebertragCols = cols[0]
                            nextline = next(readfile).strip()
                            nextcols = nextline.split('\t')
                            nextcols = filter(None, nextcols)
                            if re.match('auch$',
                                        nextcols[0]):
                                uebertragNextcols = nextcols[0]
                                nextnextline = next(readfile).strip()
                                nextnextcols = nextnextline.split('\t')
                                nextnextcols = filter(None, nextnextcols)
                                if re.match('immer$', nextnextcols[0]):
                                    pass
                                    # print uebertragCols + ' ' +\
                                    #     uebertragNextcols + \
                                    #     ' ' + nextnextcols[0]

                        # (8) Anrede bestimmter User in Gruppendiskussionen
                        if re.match('\@.+', cols[0]):
                            # print '8: ' + cols[0] + '\t' + cols[1]
                            task8 = '1'
                        else:
                            task8 = '0'

                        # (9) Interjektionen
                        if re.match('I.*', cols[1]):
                            # print '9: ' + cols[0] + '\t' + cols[1]
                            task9 = '1'
                        else:
                            task9 = '0'

                        # (10) Partikel
                        if re.match('Q.*', cols[1]):
                            # print '10: ' + cols[0] + '\t' + cols[1]
                            task10 = '1'
                        else:
                            task10 = '0'

                        # (11) Adverbien
                        if re.match('R--', cols[1]):
                            # print '11: ' + cols[0] + '\t' + cols[1]
                            task11 = '1'
                        else:
                            task11 = '0'

                        # (12) Personalpronomen
                        if re.match('Pp[12]-.', cols[1]):
                            # print '12: ' + cols[0] + '\t' + cols[1]
                            task12 = '1'
                        else:
                            task12 = '0'

                        # (13) Possessivpronomen
                        if re.match('Pp-.', cols[1]):
                            # print '13: ' + cols[0] + '\t' + cols[1]
                            task13 = '1'
                        else:
                            task13 = '0'

                        # (14) Reflexivpronomen
                        if re.match('P[xs][12]-.', cols[1]):
                            # print '14: ' + cols[0] + '\t' + cols[1]
                            task14 = '1'
                        else:
                            task14 = '0'

                        print cols[0] + '\t' + cols[1] + '\t' + task1 + '\t' +\
                            task2 + '\t' + task3 + '\t' + task4 + '\t' +\
                            task5 + '\t' + task6 + '\t' + task8 + '\t' +\
                            task9 + '\t' + task10 + '\t' + task11 + '\t' +\
                            task12 + '\t' + task13 + '\t' + task14 + '\n'


HeimwerkerCorpus()
