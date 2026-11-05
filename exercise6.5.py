rivers = {
    "Nile": "Egypt",
    "Yangtze": "China",
    "Seine": "France"
}

print("INFORMASI SUNGAI:\n")

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")
print("\nNama Sungai:")

for river in rivers.keys():
    print(river)

print("\nNama Negara:")
for country in rivers.values():
    print(country)
