usernames = ["admin", "naila", "alkina", "khalisha", "jeva"]

for username in usernames:
    if username == "admin":
        print("Halo admin! Mau liat hasil laporan kah?")
    else:
        print(f"Halo {username}, makasih udah login kembali :3")
        
else:
    print("Kita perlu mencari pengguna lain")
    
usernames = []
if usernames:
    for username in usernames:
        print(f"Halo {username}")
else:
    print("Kita perlu mencari pengguna lain!")