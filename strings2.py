#slicing of strings

color='Norwegian Blue'
print(color)
print(color[3:5])
print(color[:9])        #we can skip off the start value when its 0.
print(color[0:9])       #as we get the same result
print(color[10:14])     #Blue
print(color[10:])       #last value can be skipped

print(color[:6])
print(color[6:])
print(color[:6] + color[6:])
print(color[:])
print()
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters)
print(letters[1]+letters[0]+letters[3])

#                   1
#         012345678901234
color = "Norwegian Blue"

print(color[0:6:2])    # Nre
print(color[0:6:3])    # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
