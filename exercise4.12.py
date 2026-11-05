makanans = ["Geprek", "Dimsum", "Cireng"]

friend_makanans = makanans[:]
makanans.append("Sate")
friend_makanans.append("Ketoprak")

print("Makanan kesukaanku adalah:")

for makanan in makanans:
    print(makanan)
    
print("\nMakanan kesukaan temanku:")
for makanan in friend_makanans:
    print(makanan)