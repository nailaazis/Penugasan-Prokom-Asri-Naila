cities = {
    "Surakarta": {
        "negara": "Indonesia",
        "populasi": "lebih dari 500.000 jiwa",
        "fakta": "Dikenal sebagai Kota Batik."
    },

    "Tokyo": {
        "negara": "Jepang",
        "populasi": "sekitar 14 juta jiwa",
        "fakta": "Merupakan ibu kota Jepang."
    },

    "Paris": {
        "negara": "Prancis",
        "populasi": "sekitar 2 juta jiwa",
        "fakta": "Dikenal dengan Menara Eiffel."
    }
}

for city, information in cities.items():
    print(f"\nInformasi Kota {city}:")
    print("Negara:", information["negara"])
    print("Populasi:", information["populasi"])
    print("Fakta menarik:", information["fakta"])
