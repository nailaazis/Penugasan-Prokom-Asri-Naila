person1 = {
    "nama_depan": "Naila",
    "nama_belakang": "Azis",
    "usia": 19,
    "kota": "Surakarta"    
}

person2 = {
    "nama_depan": "Alkina",
    "nama_belakang": "Guntoro",
    "usia": 18,
    "kota": "Surakarta"    
}

person3 = {
    "nama_depan": "Jezreel",
    "nama_belakang": "Varda",
    "usia": 18,
    "kota": "Surakarta"    
}
people = [person1, person2, person3]

for person in people:
    print("\nInformasi Seseorang:")
    print("Nama depan:", person["nama_depan"])
    print("Nama belakang:", person["nama_belakang"])
    print("Usia:", person["usia"])
    print("Kota:", person["kota"])