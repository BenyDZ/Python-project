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

from moviepy.editor import *
import time
import os

#Change current directory file
os.chdir("D:/Videos/South.Park.Season.22.Complete.UNCENSORED.720p.WEB-DL.x264.AAC")

#get a specific part of the video, return the object video of type moviepy.video.io.VideoFileClip.VideoFileClip
video = VideoFileClip("South.Park.S22E01.Dead.Kids.UNCENSORED.720p.WEB-DL.x264.AAC.mp4").subclip(400,420)
# Make the text, define position and duration, return the object video of type moviepy.video.VideoClip.TextClip
txt_clip = ( TextClip("The best anime",fontsize=70,color='red')
             .set_position('center')
             .set_duration(10) )
# Overlay text on video, return the object of type moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip'
result = CompositeVideoClip([video, txt_clip])
#create the new video with the text, return an object of type  NoneType
result.write_videofile("The_best_anime.mp4",fps=25)