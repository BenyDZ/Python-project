#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     29/12/2018
# Copyright:   (c) user 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import needed object
import tkinter
import re

#get the content of the clipbiard et put it in the object text, return the object text of type str
text = tkinter.Tk().clipboard_get()

#initialise the object newText of type str
newText =""
#initialise the object phoneNumber of type list
phoneNumber = []
#initialise the object newText of type list
emails = []

#condition to read the object text line by line, return an object of type bool
for line in text.splitlines():
    #search all phone number in the object text, return the objet searchNumbers of type list
    searchNumbers = re.findall(r"\+*\(*\+*?\d+\)*[\-\.\ ]?\d+[\-\.\ ]?\d+[\-\.\ ]?\d+[\-\.\ ]?\d+[\-\.\ ]?\w+?\d+ ",line, flags=re.MULTILINE)
    #search all phone number in the object text, return the objet searchNumbers of type list
    searchEmails = re.findall(r"\w+\.?\w*\@\w+\.\w+", line, flags=re.MULTILINE)
    #add each phone in the object phoneNumber
    phoneNumber.append(searchNumbers)
    #add each emails in the object emails
    emails.append(searchEmails)

#conditions to browse the object phoneNumber items by items; return an object of type bool
for items in phoneNumber :
    #conditions to browse the object items items by items; return an object of type bool
    for numbers in items :
        #add each numbers in the object newText
        newText = newText + "\n" + numbers

#conditions to browse the object emails items by items; return an object of type bool
for items in emails :
    #conditions to browse the object items items by items; return an object of type bool
    for email in items :
        #add each numbers in the object newText
        newText = newText + "\n" + email

#clear the clipboard, return an object of type NoneType
tkinter.Tk().clipboard_clear()

#add the object newText in the clipboard, return an object of type NoneType
tkinter.Tk().clipboard_append(newText)

#close tkinter, return an object of type NoneType
tkinter.Tk().destroy()
