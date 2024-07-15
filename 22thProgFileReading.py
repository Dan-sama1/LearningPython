#Reading a file
try:
    with open("D:\\DAN\\TESTING.txt") as file:
        print("File output: "+file.read())
except FileNotFoundError:
    print("File didn't exist :(")