# 7. Write a Python program to copy the contents of a file to another file
original_file = open('KBTU\\Course 1\\Semester 2\\Programming Principles II\\Laboratory\\Laboratory 6\\Python Directories and Files exercises\\Exercise 7\\original_file.txt', 'r')
file_contents = original_file.read()
new_file = open('KBTU\\Course 1\\Semester 2\\Programming Principles II\\Laboratory\\Laboratory 6\\Python Directories and Files exercises\\Exercise 7\\new_file.txt', 'w')
new_file.write(file_contents)
print('File compied successfully!')
original_file.close()
new_file.close()
