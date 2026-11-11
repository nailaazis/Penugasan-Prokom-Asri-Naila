class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Nama restorant: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} sudah buka!")
        
restaurant = Restaurant("Dapur Bundari", "Masakan Makassar")

print("Nama restoran:", restaurant.restaurant_name)
print("Jenis masakan:", restaurant.cuisine_type)

print("\nInformasi Restoran:")
restaurant.describe_restaurant()

print("\nStatus Restoran:")
restaurant.open_restaurant()