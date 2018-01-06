## Created by Kiren Jacob Thomas
# =============================
# 01/01/2018
# File_Sorter
# Sorts file according to name and puts in folder

import os
from shutil import copyfile

targetFolderLocation = raw_input("Target Folder : ")
targetFolderLocation = targetFolderLocation.replace("'", "")

if os.path.exists(targetFolderLocation):
    keyWord = raw_input("Enter keyword : ")
    destLocation = raw_input("Enter destination : ")
    destLocation = destLocation.replace("'", "")
    if os.path.exists(destLocation):
        destFolderName = raw_input("Enter directory name : ")
        os.makedirs(os.path.join(destLocation, destFolderName))
        for subDir, directories, files in os.walk(targetFolderLocation):
            for name in files:
                if name.find(keyWord) != -1:
                    targetFile = os.path.join(subDir, name)
                    destFile = os.path.join(destLocation, destFolderName)
                    destFile = os.path.join(destFile, name)
                    print targetFile
                    print destFile
                    copyfile(targetFile, destFile)

