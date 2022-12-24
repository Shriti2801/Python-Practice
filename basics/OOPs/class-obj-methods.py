class Clothing:
    def __init__(self,category):
        self.category = category

    def buy(self):
        print("I want to buy a {}.".format(self.category))
        # print("Can you buy me a {}".format(self.category))

category1 = Clothing("Jacket")
category2 = Clothing("Cap")

category1.buy()
category2.buy()




