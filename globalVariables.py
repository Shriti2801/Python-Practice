x="Shriti"
def myfunc():
    print("My name is "+x)
myfunc()

#local variable

x = "hello"

def myfunc():
  x = "Hi"
  print(x+" Nice to meet you")      #local var is printed first

myfunc()

print(x+" nice to meet you")        #followed by global variable
