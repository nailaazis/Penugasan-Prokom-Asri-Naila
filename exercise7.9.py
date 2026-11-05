sandwich_orders = ["daging", "ayam", "sayuran", "kambing"]
finished_sandwiches = []

while "kambing" in sandwich_orders:
    sandwich_orders.remove("kambing")
    
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    
    finished_sandwiches.append(current_sandwich)

print("\nFinished Sandwiches")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")