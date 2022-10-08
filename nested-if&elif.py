print("Welcome to the rollercoaster")
print()
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("You have to pay 5$")
    elif age <=18:
        bill = 7
        print("You have to pay 7$")
    else:
        bill = 12
        print("You have to pay 12$")
    photos = input("Do you want photos? Y or N\n")   
    if photos == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
        
else:
    print("Sorry! You cannot ride the rollercoaster")