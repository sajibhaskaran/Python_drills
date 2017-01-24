# Purpose: A Python GUI program to figure out the files in a folder that are created
#          or edited in the last 24 hours, and copy them to a destination folder.
#
# 
# Author : Saji Bhaskaran




import os, shutil
from datetime import datetime, timedelta
from tkinter import *
import tkinter as tk
from tkinter import filedialog, font

import files_gui


class AppWindow:
    # This class sets up the main application window and a function to figure out
    # the center of the screen.
    # files_gui.py got the rest of the functions for gui elements.
    
    def __init__(self, master):
        helv36 = font.Font(family='Helvetica', size=36, weight='bold')
        self.master = master
        self.master.minsize(500, 400)
        self.master.maxsize(500, 400)

        self.master.title("Move Files")
        self.master.configure(bg = "silver")

        self.center_window(500, 400)

        files_gui.load_gui(self)

    def center_window(self, w, h):

        #function to figure out the center of the screen
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x = int((screen_width/2) - (w/2))
        y = int((screen_height/2) - (h/2))

        centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        return centerGeo
       
    




def main():
    
    root = tk.Tk()
    app = AppWindow(root)
    root.mainloop()



if __name__ == "__main__":
          main()
