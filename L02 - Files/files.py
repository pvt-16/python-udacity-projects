import os
import re

path = "E:\Prabha\Projects\python-udacity-projects\L02 - Files\prank"

def rename_files():
    list_path = os.listdir(path)
    print(list_path)
    for filename in list_path:
        new_filename = re.sub("\d+", " ", filename)
        # filename.translate(None,"0123456789")
        print(new_filename)
        os.rename(path+ "\\" +filename, new_filename)
    
rename_files()