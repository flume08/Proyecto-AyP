class Item:
    def __init__(self,name,price,sell=0):
        self.name = name
        self.price = float(price)*1.16
        self.sell = sell
        self.stock = self.stock - self.sell
    def show_attributes(self):
        print('\n')
        print(f'Name ==> {self.name}')
        print(f'Type ==> {self.type}')
        print(f'Price ==> {self.price}')
        print(f'Stock ==> {self.stock}')
        print(f'Sells ===> {self.sell}')
    def add_sell(self):
        self.sell +=1
    def rest_stock(self):
        self.stock -=1
    def dicc(self):
        return{
            'name':self.name,
            'price':self.price*(25/29),
            'type':self.type,
            'stock':self.stock,
            'sell':self.sell
        }
class FoodRestaurant(Item):
    type = 'Comida de restaurant'
    stock = 20
class FoodFast(Item):
    type = 'Comida Rapida'
    stock = 25
class DrinkAlcohol(Item):
    type ='Bebida Alcoholica'
    stock = 20
class DrinkNonAlcoholic(Item):
    type = 'Bebida no alcoholica'
    stock = 30