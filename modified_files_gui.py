# Purpose: A Python program to figure out the files in a folder that are created
#          or edited in the last 24 hours, and copy them to a destination folder.
#
# 
# Author : Saji Bhaskaran




import os, shutil
from datetime import datetime, timedelta
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import files_gui

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

class AppWindow:

    def __init__(self, master):
        self.master = master
        self.master.minsize(500, 400)
        self.master.maxsize(500, 400)

        self.master.title("Move Files")
        self.master.configure(bg = "silver")

        files_gui.load_gui(self)
        '''
        tk.Button(master, text = "Open",
                  command = self.open_file).grid(row = 1, column = 0)
    
    def open_file(self):
        folder = filedialog.askdirectory()
        files = os.listdir(folder)
        print(files)

        load_gui(self)
        '''
    




def main():
    src= r"C:\Users\sajibhaskaran\Desktop\folderA"
    dest= r"C:\Users\sajibhaskaran\Desktop\folderB"
    # modified_time(src, dest)
    root = tk.Tk()
    app = AppWindow(root)
    root.mainloop()



if __name__ == "__main__":
          main()
