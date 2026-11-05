favorite_places = {
    "Naila": ["Mekkah", "Paris", "Jepang"],
    "Anya": ["Bali", "Bandung"],
    "Dita": ["Korea Selatan", "Swiss", "Maldives"]
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name}:")

    for place in places:
        print("-", place)