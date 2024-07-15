#File Detection
import os
path = "D:\\DAN\\TESTING.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("File is directory")
else:
    print("File didn't exist")