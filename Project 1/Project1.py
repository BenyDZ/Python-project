#-------------------------------------------------------------------------------
# Name:        Take a Music Break
# Purpose:
#
# Author:      BENY-PC
#
# Created:     14/12/2018
# Copyright:   (c) BENY-PC 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Project 1 :
#   write a program that schedules breaks throughout the day reminding your
#    friend to listen to his favorite music in the web browser, get up and dance
#     to it or just walk away from the computer if he wants to, then go back to
#      work when his favorite music finishes to play.

#import needed object
import webbrowser
import time

# initialise the object iteration to 0
iteration = 0

#Loop to repeat the code 3 times, return an object of type bool
while iteration < 3 :
    #wait 360 secondes return an objct of type NoneType
    time.sleep(360)
    #open the song in the web navigator, return an obect of type bool
    webbrowser.open('https://www.youtube.com/watch?v=qNiNsHB9nQU&list=RDqNiNsHB9nQU&start_radio=1')
    #inc the value of itération or add + 1 in the value of itération
    iteration+=1
