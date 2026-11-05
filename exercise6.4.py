glossary = {
    "Variable": "Tempat untuk menyimpan data.",
    "List": "Kumpulan data yang dapat diubah.",
    "Tuple": "Kumpulan data yang tidak dapat diubah langsung.",
    "Loop": "Perintah untuk mengulang suatu proses.",
    "Dictionary": "Struktur data yang menyimpan pasangan key dan value."
}

print("KAMUS ISTILAH PYTHON\n")

for word, meaning in glossary.items():
    print(f"{word}:")
    print(f"    {meaning}\n")