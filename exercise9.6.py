class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name):
        super().__init__(restaurant_name, "Es Krim")
        self.flavors = ["Vanila", "Coklat", "Stroberi", "Matcha"]

    def display_flavors(self):
        print("\nRasa es krim yang tersedia:")

        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream = IceCreamStand("Sweet Ice Cream")

ice_cream.describe_restaurant()
ice_cream.display_flavors()
