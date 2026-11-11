class Users:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        
    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Usia: {self.age}")
        print(f"Kota: {self.city}")

class Admin(Users):

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)

        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("\nHak akses administrator:")

        for privilege in self.privileges:
            print(f"- {privilege}")
            
admin = Admin("Naila", "Azis", 19, "Jakarta")

admin.describe_user()
admin.show_privileges()
            