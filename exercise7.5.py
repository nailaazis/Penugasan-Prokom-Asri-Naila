while True:
    usia_input = input("Masukkan usia (atau ketik quit untuk selesai): ")

    if usia_input.lower() == "quit":
        break

    usia = int(usia_input)

    if usia < 3:
        print("Tiket gratis!")
    elif usia <= 12:
        print("Harga tiket adalah $10.")
    else:
        print("Harga tiket adalah $15.")

print("Terima kasih sudah menggunakan program!")
