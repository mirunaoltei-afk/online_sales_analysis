class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(
            f"Produs: {self.name}, "
            f"Preț: {self.price} lei, "
            f"Cantitate: {self.quantity}"
        )

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity