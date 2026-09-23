from product import Product
from product_manager import ProductManager
from cart import Cart
import random


manager = ProductManager()

product1 = Product("Laptop Gaming", 3500, 3)
product2 = Product("Smartphone", 2000, 8)
product3 = Product("Casti Wireless", 250, 12)
product4 = Product("Mouse Gaming", 120, 15)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)


print("\nEliminam produsul Smartphone:")
manager.remove_product("Smartphone")

print("\nProduse dupa eliminare:")
manager.display_products()

cart = Cart()

selected_products = random.sample(manager.products, 3)

for product in selected_products:
    cart.add_product(product)

print("\nContinutul cosului:")
cart.display_cart()

print(f"\nValoarea totala de plata: {cart.calculate_total()} lei")