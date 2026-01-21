items = ["Python", "Java", "C++"]

file = open("sample.txt", "a")
for item in items:
    file.write(item + "\n")
file.close()

print("Data appended successfully")
