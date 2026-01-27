import shutil
import datetime
import os


def backup_file(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name,'zip',source)


source = "C:/Users/Acer/OneDrive/Documents/python"
destination = "C:/Users/Acer/OneDrive/Documents/python/backups"

backup_file(source,destination)




# bash_path = os.path.expanduser("~")
# folder_path = os.path.join(bash_path,"logs")
# file_path = os.path.join(folder_path,"app.py")

# if not os.path.exists(folder_path):
#     os.mkdir(folder_path)


# file = open(file_path,"a")
# file.write("hello")
# file.close()


# print("Done")





