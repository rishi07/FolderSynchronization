"""
Author:	Saptarshi Dey
	National Institute of Technology, Durgapur
"""

import glob
import shutil
import os
import re


#list of file types to sort-out. May add new file types.
file_types = ["*.pdf", "*.mp3", "*.docx", "*.txt", "*.odt", "*.mp4", "*.zip", "*.ppt", "*.jpg", "*.jpeg", "*.ipynb"]

#Our source folder which needs to be synchronized.
source = "/home/rishi_07/Documents/"


#Iterating for each file-type
for filetype in file_types:
    
    #Extracting the extension of the file-type
    ext = " ".join(re.findall("['a-zA-Z0-9]+",filetype))
    
    #Creating the destination link
    destination = source + ext.upper()
    
    #If the folder is already created do nothing else creating it
    if not os.path.exists(destination):
        os.makedirs(destination)

    #Now trying the match the extension of each file-type with the list of available files using the glob library
    for filename in glob.glob(source + filetype):
        
        #creating the matched file link
        name = str(destination)
        temp = str(filename)
        temp = temp.split('/')
        name = name + "/"+temp[-1]

        #If the file is already present in the destination just remove the file from the source else moving it
        if not os.path.isfile(name):
            shutil.move(filename,destination)
        else:
            os.remove(filename)

