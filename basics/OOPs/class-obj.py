class Books:
    def __init__(self,type):
        self.type = type
type1 = Books("Magic")
type2 = Books("Business")

print("I like reading books about {}.".format(type1.type))
print("I also like reading books about {}.".format(type2.type))
        