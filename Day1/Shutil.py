import shutil

# File copy
shutil.copy("data.txt", "backup/data_copy.txt")

# Folder copy (recursive)
shutil.copytree("project", "project_backup")

# Move file/folder
shutil.move("data.txt", "backup/")

# Delete folder (non-empty)
shutil.rmtree("old_backup")
