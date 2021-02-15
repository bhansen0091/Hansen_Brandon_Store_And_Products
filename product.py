

class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change = 0.1, is_increased = True):
        if is_increased:
            self.price = self.price + (self.price * percent_change) 
        else:
            self.price = self.price - (self.price * percent_change) 

    def print_info(product_list):
        for dict in product_list:
            for key, value in dict.items():
                print(f"{key} {value}")
        # print(f"Product: {product_list} ")
        return

    def __repr__(self):
        return f"[{self.name}, {self.price}, {self.category}]"

    def __str__(self):
        return f"Name: {self.name} | Price: ${self.price} | Category: {self.category}"