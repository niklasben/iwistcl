#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Docstring."""


def lastFirst(firstName, lastName):
    """Docstring."""
    separator = ', '
    result = lastName + separator + firstName
    return result

print(lastFirst('Benjamin', 'Franklin'))
print(lastFirst('Andrew', 'Harrington'))


def sumProblemString(x, y):
    """Docstring."""
    sum = x + y
    return 'The sum of {} and {} is {}.'.format(x, y, sum)


def main():
    """Docstring."""
    print(sumProblemString(2, 3))
    print(sumProblemString(1234567890123, 535790269358))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(sumProblemString(a, b))

main()
