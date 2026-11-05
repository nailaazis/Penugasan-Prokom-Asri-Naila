pet1 = {
    "jenis_hewan": "Hamster",
    "nama_pemilik": "Naila"
}

pet2 = {
    "jenis_hewan": "Anjing",
    "nama_pemilik": "Jeva"
}

pet3 = {
    "jenis_hewan": "Kucing",
    "nama_pemilik": "Alkina"
}

pets = [pet1, pet2, pet3]

# Menampilkan informasi hewan
for pet in pets:
    print("\nInformasi Hewan Peliharaan:")
    print("Jenis hewan:", pet["jenis_hewan"])
    print("Nama pemilik:", pet["nama_pemilik"])
