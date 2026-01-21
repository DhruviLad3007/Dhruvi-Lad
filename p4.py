try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(x / y)
except ValueError:
    print("Error: Invalid input")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
