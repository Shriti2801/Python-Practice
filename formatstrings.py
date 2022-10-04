#format() takes passed arguments, formats them and places them where the {} are
#{} are placeholders

age=22                            
text="I am Shriti, I am {}"
print(text.format(age))

#when multiple arguments are passed

quantity=10
price=10
date=10
text="I want {} packets of chocolates for {} dollars on the {} of next month."
print(text.format(quantity,price,date))

#{0} using index values 

price=10
date=10
quantity=10
text="I want {2} packets of chocolates for {0} dollars on the {1} of next month."
print(text.format(quantity,price,date))