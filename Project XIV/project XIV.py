#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     18/01/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
        Program that show current price of coffee beans
"""
#import needed object
import urllib.request

def getcurrentPrice() :
    """
    function to get the current price of coffee beans
    """
    #Take the content of the web page, return the object page of type http.client.HTTPResponse
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")

    #decode the content on utf-8, return the object text of type str
    text = page.read().decode("utf8")

    #put the index of the char $ in the object dollarIndex, return an object of type int
    dollarIndex = text.find("$")

    #take the price without the char $, convert it to type string on type float and put it on the object price, return an object of type float
    price = float (text[dollarIndex+1:dollarIndex+5])

    return price

def getChoice ():
    """
    Function to get the choice of the user
    """
    while True :
        try :
            #get the choice and convert in integer
            choice = int(input("Enter your choice : "))
            #assert that the choice is equal to 1 or 2
            assert choice == 1 or choice ==2
            break
        #in case the entered value is not an integer
        except ValueError :
            #print La valeur entrée n'est pas un entier on the screen, return an object of type NoneType
            print("La valeur entrée n'est pas un entier")
        #in case the entered value is not an integer
        except AssertionError:
            #print La valeur entrée n'est pas un entier on the screen, return an object of type NoneType
            print("La valeur entrée est soit supérieur à 2 ou inférieur à 1")

    return choice

print("Select your option : ")
print("1. Wait for price of coffee beans drop")
print("2. Place an emergency order")

choice = getChoice()

if choice == 1:
    #initialise the object price to 4.75, return an object of type float
    price = 4.75
    #condition to repeat the program while the price is higher than 4.74
    while price > 4.74:
        #get currence price, return the object price of type float
        price = getcurrentPrice()
        #condition to compar the object price to the float 4.74, return an object of type bool
        if price < 4.74 :
            #print the price with the symbol $ on the screen, return an object of type NoneType
            print("The current price is : ${}".format(price))
            #stop the program
            break
if choice == 2:
    price = getcurrentPrice()
    print("The current price is : ${}".format(price))