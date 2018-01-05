# Created by - Kiren Jacob Thomas
# ===============================
#
# Creates the specified folder structure at the dest 

import os

targetLocation = raw_input("Enter the target Location : ")
targetLocation = targetLocation.replace("'", "")
destLocation = raw_input("Enter Destination : ")
destLocation = destLocation.replace("'", "")

for subdir, directory, files in os.walk(targetLocation):
    for direc in directory:
        print(direc)
