#importing needed objects
import os
import re

#define the way to the folder, return an object of type str
foldername = "D:/IIHT/Python/Project/project 2/prank"

#list all files name: return an object of type list
listOfFileName = os.listdir(foldername)

#change current directory file, return an object of type NoneType
os.chdir(foldername)

#on in to list an remove all the numbers in each file, return an object of type bool
for filename in listOfFileName:
    #remove numbers in a file name: return an object of type str
    newName = re.sub('[0-9]', '',filename )
    #change and save the new file name, return an object of type NoneType
    os.rename(filename, newName)


