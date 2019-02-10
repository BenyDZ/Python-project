#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Beny DZIENGUE
#
# Created:     28/12/2018
# Copyright:   (c) Beny DZIENGUE 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#import needed object
import tkinter

#get the content of the clipbiard et put it in the object text, return an object of type str
text = tkinter.Tk().clipboard_get()

#initialise the object newText, return an object of type str
newText =""

#condition to read the string line by line, return an object of type bool
for line in text.splitlines():

    #add * et a space in front of each line, return an object of type str
    line = "* " + line

    #add the new line in the object newText, return an object of type str
    newText = newText + "\n" + line

#clear the clipboard, return an object of type NoneType
tkinter.Tk().clipboard_clear()

#add the object newText in the clipboard, return an object of type NoneType
tkinter.Tk().clipboard_append(newText)

#, return an object of type NoneType
tkinter.Tk().destroy()









