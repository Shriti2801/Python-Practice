# __init__() function to assign values to object properties

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("John",30)

print(p1.name)
print(p1.age)