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
"""
        Program that show current price of coffee beans
"""
#import needed object
import urllib.request

#initialise the object price to 4.75, return an object of type float
price = 4.75

#condition to repeat the program while the price is higher than 4.74
while price > 4.74:

    #Take the content of the web page, return the object page of type http.client.HTTPResponse
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")

    #decode the content on utf-8, return the object text of type str
    text = page.read().decode("utf8")

    #put the index of the char $ in the object dollarIndex, return an object of type int
    dollarIndex = text.find("$")

    #take the price without the char $, convert it to type string on type float and put it on the object price, return an object of type float
    price = float (text[dollarIndex+1:dollarIndex+5])

    #condition to compar the object price to the float 4.74, return an object of type bool
    if price < 4.74 :

        #print the price with the symbol $ on the screen, return an object of type NoneType
        print(text[dollarIndex:dollarIndex+5])

        #stop the program
        break
