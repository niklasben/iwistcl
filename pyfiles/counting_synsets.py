# -*- coding: utf-8 -*-
"""Docstring.

-------------------------------------------------------------------------------
Oh, that was just a temporary fix
-> http://programmingexcuses.com/
"""

import csv


dict_word_synset = dict()
set_word_synyset = set()
list_word_synset = []

with open('files/word_synset_stripped.csv', 'r') as openfile:
    reader = csv.DictReader(openfile, delimiter=';')
    for row in reader:
        if row['Word #1'] not in dict_word_synset:
            dict_word_synset[row['Word #1']] = [row['Synset #1']]
        else:
            dict_word_synset[row['Word #1']].append(row['Synset #1'])


with open('files/table_term_synsets.tex', 'w') as texfile:
    texfile.write('% Beginn Liste Carsharing Terme mit Synsets\n')
    texfile.write('%\n')
    texfile.write('\\section{Carsharing Terme mit Synsets}\\'
                  'label{sec:list_term_synsets}\n')
    texfile.write('\\begin{longtable}{|m{1cm}|m{4.5cm}|m{7.5cm}|}\n')
    texfile.write('\t\\caption{Carsharing Terme mit Synsets}\\'
                  'label{tbl:car_terme_synsets}\\\\'
                  '%Verweis im Text mittels \\ref{tbl:car_terme_synsets}\n')
    texfile.write('\t\\hline\n')
    texfile.write('\t\\textbf{Nr.} & \\textbf{Term} & \\textbf{Synsets}'
                  '\\\\\n')
    texfile.write('\t\hline \\hline\n')

    length_dict_word_synset = len(dict_word_synset)
    length_dict_word_synset = length_dict_word_synset-1

    counter_key = 0
    for key, value in sorted(dict_word_synset.iteritems()):
        set_values = set(value)
        counter_iter = 0
        counter_total = 0

        for i in sorted(set_values):
            counter_total = counter_total+1

        for value in sorted(set_values):
            counter_iter = counter_iter+1

            if counter_key > 0 and counter_total == 1:
                texfile.write('\t' + str(counter_key) + ' & ' + key + ' & ' +
                              value + '\\\\\n')
                if counter_key < length_dict_word_synset:
                    texfile.write('\t\\hline\n')
                else:
                    texfile.write('\t\\lasthline\n')

            elif counter_key > 0 and counter_total > 1 and counter_iter == 1:
                texfile.write('\t\\multirow{' + str(counter_total) + '}{*}{' +
                              str(counter_key) + '} & \\multirow{' +
                              str(counter_total) + '}{*}{' + key + '} & ' +
                              value + '\\\\\n')

            elif counter_key > 0 and counter_total > 1 and counter_iter > 1:
                texfile.write('\t& & ' + value + '\\\\\n')
                if counter_key < length_dict_word_synset:
                    texfile.write('\t\\hline\n')
                else:
                    texfile.write('\t\\lasthline\n')

        counter_key = counter_key+1

    texfile.write('\\end{longtable}\n')
    texfile.write('%\n')
    texfile.write('% Ende Liste Carsharing Terme mit Synsets')
