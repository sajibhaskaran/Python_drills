import os, shutil
from datetime import datetime, timedelta
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import sqlite3



def load_gui(self):

    
    
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
    create_db()
    get_db(self)


    



def open_file(self):
    # This function runs when user clicks the Open Origin button.
    # Sets up global variable so the filedialog doesn't need to be called
    # multiple times.
    global src_folder

    # Clearing the list box.
    clear_box(self)
    src_folder = filedialog.askdirectory()
    if src_folder == '':
        messagebox.showwarning("Invalid Selection", "Please pick a valid directory.")
        src_folder = filedialog.askdirectory()
    else:
        folder_name = get_folder(src_folder)
        or_text = "Origin directory: " + folder_name
        self.lbl_origin.configure(text = or_text)
        get_data = get_db(self)
        
        files = get_files(src_folder, get_data)
        if(len(files) == 0):
            self.lst_origin.insert(END, "No new or modified files")
        else:
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


def get_files(folder, time):
    # Getting the files from selected folder.
    files = os.listdir(src_folder)    
    c_files = []
    for file in files:
        path = src_folder+'/'+file      

        # getting the modified time of the file.
        m_time = os.path.getmtime(path)
        # checking if file is recently created or edited.
        if datetime.fromtimestamp(m_time) > time:
            # copying the file.
            c_files.append(file)
    return c_files
    
    


def copy_file(self):
    
    # finding out the time 24 hours ago.
    
    data = []
    time_id = round(datetime.today().timestamp())
    get_data = get_db(self)
    files = get_files(src_folder, get_data)
    # Clearing the list box.
    clear_box(self)
    for file in files:
        path = os.path.join(src_folder, file)
        dst = os.path.join(dest_folder, file)
        if path == dst:
            messagebox.showwarning("Invalid Selection", "Origin and Destination folders are the same! \nPlease pick a valid directory.")
        else:
            shutil.copy(path, dst)
            data.append([time_id, file])
        
    self.btn_copy.configure(state = DISABLED)
    insert_db(data)
    get_db(self)
    

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
    # Creting the database if it is not already exists.
    conn = sqlite3.connect('copyfiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_savetime(\
                   ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                   col_timeid INTEGER, \
                   col_filename TEXT);")
        conn.commit()
        # Checking to see if the database is empty. If so, putting some initial data in it.
        cur.execute("""SELECT * FROM tbl_savetime""")
    
        count = cur.fetchall()
        if not count:
            time_id = round(datetime.today().timestamp())
            cur.execute("""INSERT INTO tbl_savetime (col_timeid, col_filename)
                                VALUES (?,?)""",(time_id, "No Files"))
            conn.commit()
    conn.close()


def insert_db(data):
    # Inserting the copied filenames and the timestamp in the database.
    conn = sqlite3.connect('copyfiles.db')
    with conn:
        cur = conn.cursor()
        for item in data:
            cur.execute("""INSERT INTO tbl_savetime (col_timeid, col_filename)
                              VALUES (?,?)""", (item[0], item[1]))
            conn.commit()
    conn.close()


def get_db(self):
    # Getting the last updated time and the files updated from the database.
    conn = sqlite3.connect('copyfiles.db')
    cur = conn.cursor()
    cur.execute("""SELECT MAX(ID) AS ID, col_timeid, col_filename FROM tbl_savetime""")
    r_data = cur.fetchall()    
    updated_time = r_data[0][1]
    
    if updated_time == None:
        self.lst_dest.insert(END, "No files copied yet!")
    else:
        r_time = datetime.fromtimestamp(updated_time)
        date = r_time.strftime('%B %d, %Y')
        time = r_time.strftime('%I:%M%p')
        self.lst_dest.insert(1, "Last file check: ")
        self.lst_dest.insert(2, "Date:  {}".format(date))
        self.lst_dest.insert(3, "Time:  {}".format(time))
        self.lst_dest.insert(4, "Files updated: ")
        
        cur.execute("""SELECT col_filename FROM tbl_savetime WHERE col_timeid ={id}""".format(
                                                                                        id = updated_time))
        c_data = cur.fetchall()
        
        [self.lst_dest.insert(5, item[0]) for item in c_data]
    conn.close()
    # returning the timestamp of the last check.
    return r_time
       


    
    
        
    
    

















        
    
