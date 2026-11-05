gunung = ["Merbabu", "Merapi", "Lawu", "Rinjani", "Semeru"]
print("Gunung pertama yang ingin aku daki:", gunung[0])
print("Gunung terakhir yang ingin aku daki:", gunung[-1])

gunung[2] = "Bromo"
print("\n Gunung yang ingin aku daki:", gunung)

gunung.append("Sumbing")
print("\n List terbaru gunung yang ingin aku daki:", gunung)

gunung.insert(1, "Slamet")
print("\n List terbaru gunung yang ingin aku daki:", gunung)
del gunung[4]
print("\n List terbaru gunung yang ingin aku daki:", gunung)

removed_gunung = gunung.pop(3)
print(f"\n Gunung yang dihapus: {removed_gunung}")
print("\n List gunung terbaru:", gunung)

gunung.remove("Merbabu")
print("List gunung terbaru:", gunung)

print(sorted(gunung))
print("List gunung terbaru:", gunung)
print("List gunung terbaru (terbalik):", sorted(gunung, reverse=True))

gunung.reverse()
print("List gunung terbaru:", gunung)

gunung.sort()
print("List gunung terbaru:", gunung)
gunung.sort(reverse=True)
print("List gunung terbaru (dibalik):", gunung)

print("\n Jumlah gunung yang ingin aku daki:", len(gunung))


