# 5. Write a Python program to write a list to a file.
import os
print(os.getcwd())
list = [i for i in input().split(" ")]
file = open('Python Directories and Files exercises\\Exercise 5\\file.txt', 'w')
for item in list:
    file.write(f"{item}\n")
print("List written to file.")
file.close()