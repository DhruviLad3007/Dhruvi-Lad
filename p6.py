search_word = input("Enter word to search: ")

file = open("sample.txt", "r")
for line in file:
    if search_word in line:
        print(line.strip())
file.close()
