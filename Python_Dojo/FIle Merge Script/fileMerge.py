# Created by Kiren Jacob - 03/12/2017

# Script to merge the contents of any number files
# into a single file of specified format


import sys

numCmdLineArgs = len(sys.argv)

iterator = 1

mergedFilePath = raw_input("Please enter the final output path with fileName.extension appended : ")

print(mergedFilePath)

while iterator < numCmdLineArgs:
    print("arg " + str(iterator) + " : " + sys.argv[iterator])
    with open(sys.argv[iterator], "r") as inputFile:
        with open(mergedFilePath, "a+") as outputFile:
            outputFile.write(inputFile.read()+"\n")
    iterator = iterator + 1

print("All finished here!!!!")


def add():
    print("")
