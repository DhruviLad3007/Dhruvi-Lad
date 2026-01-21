file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

data = file1.read() + "\n" + file2.read()

file1.close()
file2.close()

file3 = open("merged.txt", "w")
file3.write(data)
file3.close()

print("Files merged successfully")
