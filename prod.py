##Write a class called Product. The class should have fields called name, amount, and price,
#holding the product’s name, the number of items of that product in stock, and the regular
#price of the product. There should be a method get_price that receives the number of
#items to be bought and returns a the cost of buying that many items, where the regular price
#is charged for orders of less than 10 items, a 10% discount is applied for orders of between
#10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should
#also be a method called make_purchase that receives the number of items to be bought and
#decreases amount by that much.

class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amout = amount
        self.price = price

    def get_price(self, item):
        self.item = item
        if item <= 10:
            cost = item * self.price
            print(cost)
        if item> 10 and item<=99:
            discount = (item * self.price)*0.1
            cost = (item * self.price)-discount
            print(cost)

customer = Product("soap", 20, 5)
print(customer.get_price(2))
