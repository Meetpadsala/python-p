import os

# Current working directory
print(os.getcwd())

# Folder create
os.mkdir("backup_folder")  # create folder

# Folder exist check
if os.path.exists("backup_folder"):
    print("Folder exists!")

# List files in folder
print(os.listdir("."))

# Delete empty folder
os.rmdir("backup_folder")
