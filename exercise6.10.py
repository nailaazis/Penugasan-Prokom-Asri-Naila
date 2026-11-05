favorite_numbers = {
    "Naila": [7, 10, 21],
    "Khalisha": [5, 8],
    "Zizi": [3, 9, 12],
    "Anya": [4, 15],
    "Dita": [2, 6, 11]
}

for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name}:")

    for number in numbers:
        print("-", number)
