from pathlib import Path 

path = Path("newdata.txt")
path.touch()
print(path.exists())


folder = Path("data")
folder.mkdir()
print(folder.exists())

