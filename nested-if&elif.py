print("Welcome to the rollercoaster")
print()
height = int(input("What is your height in cm?\n"))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("You have to pay 5$")
    elif age <=18:
        print("You have to pay 7$")
    else:
        print("You have to pay 12$")
else:
    print("Sorry! You cannot ride the rollercoaster")