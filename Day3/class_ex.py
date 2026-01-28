import os

class FileManager:
    def __init__(self,path):
        self.path = path
    

    def count_file(self):
        files = os.listdir(self.path)
        return len(files)
    


folder = input("Enter folder path :").strip()
fm = FileManager(folder)
print("Total file :", fm.count_file())






