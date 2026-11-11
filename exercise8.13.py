def build_profile(first, last, **user_info):
    profile = {
        "nama_depan": first,
        "nama_belakang": last
    }

    for key, value in user_info.items():
        profile[key] = value

    return profile

my_profile = build_profile(
    "Naila",
    "Azis",
    usia=19,
    kota="Surakarta",
    jurusan="Teknik Industri"
)

print("PROFIL PENGGUNA")
print(my_profile)
