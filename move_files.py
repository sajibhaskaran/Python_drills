# Purpose: A Python program to move files to a destination directory.
#
# Author: Saji Bhaskaran
# 


import shutil
import os

def move_file(src,dest):
    files = os.listdir(src)
    for file in files:
        if file.endswith('.txt'):
            path = src+file
            print(path)
            dst = dest+file
            shutil.move(path,dest)




def main():
    dest = "C:/Users/sajibhaskaran/Desktop/folderA/"
    src = "C:/Users/sajibhaskaran/Desktop/folderB/"
    move_file(src,dest)

if __name__ == "__main__":
    main()


