from product import Product


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_id, name, price, category):
        new_product = Product(product_id, name, price, category)
        new_product_dict = {
            "id": new_product.product_id,
            "name": new_product.name,
            "price": new_product.price,
            "category": new_product.category
        }
        self.products.append(new_product_dict)
        return self

#---------------------------------------------------------
        # new_product = Product(new_product.name, new_product.price, new_product.category)
        # self.products.append(new_product)
        # return self
#---------------------------------------------------------

    def sell_product(self, id):
        pass

    def inflation(self, percent_increase):
        pass

    def set_clearance(self, category, percent_discount):
        pass

    def display_inventory(self):
        for product_dict in self.products:
            for key, value in product_dict.items():
                print(key, ":", value)
            print("\n" + "*"*80)
        return self
#---------------------------------------------------------
        # for id, info in self.products.items():
        #     print("\n\n" + "*"*80 + "\n" + f"\nID: {id}")
        #     for key in info:
        #         print(f"{key}: {info[key]}")
#---------------------------------------------------------        
        # for key in self.products:
        #     print(f"ID #{key}")
        #     for sub_key in self.products[key]:
        #         print(f"{sub_key}: {self.products[key][sub_key]}")
        #     print("*"*80)
        #         # print(f" {self.products} | {key} | {self.products[key]} | {sub_key}")
#---------------------------------------------------------        
        # for product in self.products:
        #     product.print_info()

    def __repr__(self):
        return f"{self.name} {self.products}"
    
    def __str__(self):
        return f"Store Name: {self.name} | Products: {self.products}"