#-------------------------------------------------------------------------------
# Name:        Password
# Purpose:
#
# Author:      Beny DZIENGUE
#
# Created:     28/12/2018
# Copyright:   (c) Beny DZIENGUE 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
Password manager, generate a random password
"""

#imported needed object
import string
import random

#initiliase the object size with the size of the password between 6 and 10, return an object of type int
size = random.randint (6,11)

#set the asci letters in the object letter, return an object of type str
letter = string.ascii_letters

#set all digits in the object digit, return an object of type str
digit = string.digits

#set all punctuations in the object punctuation, return an object of type str
punctuation = string.punctuation

#initialise the object password , return an object of type str
password = ""
#initialise the object counter to 0, return an object of type int
counter=0
#condition to create a password of a size equal to the size object, return an object of type bool
while counter < size :

    # chose a random character between digits, letters, punctuation and add it to the object password, return an object of type str
    password = password + (random.choice(digit + letter + punctuation))

    counter+=1

#print the password on the screen, return an object of type NoneType
print(password)