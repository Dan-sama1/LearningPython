#DELETING FILE
import os
import shutil #used to delete a folder that has file in it

path = 'D:\\DAN\\TESTING.txt'

try:
    os.remove(path) #Deletes a file
    #os.rmdir('path') #Deletes an empty folder (rmdir: remove directory)
    #shutil.rmtree(path) #Deletes a folder that has file in it (rmtree: remove tree)
except FileNotFoundError:
    print("File not found :(")
except PermissionError:
    print("You cannot delete that file")
except OSError:
    print("Error")
else:
    print(path + " deleted successfully")