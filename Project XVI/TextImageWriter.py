#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     20/01/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PIL import Image, ImageFont, ImageDraw
import os

#Get a text, return the object text of type str
text = input("Please enter your text : ")
#Change current directory file
os.chdir("C:/Users/user/Pictures/Saved Pictures")
#open an image, return an object of type PIL.PngImagePlugin.PngImageFile
im = Image.open("class_diagram.png")
#define a font and the size for the text, return the object freeMono of type PIL.ImageFont.FreeTypeFont
freeMono = ImageFont.truetype("FreeMono.ttf", size=150)
#create an ImageDraw object, return an object of type PIL.ImageDraw.ImageDraw
d = ImageDraw.Draw(im)
#define the location of the text, return the object location of type tuple
location = (1200, 1200)
#define the color of the text, return the object text_color of type tuple
text_color = (250, 250, 000)
#whrite the text, return an object of type NoneType
d.text(location, text, font=freeMono, fill=text_color)
#save the the new image with the text, return an object of type NoneType
im.save("drawn_grid.png")