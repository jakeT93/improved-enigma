# Created by Kiren Jacob Thomas
# =============================
# 01/01/2018

# Movie_Picker
# Selects a random movie or video file within the given constraints

import os
import vlc
from random import *
import platform
import subprocess

VLC_Player_Location = ""
videoFormats = [".mp4", ".avi", ".mov"]
#degree = 100


def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def get_random_file(path, deg_of_randomization):
    error_msg = "Sorry! Try again Later!"
    degree = 90

    if not os.path.exists(path):
        return "Not a valid path!!!"

    if str(deg_of_randomization).lower() == 'l':
        degree = 65
    elif str(deg_of_randomization).lower() == 'm':
        degree = 40
    elif str(deg_of_randomization).lower() == 'h':
        degree = 15

    for subdir, dirs, files in os.walk(path):
        for file_name in files:
            for curr_format in videoFormats:
                if file_name.find(curr_format) != -1:
                    if randint(1, 100) < degree:
                    	open_file(subdir)
                        return os.path.join(subdir, file_name)

    return error_msg


videoFilesRoot = ""

# main function starts here...

videoFilesRoot = raw_input("Please enter general path : ")
degRandomization = raw_input("Enter degree of randomization (L/M/H): ")

videoFilesRoot = videoFilesRoot.replace("'", "")

randomFileOut = get_random_file(videoFilesRoot, degRandomization)

if os.path.exists(randomFileOut):
    print("Starting video : " + randomFileOut)
    player = vlc.MediaPlayer(randomFileOut)
    player.play()

