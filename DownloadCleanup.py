import os
import time
import shutil

# download-cleanup-script
## DANGER 
## DO NOT RUN UNLESS YOU UNDERSTAND IT

# This is a destructive script it will delete all files/folders that don't match its settings
# in the current directory I am not responsible for you delete your stuff.

# It delete any files/folders that are older than a specified number of days in the current directory

# It does not look in the sub dir to match names.

# setup
# Add the files/folders you wish it to ignore to the ignore list and then set haveConfig to True


# config
haveConfig = False
DeleteAfterDays = 5
ignore = [".stfolder", ".stignore", "desktop.ini", "DownloadCleanup.py"]

calcTime = DeleteAfterDays * 24 * 60 * 60

def isIgnored(f):
    for i in ignore:
        if f == i:
            return True
    return False

def DeleteFiles():
    for f in os.listdir('.'):
        if (time.time() - os.path.getmtime(f)) > calcTime and not isIgnored(f):
            if os.path.isdir(f):
                shutil.rmtree(f)
            else:
                os.remove(f)
            print("Deleted: " + f)

def main():
    if not haveConfig:
        input("Script needs to be configured first\n Press Enter to exit")
        return

    i = input("This script will delete all files not matching the ignore and time setting\n Are you Sure Y\\N?\n")
    if i == "Y" or i == "y":
        DeleteFiles()
        input("\n\nDone\nPress Enter to exit")

main()
