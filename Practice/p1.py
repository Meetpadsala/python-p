import os
import shutil
import datetime


source = "C:/Users/Acer/OneDrive/Documents/python"
dest = "C:/Users/Acer/OneDrive/Documents/python/backups"

today = datetime.datetime.today()
time = today.strftime("%Y%m%d_%H%M%S")

backup_file_name = os.path.join(dest,f"backup{time}")
shutil.make_archive(backup_file_name ,'zip',source)

print(source,dest)
print("Done")

