source = open("sample.txt", "r")
backup = open("backup.txt", "w")

backup.write(source.read())

source.close()
backup.close()

print("Backup created successfully")
