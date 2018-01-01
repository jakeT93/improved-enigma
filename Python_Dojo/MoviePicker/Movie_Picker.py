#Created by Kiren Jacob Thomas
#=============================
#01/01/2018

#Movie_Picker
#Selects a random movie or video file within the given constraints

import os

videoFilesRoot = ""

videoFilesRoot = raw_input("Please enter general path : ")

videoFilesRoot = videoFilesRoot.replace("'", "")
print(os.listdir(videoFilesRoot)
