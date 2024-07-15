#MOVING FILES
import os

source = "D:\\DAN\\S\\copy.txt"
dst = "D:\\DAN\\path\\copy.txt"
try:
    if os.path.exists(dst):
        print("File already exist")
    else:
        os.replace(source, dst)
        print("File successfully moved")
except FileNotFoundError:
    print("Source not found")