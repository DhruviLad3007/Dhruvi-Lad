light = input("Enter traffic light color (Red/Yellow/Green): ").lower()

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go")
else:
    print("Invalid color")
