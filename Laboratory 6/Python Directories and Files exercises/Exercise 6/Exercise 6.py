# 6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os
for i in range(ord("A"), ord("Z") + 1):
    file = open(f'KBTU\\Course 1\\Semester 2\\Programming Principles II\\Laboratory\\Laboratory 6\\Python Directories and Files exercises\\Exercise 6\\Text Files\\{chr(i)}.txt', 'w')
    file.write(f"This is the {chr(i)}.txt file.")
    file.close()
print("All done")