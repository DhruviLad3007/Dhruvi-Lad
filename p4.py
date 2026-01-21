balance = 5000
withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")
