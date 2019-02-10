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
import re
import sys

#get the password and put it in the object password, return the object password of type str
password = input("Enter your password : ")

#put the length of the password in the object length, return the object length of type int
length = len(password)

#condition to verify to compare the password to the number 8
if length > 8:

    #check if the password has uppercase characters, return the object match of type list
    match = re.findall(r'[A-Z]+', password)

    #condition to verify if the password hat uppercase characters
    if match :
        #do nothing
        pass
    else :
        # print our password is not strenght on the screen, return an object of type NoneType
        print("Your password is not strenght")
        #exit the program
        sys.exit()

    #check if the password has lowercase characters, return the object match of type list
    match = re.findall(r"[a-z]+", password)

    #condition to verify if the password hat uppercase characters
    if match :
        pass
    else :
        # print our password is not strenght on the screen, return an object of type NoneType
        print("Your password is not strenght")
        #exit the program
        sys.exit()

    #check if the password has at least one digit
    match = re.findall(r"\d+", password)
    if match :
        print("validate")
    else:
        print("Your password is not strenght")
        sys.exit()

else :
    print("Your password is not strenght")