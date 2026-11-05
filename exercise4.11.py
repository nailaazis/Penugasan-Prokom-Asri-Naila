pizzas = ["Pepperoni", "Keju", "Ayam"]

friend_pizzas = pizzas[:]
pizzas.append("Nanas")
friend_pizzas.append("Daging")

print("Pizza kesukaanku adalah:")

for pizza in pizzas:
    print(pizza)
    
print("\nPizza favorit temanku:")
for pizza in friend_pizzas:
    print(pizza)