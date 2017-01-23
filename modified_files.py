import os, shutil
from datetime import datetime, timedelta


def modified_time(src, dest):
    time_24hours_ago = datetime.today()-timedelta(hours = 24)
    files = os.listdir(src)
    for file in files:
        path = os.path.join(src, file)
        dst = os.path.join(dest, file)
        print(path)
        m_time = os.path.getmtime(path)
        if datetime.fromtimestamp(m_time)>time_24hours_ago:
            shutil.copy(path, dst)
            print(dst)




def main():
    src= r"C:\Users\sajibhaskaran\Desktop\folderA"
    dest= r"C:\Users\sajibhaskaran\Desktop\folderB"
    modified_time(src, dest)



if __name__ == "__main__":
          main()
