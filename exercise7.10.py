polling_active = True
poll_results = {}
while polling_active:
    name = input("\nSiapa namamu?")
    response = input("Kalau kamu bisa mendatangi suatu tempat di dunia, kamu mau ke mana?")
poll_results[name] = response

repeat = input("Maukah kamu membiarkan orang lain merespon? (yes/ no)")
if repeat.lower() == "no":
    polling_active = False
    
print("\n--- Poll Results ---")
for name, respon in poll_results.item():
    print(f"{name.title()} would love to visit {response.title()}.")