# 1. Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = input("Enter a path: ")  # C:\user\user\dirnames\
# Перечислите все каталоги в пути
print("Directories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        print(name)

# Список всех файлов в пути
print("Files: ")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        print(name)

# Список всех каталогов и файлов в пути
print("Directories and Files: ")
for dirpath, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
        print('Directory: ', os.path.join(dirpath, dirname))
    for filename in filenames:
        print('File:', os.path.join(dirpath, filename))

# Эта программа использует модуль os для составления списка каталогов и файлов в указанном пути. 
# Функция os.listdir() используется для получения списка всех файлов и каталогов в пути, а модуль os.path используется для проверки того, является ли каждый элемент каталогом или файлом.
# Программа сначала перечисляет все каталоги в пути, затем все файлы и, наконец, все каталоги и файлы. 
# Она использует функцию os.walk() для обхода дерева каталогов и рекурсивного перечисления всех каталогов и файлов.
