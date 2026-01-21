try:
    x = int(input("Enter number: "))
    y = int(input("Enter number: "))
    print(x / y)
except Exception as e:
    file = open("error_log.txt", "a")
    file.write(str(e) + "\n")
    file.close()
