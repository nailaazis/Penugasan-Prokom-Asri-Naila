class Users:
    def __init__(self, first_name, last_name, age, city, login_attemps):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0
        
    def describe_user(self):
        print("Informasi User:")
        print(f"Nama depan: {self.first_name}")
        print(f"Nama belakang: {self.last_name}")
        print(f"Usia: {self.age}")
        print(f"Kota: {self.city}")
        
    def greet_user(self):
        print(f"Halo {self.first_name} {self.last_name}!")
            
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user = Users("Naila", "Azis", "19", "Jakarta", "Menyanyi")

print("Jumlah login awal:", user.login_attempts)

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print("Jumlah login sekarang:", user.login_attempts)

user.reset_login_attempts()
print("Jumlah login setelah reset:", user.login_attempts)    
        