from product import Product
from product_manager import ProductManager


manager = ProductManager()

product1 = Product("Laptop", 3500, 5)
product2 = Product("Telefon", 2000, 10)
product3 = Product("Casti", 250, 15)
product4 = Product("Mouse", 120, 20)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)

print("Produse disponibile:")
manager.display_products()

print(f"\nValoarea totala a inventarului: {manager.total_inventory_value()} lei")
print("\nEliminam produsul Telefon:")
manager.remove_product("Telefon")

print("\nProduse dupa eliminare:")
manager.display_products()