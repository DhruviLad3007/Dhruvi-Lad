import os

path = "."   # current directory
files = os.listdir(path)

for file in files:
    print(file)
