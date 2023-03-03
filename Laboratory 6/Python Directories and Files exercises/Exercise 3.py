# 3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
path = input("Enter a path: ")  # C:\user\user\dirnames\
if os.path.exists(path):
    print(f"{path} exists.")
    directory, filename = os.path.split(path)
    print(f"Directory: {directory}")
    if os.path.isfile(path):
        print(f"Filename: {filename}")
    else:
        print("No files are in this path.")
else:
    print(f"{path} does not exist.")
