locations = ["Mekkah", "Venice", "Paris", "Edinburgh", "Swiss"]
print("List lokasi yang ingin dikunjungi:", locations)
print(sorted(locations))

locations.reverse()
print("List lokasi yang terbalik:", locations)
locations.reverse()
print("List yang telah dibalik:", locations)
locations.sort()
print("List lokasi (telah berurutan):", locations)

# di buku panduan diminta untuk kembali mereverse list locationsnya
locations.sort(reverse=True)
print("List lokasi terbaru (terbalik):", locations)
