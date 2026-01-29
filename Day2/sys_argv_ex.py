import sys
import os 
import argparse

# a = sys.argv[1]
# b = sys.argv[2]

# print(a+b)


# a = int(sys.argv[1])
# b = int(sys.argv[2])

# print(a+b)

# path = sys.argv[1]
# files = os.listdir(path)

# print(len(files))
# print(files)




# parser = argparse.ArgumentParser()

# parser.add_argument("a", type=int)
# parser.add_argument("b",type=int)


# args = parser.parse_args()

# print(args.a + args.b)


parser = argparse.ArgumentParser(description="Count files in folder")
parser.add_argument("path", help="Folder path")

args = parser.parse_args()

files = os.listdir(args.path)
print("Total files:", len(files))










