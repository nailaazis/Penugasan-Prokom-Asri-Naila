topping = ""

while topping != "quit":
    topping = input("Masukkan topping pizza (atau quit untuk selesai): ")

    if topping != "quit":
        print(f"Topping {topping} akan ditambahkan ke pizza kamu.")

print("Pesanan pizza selesai!")