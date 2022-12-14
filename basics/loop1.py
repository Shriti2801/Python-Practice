number = int(input("enter the number: "))
count = 1

print("The table of ",number)
while count<11:
    print(number,'x', count, '=', number*count)
    count += 1
