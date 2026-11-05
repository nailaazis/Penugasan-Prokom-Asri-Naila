# conditional
topping = ""

while topping != "quit":
    topping = input("Masukkan topping (quit untuk selesai): ")

    if topping != "quit":
        print(f"Topping {topping} ditambahkan.")
        
# active variable
aktif = True

while aktif:
    topping = input("Masukan topping (quit untuk selesai):")
    if topping == "quit":
        aktif = False
    else:
        print(f"Topping {topping} ditambahkan.")

# Break Statement

while True:
    topping = input("Masukkan topping (quit untuk selesai): ")

    if topping == "quit":
        break

    print(f"Topping {topping} ditambahkan.")

print("\nProgram selesai!")
