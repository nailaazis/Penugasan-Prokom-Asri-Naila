class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()

class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Baterai mobil: {self.battery_size} kWh")

    def get_range(self):
        if self.battery_size == 40:
            battery_range = 150
        elif self.battery_size == 65:
            battery_range = 225
        else:
            battery_range = 0

        print(
            f"Mobil dapat menempuh sekitar {battery_range} "
            "mil dengan baterai penuh."
        )

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print("Baterai berhasil di-upgrade menjadi 65 kWh.")
        else:
            print("Baterai sudah menggunakan kapasitas 65 kWh.")

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery = Battery()

my_car = ElectricCar("Nissan", "Leaf", 2024)

print("Mobil listrik:")
print(my_car.get_descriptive_name())

print("\nSebelum upgrade:")
my_car.battery.describe_battery()
my_car.battery.get_range()

print("\nSetelah upgrade:")
my_car.battery.upgrade_battery()
my_car.battery.describe_battery()
my_car.battery.get_range()
