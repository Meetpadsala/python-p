import os


folder_path = input("Enter folder path :")

def count_files(folder_path):
    files = os.listdir(folder_path)
    return len (files)


print("Total count :" ,count_files(folder_path) )












