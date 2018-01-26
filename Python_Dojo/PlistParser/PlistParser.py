# This file parses plist files and makes necessary corrections


import plistlib
import sys

try:
    location = sys.argv[1]
except:
    print (' Macha u gotta give me somthing here!!!! Check the argv[0]!!! ')
    quit()

if ".plist" not in location:
    quit()

pl = plistlib.readPlist(location)
print pl
