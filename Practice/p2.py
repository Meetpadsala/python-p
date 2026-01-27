import os
import shutil
import datetime


# source = "C:/Users/Acer/OneDrive/Documents/python"
# dest = "C:/Users/Acer/OneDrive/Documents/python/backups"


# today = datetime.datetime.today()
# time = today.strftime("%Y%m%d_%H%M%S")

# file_name = os.path.join(dest,f"backup{time}")
# shutil.make_archive(file_name,'zip',source)

# print(source,dest)
# print("Done")



# src = os.listdir(".") 

# for i in src :
#     print(i)



# def count_files(path):
#     files = os.listdir(path)
#     return len(files)

# print(count_files("."))



def main(path):
    files = os.listdir(path)
    return len (files)

if __name__ == "__main__":
    print(main("."))









