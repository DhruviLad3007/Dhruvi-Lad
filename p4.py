file = open("sample.txt", "w")

for i in range(1, 6):
    sentence = input(f"Enter sentence {i}: ")
    file.write(sentence + "\n")

file.close()
print("Data written successfully")
