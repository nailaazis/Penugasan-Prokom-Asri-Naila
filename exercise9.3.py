class Users:
    def __init__(self, first_name, last_name, age, city, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.hobby = hobby
        
    def describe_user(self):
        print("Informasi User:")
        print(f"Nama depan: {self.first_name}")
        print(f"Nama belakang: {self.last_name}")
        print(f"Usia: {self.age}")
        print(f"Kota: {self.city}")
        print(f"Hobi: {self.hobby}")
    
    def greet_user(self):
        print(f"Halo {self.first_name} {self.last_name}, selamat datang di page berikut!")
    
user1 = Users("Naila", "Azis", "19", "Jakarta", "Menyanyi")
user2 = Users("Khalisha", "Fayza", "18", "Jogja", "Kulineran")
user3 = Users("Anya", "Channiswara", "17", "Jatinangor", "Beli bunga")

print("User 1")
user1.describe_user()
user1.greet_user()

print("\nUser 2")
user2.describe_user()
user2.greet_user()

print("\nUser 3")
user3.describe_user()
user3.greet_user()