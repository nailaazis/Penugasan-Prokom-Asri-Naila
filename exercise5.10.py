user_sekarang = ["naila", "alkina", "khalisha", "jeva", "natha"]
user_baru = ["naila", "queena", "naval", "zaki", "hafizh"]

user_sekarang_lower = []
for user in user_sekarang:
    user_sekarang_lower.append(user.lower())

for user_baru in user_baru: 
    if user_baru.lower() in user_sekarang_lower:
        print(f"Maaf, {user_baru} sudah terisi")
    else:
        print(f"{user_baru} masih tersedia.")