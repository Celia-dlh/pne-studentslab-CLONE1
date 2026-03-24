class Product:
    def __init__(self, name , price):
        self.name = name
        self.price = price

    def get_information(self):
        return f"Product: {self.name} | Price: {self.price}"


class Client:
    def __init__(self, name , email ):
        self.name = name
        self.email = email
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def compute_total(self):
        total = 0
        for product in self.cart:
            total += product.price
        return total


class VIPClient(Client):
    def __init__ (self, name , email, discount):
        super().__init__(name , email)
        self.discount = discount

    def compute_total(self):
        total = super().compute_total()
        discounted_total = total * (1 - self.discount / 100)
        return int(discounted_total)

if __name__ == "__main__":

    product1 = Product("Laptop" , 1200)
    product2 = Product("Chair" , 90)
    product3 = Product("Scarf" , 24)

    client1 = VIPClient("Alice", "alice@gmail.com" , 20 )
    client2 = Client("Paul", "paul@gmail.com")

    client1.add_to_cart(product1)
    client1.add_to_cart(product2)

    client2.add_to_cart(product2)
    client2.add_to_cart(product3)

    print(f"Customer (VIP): {client1.name}")
    print(f"Total to pay: {client1.compute_total()}")

    print(f"Customer : {client2.name}")
    print(f"Total to pay: {client2.compute_total()}")
