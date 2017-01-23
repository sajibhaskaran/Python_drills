# Purpose: A Python program to figure out the files in a folder that are created
#          or edited in the last 24 hours, and copy them to a destination folder.
#
# 
# Author : Saji Bhaskaran




import os, shutil
from datetime import datetime, timedelta


def modified_time(src, dest):
    # finding out the time 24 hours ago.
    time_24hours_ago = datetime.today()-timedelta(hours = 24)
    files = os.listdir(src)
    
    for file in files:
        path = os.path.join(src, file)
        dst = os.path.join(dest, file)
        # print(path)

        # getting the modified time of the file.
        m_time = os.path.getmtime(path)

        # checking if file is recently created or edited.
        if datetime.fromtimestamp(m_time) > time_24hours_ago:
            # copying the file.
            shutil.copy(path, dst)
            # print(dst)




def main():
    src= r"C:\Users\sajibhaskaran\Desktop\folderA"
    dest= r"C:\Users\sajibhaskaran\Desktop\folderB"
    modified_time(src, dest)



if __name__ == "__main__":
          main()
