import os, shutil
from datetime import datetime, timedelta
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3



def load_gui(self):

    create_db()
    # GUI set up using tkinter.
    
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
    self.btn_copy.configure(state = DISABLED)
    self.btn_copy.grid( row = 1, column = 1, padx = (20,20), pady = (110,0), sticky = N+E)
    self.btn_open = tk.Button(self.master, width = 25, height = 2, text = "Clear",
                              command = lambda: clear_box(self))
    self.btn_open.grid( row = 3, column = 1, padx = (20,20), pady = (50,0), sticky = N+W)
    self.btn_close = tk.Button(self.master, width = 25, height = 2, text = "Close",
                               command = lambda: close_window(self))
    self.btn_close.grid( row = 3, column = 1, padx = (20,20), pady = (100,0), sticky = N+E)



def open_file(self):
    # This function runs when user clicks the Open Origin button.
    # Sets up global variable so the filedialog doesn't need to be called
    # multiple times.
    global src_folder
    #self.lst_origin.delete(0, END)
    clear_box(self)
    src_folder = filedialog.askdirectory()
    if src_folder == '':
        messagebox.showwarning("Invalid Selection", "Please pick a valid directory.")
        src_folder = filedialog.askdirectory()
    folder_name = get_folder(src_folder)
    or_text = "Origin directory: " + folder_name
    self.lbl_origin.configure(text = or_text)
    files = os.listdir(src_folder)
    # print(files)
    # Iterating through the files and lists ones that modified recently.
    [self.lst_origin.insert(END, file) for file in files]
        

def dest_file(self):
     # This function runs when user clicks the Open Destination button.
     
    global dest_folder
    
    dest_folder = filedialog.askdirectory()
    if dest_folder == '':
        messagebox.showwarning("Invalid Selection", "Please pick a valid directory.")
        dest_folder = filedialog.askdirectory()
    
    folder_name = get_folder(dest_folder)
    dest_text = "Destination directory: " + folder_name
    self.lbl_dest.configure(text = dest_text)
    self.btn_copy.configure(state = ACTIVE)
    

def get_folder(folder):
    # A helper function to get the selected folder name.
    listA = folder.split('/')
    return str(listA[0])+"/.../"+str(listA[len(listA)-1])
    
    


def copy_file(self):
    
    # finding out the time 24 hours ago.
    time_24hours_ago = datetime.today()-timedelta(hours = 24)
    files = os.listdir(src_folder)
    curr_time = datetime.now()
    data = []
    
    for file in files:
        path = os.path.join(src_folder, file)
        dst = os.path.join(dest_folder, file)
        # print(path)

        # getting the modified time of the file.
        m_time = os.path.getmtime(path)
        

        # checking if file is recently created or edited.
        if datetime.fromtimestamp(m_time) > time_24hours_ago:
            print(datetime.now()- datetime.fromtimestamp(m_time))
            # copying the file.
            shutil.copy(path, dst)
            data.append([file, curr_time])
            self.lst_dest.insert(END, file)
            # print(dst)
    self.btn_copy.configure(state = DISABLED)
    print(data)
    insert_db(data)
    

def clear_box(self):
    # Attached to Clear button to clear items from the list boxes.
    
    self.btn_copy.configure(state = DISABLED)
    self.lst_origin.delete(0, END)
    self.lst_dest.delete(0, END)
    self.lbl_origin.configure(text = "Origin directory: ")
    self.lbl_dest.configure(text = "Destination directory: ")
    

        

def close_window(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application"):
        # closing the app
        self.master.destroy
        os._exit(0)


def create_db():
    conn = sqlite3.connect('copyfiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_savetime(\
                   ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                   col_filename TEXT, \
                   col_updatetime TIMESTAMP);")
        conn.commit()
    conn.close()


def insert_db(data):

    conn = sqlite3.connect('copyfiles.db')
    with conn:
        cur = conn.cursor()
        for item in data:
            cur.execute("""INSERT INTO tbl_savetime (col_filename, col_updatetime)
                              VALUES (?,?)""", (item[0], item[1]))
            conn.commit()
    conn.close()


















        
    
