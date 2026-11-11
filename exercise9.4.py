class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Nama restorant: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} sudah buka!")
        
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number
                
restaurant = Restaurant("Dapur Bundari", "Masakan Makassar")
print("Jumlah pelanggan awal:", restaurant.number_served)

restaurant.number_served = 25
print("Jumlah pelanggan sekarang:", restaurant.number_served)

restaurant.set_number_served(40)
print("Setelah menggunakan set_number_served():",
      restaurant.number_served)

print.increment_number_served(15)
print("Setelah menggunakan increment_number_served():",
      restaurant.number_served)