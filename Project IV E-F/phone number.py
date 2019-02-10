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
"""
  Verify if a string is a phone number
"""
#import needes object
import re

#enter the string, return an object of type str
text = input ("Enter the number : ")

#search the phone number in the object text, return an object of type NoneType
match = re.search(r'^\(*\d{3}\)*[\-\.\ ]\d{3}[\-\.]\d{4}.*', text)

#condition to verify if the object text is a phone number, return an object of type bool
if match :
    #print the value of the object text and is a phone number : True on the screen, return an object of type NoneType
    print(text, " is a phone number : \nTrue")
else :
    #print the value of the object text and is a phone number : False on the scree, return an object of type NoneType
    print(text, " is a phone number : \nFalse")