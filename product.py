

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change = 0.1, is_increased = True):
        if is_increased:
            self.price = self.price + (self.price * percent_change) 
        else:
            self.price = self.price - (self.price * percent_change) 

    def print_info(self, id):
        
        # print(f"Product: {self.name} | Price: ${self.price} | Category: {self.category}")
        return self

    def __repr__(self):
        return f"[{self.name}, {self.price}, {self.category}]"

    def __str__(self):
        return f"Name: {self.name} | Price: ${self.price} | Category: {self.category}"