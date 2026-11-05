foods = ("Ayam goreng", "Rendang", "Pasta", "Sup")
print("Menu Buffet:")

for food in foods:
    print(food)
    
print("\nMencoba mengubah menu")
try:
    foods[0] = "Gorengan"
except TypeError as error:
    print("Python tidak memperbolehkan mengganti item tuple.")
    print("Error:", error)
    
foods = ("Gorengan", "Sup", "Dendeng balado", "Pasta")
print("\nMenu yang telah direvisi:")
for food in foods:
    print(food)