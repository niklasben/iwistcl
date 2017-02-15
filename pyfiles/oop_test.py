# -*- coding: utf-8 -*-
"""Docstring."""


class Employee:
    """Class."""

    empCount = 0

    def __init__(self, name, salary):
        """Docstring."""
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        """Docstring."""
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        """Docstring."""
        print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
