class Item:
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price
    def item(self):
        return(self.name, self.price)
    
class ShoppingCart(Item):
    def add(item: Item):
        cart = []
        cart.append(item)
        return(cart)

bike = Item('Hero', 3000)
phone = Item('iPhone', 1000)
arr = ShoppingCart(bike)
print(bike.item())
print(arr.add())

