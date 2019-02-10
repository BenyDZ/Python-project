#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      BENY-PC
#
# Created:     15/12/2018
# Copyright:   (c) BENY-PC 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#print "welcome" on the screen, retur an object on type NoneType
print('Welcome!')

#initialize guess to 0 to enter the loop
guess = 0

#repeat the program until guess is equal to the number
while guess != 5:
    #ask a user to input a guess and convert it to type str into an object of type int
    guess = int(input('Guess the number : '))

    # condition to compar the object guess on the type int to the number 5
    if guess == 5:
        #print "You win" on the screen, return an object on the type NoneType
        print('You win!')
        break

    else :
        # condition to compar the object guess on the type int to the number 5 to know if it is higher
        if guess > 5 :
            
            #print "Too high" on the screen, return an object on the type NoneType
            print("Too high")
            #print "You loose" on the screen, return an object on the type NoneType
            print("You loose")
            
        else :
             #print "Too low" on the screen, return an object on the type NoneType
            print("Too low")
            #print "You loose" on the screen, return an object on the type NoneType
            print("You loose")

#print "Game over" on the screen, return an object on the type NoneType
print("Game over")
