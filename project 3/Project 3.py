#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      BENY-PC
#
# Created:     14/12/2018
# Copyright:   (c) BENY-PC 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""Project 3 : Remove duplicates and facebook links in a text file"""


#import needed object
import os
import re

#change directory file, return  an object of type NoneType
os.chdir('C:/Users/BENY-PC/Desktop/IIHT/Python/Project/project 3')

#open text file, return  an object of type io.TextIOWrapper
with open("unclean.txt", "r") as fp:

    #read the file content line by line, return an object of type list
    lines = fp.readlines()
    #initialise the list that will contain the new lines
    new_lines = []
    #read the text line by line, return an object of type bool
    for line in lines:
        #- Strip white spaces, return  an object of type str
        line = line.strip()

        #search all facebook's links and delete it, return the object line of type str
        line=re.sub(r'(https?://www.facebook.com/+[^\s]+)', "", line, flags=re.MULTILINE)
        line=re.sub(r'(http?://facebook.com/+[^\s]+)', "", line, flags=re.MULTILINE)

        #search all About and delete it, return the object line of type str
        line=re.sub("About", "", line, flags=re.MULTILINE)


        #delete duplicate lines, return a object of type bool
        if line not in new_lines:
            #add the line in the object new_lines, return  an object of type NoneType
            new_lines.append(line)


#open text file, return  an object of type io.TextIOWrapper
with open("Output.txt", "w") as op:

    #write each line in the object op, return an object of type int
    op.write('\n\n'.join(new_lines))


