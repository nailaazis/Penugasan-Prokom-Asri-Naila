def make_sandwich(*items):
    print("\nSandwich yang dipesan:")
    
    for item in items:
        print(f" - {items}")
        
    print("Sandwich berhasil dibuat!")
    
make_sandwich("Keju")
make_sandwich("Daging", "Selada", "Tomat")
make_sandwich("Telur", "Keju", "Sosis", "Selada", "Mayones")