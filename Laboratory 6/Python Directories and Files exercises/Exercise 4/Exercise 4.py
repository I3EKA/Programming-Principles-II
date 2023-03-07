# 4. Write a Python program to count the number of lines in a text file.
import os
file = open('KBTU\\Course 1\\Semester 2\\Programming Principles II\\Laboratory\\Laboratory 6\\Python Directories and Files exercises\\Exercise 4\\file.txt', 'r')
line_count = 0
while file.readline():
    line_count += 1
print(f"Number of lines: {line_count}")
file.close()
