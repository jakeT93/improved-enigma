#Python Script to rename a batch files

import sys
import os
import shutil
from os.path import expanduser
home = expanduser("~")

try:
    location = sys.argv[1]
except:
    print (' Macha u gotta give me somthing here!!!! Check the argv[0]!!! ')
    quit()


path = location
files = os.listdir(path)
i = 0

for fileName in sorted(files, None, None, True):
    # print("\n" + os.path.join(path, fileName))

    fileIndexStr = str(fileName).replace("Fire_", "", 1)
    fileIndexStr = fileIndexStr.replace(".png", "", 1)

    fileIndex = int(fileIndexStr)
    fileIndex = fileIndex-1

    newName = str("Fire_")

    if fileIndex < 10:
        newName = str(newName + "000")
    elif fileIndex < 100:
        newName = str(newName + "00")
    elif fileIndex < 1000:
        newName = str(newName + "0")

    newName = str(newName + str(fileIndex) + ".png")

    # print(os.path.join(path, newName))

    os.rename(os.path.join(path, fileName), os.path.join(path, newName))

