from tkinter import *
import tkinter as tk
from tkinter import filedialog

def load_gui(self):
    self.lbl_origin = tk.Label(self.master, bg = "silver", text = "Origin directory:")
    self.lbl_origin.grid( row = 0, column = 0, padx = (20, 0), pady = (10,0), sticky = N+W)
    self.lst_origin = Listbox(self.master, width = 40, height = 8)
    self.lst_origin.grid(row = 1, column = 0, columnspan = 3, padx = (20, 0), pady = (10,0), sticky = N+W)

    self.lbl_dest = tk.Label(self.master, bg = "silver", text = "Destination directory:")
    self.lbl_dest.grid(row = 2, column = 0, padx = (20, 0), pady = (10,0), sticky = N+W )
    self.lst_dest = Listbox(self.master, width = 40, height = 8)
    self.lst_dest.grid(row = 3, column = 0, padx = (20, 0), pady = (10,0), sticky = N+W)

    self.btn_open = tk.Button(self.master, width = 25, height = 2, text = "Open")
    self.btn_open.grid( row = 1, column = 1, padx = (20,20), pady = (10,0), sticky = N+E)
    self.btn_copy = tk.Button(self.master, width = 25, height = 2, text = "Copy")
    self.btn_copy.grid( row = 1, column = 1, padx = (20,20), pady = (60,0), sticky = N+E)
    self.btn_close = tk.Button(self.master, width = 25, height = 2, text = "Close")
    self.btn_close.grid( row = 3, column = 1, padx = (20,20), pady = (100,0), sticky = N+E)
    
    
