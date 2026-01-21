try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Division by zero error")
except Exception as e:
    print("Error:", e)
