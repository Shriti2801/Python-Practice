class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = 20
    def myfunc(self):
        print("Hello, my name is " + self.name)
    
p1 = Student("Ram",20)
p1.myfunc()