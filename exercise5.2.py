nama = "Naila"

print("String equality:")
print(nama == "Naila")
print(nama == "Anna")

print("\nString inequality:")
print(nama != "Anna")
print(nama != "Naila")

# lower
city = "JAKARTA"

print("\nUsing lower():")
print(city.lower() == "jakarta")
print(city.lower() == "bandung")

# numerical
number = 15

print("\nNumerical tests:")
print(number == 15)
print(number != 15)
print(number > 10)
print(number > 20)
print(number < 20)
print(number < 10)
print(number >= 15)
print(number >= 20)
print(number <= 15)
print(number <= 10)

# and & or
age = 20

print("\nUsing and:")
print(age > 18 and age < 30)
print(age > 18 and age > 30)

print("\nUsing or:")
print(age < 18 or age == 20)
print(age < 18 or age > 30)

# item list
foods = ["Ayam goreng", "Ketupat sayur", "Seblak"]
print("\nItem di list:")
print("Ayam goreng" in foods)
print("Seblak" in foods)

# tes apakah item tidak ada di list
print("\nItem tidak ada di list:")
print("Seblak" not in foods)
print("Ketupat sayur" not in foods)