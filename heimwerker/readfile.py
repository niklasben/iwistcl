# -*- coding: utf-8 -*-

import re


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

        # (4) Emoticons und Emojis
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

        # with open('bc-testfile.csv', 'r') as readfile:
        with open('bc.annotated.csv', 'r') as readfile:
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
                            pass

                        # (2) Wiederholte Buchstaben
                        elif any(buchstabe.match(cols[0]) for buchstabe in
                                 buchstabenList):
                            pass

                        # (4) Emoticons und Emojis
                        elif any(emo.match(cols[0]) for emo in emoList):
                            pass

                        # (5) Kontrahierte Formen und Verkürzungen
                        elif any(kontra.match(cols[0]) for kontra in
                                 kontraList):
                            pass
                        elif re.match('Vm.+', cols[1]):
                            if re.match('([bB]i|[wW]ir|[dD]arf|[wW]ill|' +
                                        '[mM]ag|[bB]rauch|[kK]riegt|[nN]imm|' +
                                        '([bB]e)?[kK]omm|[kK]önn|[mM]ach|' +
                                        '[mM]ein|[dD]enk|[fF]inde|[gG]eh|' +
                                        '[wW]ei)(mse|ste|sste|ßte|ts|ens|' +
                                        'tse)$', cols[0]):
                                pass

                        # (6) Umgangssprache
                        elif any(umgangssprache.match(cols[0]) for
                                 umgangssprache in umgangsList):
                            pass

                        elif re.match('bis$', cols[0]):
                            uebertragCols = cols[0]
                            nextline = next(readfile).strip()
                            nextcols = nextline.split('\t')
                            nextcols = filter(None, nextcols)
                            if re.match('(d[ae](nne?|mn(ae|ä)chst)|bald|' +
                                        'morgen|sp(ae|ä)ter)', nextcols[0]):
                                pass
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
                        elif re.match('\@.+', cols[0]):
                            pass

                        # (9) Interjektionen
                        elif re.match('I.*', cols[1]):
                            pass

                        # (10) Partikel
                        elif re.match('Q.*', cols[1]):
                            pass

                        # (11) Adverbien
                        elif re.match('R--', cols[1]):
                            pass

                        # (12) Personalpronomen
                        elif re.match('Pp[12]-.', cols[1]):
                            pass

                        # (13) Possessivpronomen
                        elif re.match('Pp-.', cols[1]):
                            pass

                        # (14) Reflexivpronomen
                        elif re.match('P[xs][12]-.', cols[1]):
                            pass


HeimwerkerCorpus()
