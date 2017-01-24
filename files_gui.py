import os, shutil
from datetime import datetime, timedelta
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox

def load_gui(self):
    self.lbl_origin = tk.Label(self.master, bg = "silver", text = "Origin directory: ")
    self.lbl_origin.grid( row = 0, column = 0, padx = (20, 0), pady = (10,0), sticky = N+W)
    self.lst_origin = Listbox(self.master, width = 40, height = 8)
    self.lst_origin.grid(row = 1, column = 0, columnspan = 3, padx = (20, 0), pady = (10,0), sticky = N+W)

    self.lbl_dest = tk.Label(self.master, bg = "silver", text = "Destination directory: ")
    self.lbl_dest.grid(row = 2, column = 0, padx = (20, 0), pady = (10,0), sticky = N+W )
    self.lst_dest = Listbox(self.master, width = 40, height = 8)
    self.lst_dest.grid(row = 3, column = 0, padx = (20, 0), pady = (10,0), sticky = N+W)

    self.btn_open = tk.Button(self.master, width = 25, height = 2, text = "Open Origin",
                              command = lambda: open_file(self))
    self.btn_open.grid( row = 1, column = 1, padx = (20,20), pady = (10,0), sticky = N+W)
    self.btn_dest = tk.Button(self.master, width = 25, height = 2, text = "Open Destination",
                              command = lambda: dest_file(self))
    self.btn_dest.grid( row = 1, column = 1, padx = (20,20), pady = (60,0), sticky = N+W)
    self.btn_copy = tk.Button(self.master, width = 25, height = 2, text = "Copy",
                              command = lambda: copy_file(self))
    self.btn_copy.grid( row = 1, column = 1, padx = (20,20), pady = (110,0), sticky = N+E)
    self.btn_open = tk.Button(self.master, width = 25, height = 2, text = "Clear",
                              command = lambda: clear_box(self))
    self.btn_open.grid( row = 3, column = 1, padx = (20,20), pady = (50,0), sticky = N+W)
    self.btn_close = tk.Button(self.master, width = 25, height = 2, text = "Close",
                               command = lambda: close_window(self))
    self.btn_close.grid( row = 3, column = 1, padx = (20,20), pady = (100,0), sticky = N+E)



def open_file(self):
    global src_folder
    src_folder = filedialog.askdirectory()
    folder_name = get_folder(src_folder)
    or_text = "Origin directory: " + folder_name
    self.lbl_origin.configure(text = or_text)
    files = os.listdir(src_folder)
    #print(files)
    for file in files:
        self.lst_origin.insert(END, file)
        

def dest_file(self):
    global dest_folder
    dest_folder = filedialog.askdirectory()
    
    folder_name = get_folder(dest_folder)
    dest_text = "Destination directory: " + folder_name
    self.lbl_dest.configure(text = dest_text)
    

def get_folder(folder):    
    listA = folder.split('/')
    return str(listA[0])+"/.../"+str(listA[len(listA)-1])
    
    


def copy_file(self):
    print(src_folder)
    print(dest_folder)
    
    # finding out the time 24 hours ago.
    time_24hours_ago = datetime.today()-timedelta(hours = 24)
    files = os.listdir(src_folder)
    
    for file in files:
        path = os.path.join(src_folder, file)
        dst = os.path.join(dest_folder, file)
        # print(path)

        # getting the modified time of the file.
        m_time = os.path.getmtime(path)

        # checking if file is recently created or edited.
        if datetime.fromtimestamp(m_time) > time_24hours_ago:
            # copying the file.
            shutil.copy(path, dst)
            self.lst_dest.insert(END, file)
            # print(dst)
    

def clear_box(self):
    self.lst_origin.delete(0, END)
    self.lst_dest.delete(0, END)
    self.lbl_origin.configure(text = "Origin directory: ")
    self.lbl_dest.configure(text = "Destination directory: ")
    

        

def close_window(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application"):
        # closing the app
        self.master.destroy
        os._exit(0)
    
