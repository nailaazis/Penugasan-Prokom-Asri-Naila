class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Nama restorant: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} sudah buka!")
        
restaurant1 = Restaurant("Dapur Bundari", "Masakan Makassar")
restaurant2 = Restaurant("Dapoer Baroe", "Aneka Pastry dan Kue")
restaurant3 = Restaurant("Philadelphia", "Aneka olahan salmon dan sushi")

print("Restoran 1")
restaurant1.describe_restaurant

print("\nRestoran 2")
restaurant2.describe_restaurant

print("\nRestoran 3")
restaurant3.describe_restaurant