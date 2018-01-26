#Bifrost
#--Created by Kiren Jacob Thomas on 09/11/2017

#Takes files from the specified location and magically transports them to hidden location in the multiverse


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

destLocation = '/home/kijato993/.occultatum'

def copyDirectoryRecursively(dirLocation):

    for fileName in os.listdir(dirLocation):
        here = os.path.join(dirLocation, fileName)
        if os.path.isdir(here):
            print("Directory : "+here)
            copyDirectoryRecursively(here)
        elif os.path.isfile(here):
            print("File : " + here)
            shutil.copy(here, destLocation)
    return


if not os.path.exists(destLocation):
    os.makedirs(destLocation)


if len(location) == 0 or location == '':
    print (' Macha u gotta give me somthing here!!!! Check the argv[0] thirittu munchi!!! ')
    quit()

print('*********************')
print('*..Bifrost running..*')
print('*********************')

customPath = raw_input('I found ur home directory at ' + home + '. But do u want to change this? Y|N')
if str(customPath) == 'yes' or str(customPath) == 'y':
    while True:
        customPath = raw_input('In that case tell me where u want it:')
        if os.path.isdir(customPath):
            destLocation = customPath
            break
        elif str(customPath) == 'q':
            quit()
        else:
            print ('Let try that again:')
else:
    print (home + 'it is!!!!')
    destLocation = home + '/.occultatum'


confirmation = raw_input('I know u r in a bit of a hurry but do u really wanna go forward this? (Y|N)')

confirmation = str(confirmation).lower()

print("Confirmation : " + confirmation)

if str(confirmation) == 'yes' or str(confirmation) == 'y':
    print ("okey dokey...")
else:
    print ('Houston! Its a no go... Scrape the launch.')
    quit()

if os.path.isdir(location):
    print('Its a directory!!! Why didnt u tell me?')
    copyDirectoryRecursively(location)
    shutil.rmtree(location)
elif os.path.isfile(location):
    print('Just one file? Whatever u say cap!')
    shutil.copy(location, destLocation)
    os.remove(location)
else:
    print('Its a Bird...Its a Plane...Its Superman!! Wait a minute! Its nothing!!')
    print('Are u serious? Give me something real man!')
