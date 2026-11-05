favorite_languages = {
    "lisa": "Thailand",
    "naila": "Bahasa",
    "jennie": "Korea",
    "Jisoo": "Tagalog",
    "rose": "Korea"
}

# Daftar orang yang harus mengikuti polling
people = ["lisa", "naila", "jennie", "Jisoo", "rose"]

# Memeriksa siapa yang sudah mengikuti polling
print("HASIL PEMERIKSAAN POLLING:\n")

for name in people:
    if name in favorite_languages:
        print(f"Terima kasih {name.title()}, sudah mengikuti polling.")
    else:
        print(f"{name.title()}, silakan ikuti polling bahasa favorit.")
