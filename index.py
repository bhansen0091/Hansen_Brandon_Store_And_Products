import store, product


store_1 = store.Store("Buy More")

store_1.add_product(1,"apple",.51,"produce")
store_1.add_product(2,"mop",10.99,"cleaning product")

# store_1.print_info(store_1.products)

product.Product.print_info(store_1.products)

# store_1.display_inventory()

print("waiting")


