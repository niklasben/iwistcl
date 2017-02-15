# -*- coding: utf-8 -*-
"""Docstring.

-------------------------------------------------------------------------------
It would have taken twice as long to build it properly
-> http://programmingexcuses.com/
"""

import csv
import numpy as np
import matplotlib.pyplot as plt


str_minus_zero = 'i = -1'
str_zero = 'i = 0'
str_zero_one = '0 < i <= 0.1'
str_zero_two = '0.1 < i <= 0.2'
str_zero_three = '0.2 < i <= 0.3'
str_zero_four = '0.3 < i <= 0.4'
str_zero_five = '0.4 < i <= 0.5'
str_zero_six = '0.5 < i <= 0.6'
str_zero_seven = '0.6 < i <= 0.7'
str_zero_eight = '0.7 < i <= 0.8'
str_zero_nine = '0.8 < i <= 0.9'
str_one = '0.9 < i <= 1'

minus_zero = 0
zero = 0
zero_one = 0
zero_two = 0
zero_three = 0
zero_four = 0
zero_five = 0
zero_six = 0
zero_seven = 0
zero_eight = 0
zero_nine = 0
one = 0

sum_count = 0
paths_sum_negative = 0
paths_sum_positive = 0

list_paths_negative = []
list_paths_positive = []

with open('files/synsets_path_only_stripped.csv', 'r') as openfile:
    reader = csv.DictReader(openfile, delimiter=';')
    for row in reader:
        i = float(row['Path'])
        sum_count = sum_count + 1
        # print(row['Synset #2']) + '\t' + str(i)
        if i < 0:
            # print(row['Path'])
            minus_zero = minus_zero + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
        elif i == 0:
            # print(row['Path'])
            zero = zero + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
        elif 0 < i <= 0.1:
            # print(row['Path'])
            zero_one = zero_one + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            paths_sum_positive = paths_sum_positive + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
            list_paths_positive.append(float(row['Path']))
        elif 0.1 < i <= 0.2:
            # print(row['Path'])
            zero_two = zero_two + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            paths_sum_positive = paths_sum_positive + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
            list_paths_positive.append(float(row['Path']))
        elif 0.2 < i <= 0.3:
            # print(row['Path'])
            zero_three = zero_three + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            paths_sum_positive = paths_sum_positive + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
            list_paths_positive.append(float(row['Path']))
        elif 0.3 < i <= 0.4:
            # print(row['Path'])
            zero_four = zero_four + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            paths_sum_positive = paths_sum_positive + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
            list_paths_positive.append(float(row['Path']))
        elif 0.4 < i <= 0.5:
            # print(row['Path'])
            zero_five = zero_five + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            paths_sum_positive = paths_sum_positive + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
            list_paths_positive.append(float(row['Path']))
        elif 0.5 < i <= 0.6:
            # print(row['Path'])
            zero_six = zero_six + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            paths_sum_positive = paths_sum_positive + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
            list_paths_positive.append(float(row['Path']))
        elif 0.6 < i <= 0.7:
            # print(row['Path'])
            zero_seven = zero_seven + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            paths_sum_positive = paths_sum_positive + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
            list_paths_positive.append(float(row['Path']))
        elif 0.7 < i <= 0.8:
            # print(row['Path'])
            zero_eight = zero_eight + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            paths_sum_positive = paths_sum_positive + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
            list_paths_positive.append(float(row['Path']))
        elif 0.8 < i <= 0.9:
            # print(row['Path'])
            zero_nine = zero_nine + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            paths_sum_positive = paths_sum_positive + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
            list_paths_positive.append(float(row['Path']))
        elif 0.9 < i <= 1:
            # print(row['Path'])
            one = one + 1
            paths_sum_negative = paths_sum_negative + float(row['Path'])
            paths_sum_positive = paths_sum_positive + float(row['Path'])
            list_paths_negative.append(float(row['Path']))
            list_paths_positive.append(float(row['Path']))
        else:
            print 'Something went wrong. There is a result greater than 1!'

print str_minus_zero + ': ' + str(minus_zero) + '\t Percentage incl. -: ' +\
    str(round(float(minus_zero) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(0 / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print str_zero + ': ' + str(zero) + '\t Percentage incl. -: ' +\
    str(round(float(zero) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(0 / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print str_zero_one + ': ' + str(zero_one) + '\t Percentage incl. -: ' +\
    str(round(float(zero_one) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(zero_one / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print str_zero_two + ': ' + str(zero_two) + '\t Percentage incl. -: ' +\
    str(round(float(zero_two) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(zero_two / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print str_zero_three + ': ' + str(zero_three) + '\t Percentage incl. -: ' +\
    str(round(float(zero_three) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(zero_three / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print str_zero_four + ': ' + str(zero_four) + '\t Percentage incl. -: ' +\
    str(round(float(zero_four) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(zero_four / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print str_zero_five + ': ' + str(zero_five) + '\t Percentage incl. -: ' +\
    str(round(float(zero_five) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(zero_five / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print str_zero_six + ': ' + str(zero_six) + '\t Percentage incl. -: ' +\
    str(round(float(zero_six) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(zero_six / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print str_zero_seven + ': ' + str(zero_seven) + '\t Percentage incl. -: ' +\
    str(round(float(zero_seven) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(zero_seven / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print str_zero_eight + ': ' + str(zero_eight) + '\t Percentage incl. -: ' +\
    str(round(float(zero_eight) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(zero_eight / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print str_zero_nine + ': ' + str(zero_nine) + '\t Percentage incl. -: ' +\
    str(round(float(zero_nine) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(zero_nine / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print str_one + ': ' + str(one) + '\t Percentage incl. -: ' +\
    str(round(float(one) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round(one / float(
        (sum_count - minus_zero - zero)) * 100, 3)) + '%'
print 'Total: ' + str(sum_count) + '\t Percentage incl. -: ' +\
    str(round(float(sum_count) / float(sum_count) * 100, 3)) + '%' +\
    '\t Percentage only +: ' + str(round((sum_count - minus_zero - zero) /
                                         float((sum_count - minus_zero - zero)
                                               ) * 100, 3)) + '%'


# Plots including Values <= 0

values_negative = []
values_negative.append(minus_zero)
values_negative.append(zero)
values_negative.append(zero_one)
values_negative.append(zero_two)
values_negative.append(zero_three)
values_negative.append(zero_four)
values_negative.append(zero_five)
values_negative.append(zero_six)
values_negative.append(zero_seven)
values_negative.append(zero_eight)
values_negative.append(zero_nine)
values_negative.append(one)

objects_negative = (str_minus_zero, str_zero, str_zero_one, str_zero_two,
                    str_zero_three, str_zero_four, str_zero_five, str_zero_six,
                    str_zero_seven, str_zero_eight, str_zero_nine, str_one)

y_negative = np.arange(len(objects_negative))

y_mean_negative = sum_count / len(objects_negative)
x_mean_negative = paths_sum_negative / sum_count

# Bar Chart
fig, bar_neg = plt.subplots()
bar_neg.bar(y_negative, values_negative, align='center', alpha=0.5)
bar_neg.axhline(y_mean_negative, color='red', linewidth=2, linestyle='--',
                label=y_mean_negative)
bar_neg.axvline(6, color='green', linewidth=2, linestyle='-', label='0.5')
bar_neg.legend(loc='upper right', fontsize=12)

plt.xticks(y_negative, objects_negative, rotation=60, fontsize=9)
plt.title('Bar Chart incl. Values <= 0')
plt.ylabel('# of found Paths')
plt.savefig('images/bar_chart_incl_negative.png')

# Histogram
fig, hist_neg = plt.subplots()
bins_neg = np.linspace(-1, 1, 50)
hist_neg.hist(list_paths_negative, bins=bins_neg, color='blue', alpha=0.5,
              histtype='stepfilled')
hist_neg.axvline(x_mean_negative, color='blue', linewidth=2, linestyle='-.',
                 label="%.4f" % x_mean_negative)
hist_neg.axvline(0.5, color='green', linewidth=2, linestyle='-', label='0.5')
hist_neg.margins(0.05)
hist_neg.legend(loc='upper center', fontsize=12)

plt.title('Histogram incl. Values <= 0')
plt.ylabel('# of found Paths')
plt.savefig('images/histogram_incl_negative.png')

# Pie Chart
fig, pie = plt.subplots()
colors = ['red', 'tan', 'black', 'coral', 'grey', 'white', 'yellow', 'orange',
          'lightgreen', 'violet', 'blue', 'green']
pie.pie(values_negative, colors=colors, autopct='%.1f%%', shadow=True,
        startangle=90)
pie.legend(objects_negative, loc='upper left', fontsize=10)

plt.title('Pie Chart incl. Values <= 0')
plt.savefig('images/pie_chart_incl_negative.png')


# Plots including Values > 0

values_positive = []
values_positive.append(zero_one)
values_positive.append(zero_two)
values_positive.append(zero_three)
values_positive.append(zero_four)
values_positive.append(zero_five)
values_positive.append(zero_six)
values_positive.append(zero_seven)
values_positive.append(zero_eight)
values_positive.append(zero_nine)
values_positive.append(one)

objects_positive = (str_zero_one, str_zero_two, str_zero_three, str_zero_four,
                    str_zero_five, str_zero_six, str_zero_seven,
                    str_zero_eight, str_zero_nine, str_one)

y_positive = np.arange(len(objects_positive))

y_mean_positive = (sum_count - minus_zero - zero) / len(objects_positive)
x_mean_positive = paths_sum_positive / (sum_count - minus_zero - zero)


# Bar Chart
fig, bar_pos = plt.subplots()
bar_pos.bar(y_positive, values_positive, align='center', alpha=0.5)
bar_pos.axhline(y_mean_positive, color='red', linewidth=2, linestyle='--',
                label=y_mean_positive)
bar_pos.axvline(4, color='green', linewidth=2, linestyle='-', label='0.5')
bar_pos.legend(loc='upper right', fontsize=12)

plt.xticks(y_positive, objects_positive, rotation=60, fontsize=9)
plt.title('Bar Chart incl. Values > 0')
plt.ylabel('# of found Paths')
plt.savefig('images/bar_chart_positive.png')

# Histogram
fig, hist_pos = plt.subplots()
bins_pos = np.linspace(0, 1, 30)
hist_pos.hist(list_paths_positive, bins=bins_pos, color='blue', alpha=0.5,
              histtype='stepfilled')
hist_pos.axvline(x_mean_positive, color='blue', linewidth=2, linestyle='-.',
                 label="%.4f" % x_mean_positive)
hist_pos.axvline(0.5, color='green', linewidth=2, linestyle='-', label='0.5')
hist_pos.margins(0.05)
hist_pos.legend(loc='upper left', fontsize=12)

plt.title('Histogram incl. Values > 0')
plt.ylabel('# of found Paths')
plt.savefig('images/histogram_positive.png')

# Pie Chart
fig, pie = plt.subplots()
colors = ['red', 'tan', 'black', 'coral', 'orange', 'blue', 'yellow', 'green',
          'lightgreen', 'violet']
pie.pie(values_positive, colors=colors, autopct='%.1f%%', shadow=True,
        startangle=90)
pie.legend(objects_positive, loc='upper left', fontsize=10)

plt.title('Pie Chart incl. Values > 0')
plt.savefig('images/pie_chart_positive.png')

# plt.show()
