cities = {
    "Surakarta": {
        "negara": "Indonesia",
        "populasi": "lebih dari 500.000 jiwa",
        "fakta": "Kota Batik",
        "makanan": "Nasi Liwet",
        "bahasa": "Bahasa Indonesia"
    },

    "Tokyo": {
        "negara": "Jepang",
        "populasi": "sekitar 14 juta jiwa",
        "fakta": "Ibu kota Jepang",
        "makanan": "Sushi",
        "bahasa": "Bahasa Jepang"
    },

    "Paris": {
        "negara": "Prancis",
        "populasi": "sekitar 2 juta jiwa",
        "fakta": "Kota Menara Eiffel",
        "makanan": "Croissant",
        "bahasa": "Bahasa Prancis"
    }
}

print("=== INFORMASI KOTA ===")

for city, information in cities.items():
    print(f"\nNama Kota: {city}")
    print("-" * 30)
    print("Negara:", information["negara"])
    print("Populasi:", information["populasi"])
    print("Fakta menarik:", information["fakta"])
    print("Makanan khas:", information["makanan"])
    print("Bahasa:", information["bahasa"])