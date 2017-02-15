# -*- coding: utf-8 -*-
"""Sorting a list alphabetically."""


lines = [line.rstrip('\n') for line in open
         ('files/carsharing1-candlist.txt', 'r')]

length_list = len(lines)

with open('files/carsharing_original_sorted.txt', 'w') as writefile:
    for i in sorted(lines, key=str.lower):
        writefile.write(i + '\n')

count = 0

with open('files/table_words.tex', 'w') as texfile:
    texfile.write('% Beginn Liste Carsharing Terme\n')
    texfile.write('%\n')
    texfile.write('\\section{Carsharing Terme}\\label{sec:list_original}\n')
    texfile.write('\\begin{longtable}{|m{1.5cm}|m{3cm}|m{8.5cm}|}\n')
    texfile.write('\t\\caption{Carsharing Terme}\\label{tbl:car_terme}\\\\'
                  '%Verweis im Text mittels \\ref{tbl:car_terme}\n')
    texfile.write('\t\\hline\n')
    texfile.write('\t\\textbf{Nr.} & \\textbf{Term} & \\textbf{Bemerkungen}'
                  '\\\\\n')
    texfile.write('\t\hline \\hline\n')
    for i in sorted(lines, key=str.lower):
        texfile.write('\t' + str(count+1) + ' & ' + str(i) + ' & ' + '' +
                      '\\\\\n')
        if count < length_list:
            texfile.write('\t\\hline\n')
        else:
            texfile.write('\t\\lasthline\n')
        count = count+1
    texfile.write('\\end{longtable}\n')
    texfile.write('%\n')
    texfile.write('% Ende Liste Carsharing Terme')
