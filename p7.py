old_word = input("Enter old word: ")
new_word = input("Enter new word: ")

file = open("sample.txt", "r")
content = file.read()
file.close()

content = content.replace(old_word, new_word)

file = open("sample.txt", "w")
file.write(content)
file.close()

print("Word replaced successfully")

