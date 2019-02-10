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
 Table printer, make a table with items of different list
"""

#initialise the object tableData with 3 list, return an object of type list
tableData = [["apples", "oranges", "cherries", "banana"],
            ["Alice", "Bob", "Carol", "David"],
            ["dogs", "cats", "moose", "goose"]]
#initialise 3 objects that will contain the 3 lists of the object tableData, return an object of type list
#list1 = []
#list2 = []
#list3 = []

#put the 3 lists of tableData in each object we are created, return objectcs of type list
list1,list2, list3 = tableData

#condition to browse the three lists at the same time, return an object of type bool
for item1,item2,item3 in zip(list1,list2,list3):

    #print the result like in a table on the screen, return an object of type NoneType
    print("{:>9}{:>6}{:>7}".format(item1,item2,item3))

