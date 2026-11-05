guests = ["Alkina", "Dita", "Rohmad", "Davina", "Fahira", "Arsyad"]

print("Maaf sebelumnya teman-teman, ternyata meja yang mau aku gunakan tidak bisa digunakan sesuai waktu di undangan. Jadi aku hanya bisa undang 2 orang saja.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, kamu tidak bisa hadir di acara ulang tahunku. Maaf sekali.")

print("\nUndangan ulang tahun yang baru:")
for guest in guests:
    print(f"Halo {guest}, kamu aku undang ke acara ulang tahunku. tolong datang yaa!")
    
del guests[0]
del guests[0]

print("\n Daftar tamu terbaru:")
print(guests)