guests = ["Alkina", "Dita", "Rohmad"]

print("Aku menemukan ukuran meja yang lebih besar, jadi aku bisa mengundang lebih banyak orang!")
guests.insert(0, "Davina")
guests.insert(2, "Fahira")
guests.append("Arsyad")

print("\nUndangan ulang tahun yang baru:")
for guest in guests:
    print(f"Halo {guest}, kamu aku undang ke acara ulang tahunku, tolong dateng yaa!")