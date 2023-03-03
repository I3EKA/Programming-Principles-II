# 2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
path = input("Enter a path: ")  # C:\user\user\dirnames\
if os.path.exists(path):
    print(f"{path} exists")

    if os.access(path, os.R_OK):
        print(f"{path} is readable")
    else:
        print(f"{path} is not readable")

    if os.access(path, os.W_OK):
        print(f"{path} is writable")
    else:
        print(f"{path} is not writable")

    if os.access(path, os.X_OK):
        print(f"{path} is executable")
    else:
        print(f"{path} is not executable")
else:
     print(f"{path} does not exist")
# Функция os.path.exists() проверяет, существует ли путь, а функция os.access() используется для проверки разрешений доступа для указанного пути. 
# os.R_OK, os.W_OK и os.X_OK - это константы, которые представляют разрешения на чтение, запись и выполнение соответственно. 
# Программа выводит сообщения о том, существует ли путь, доступен ли он для чтения, записи и выполнения.