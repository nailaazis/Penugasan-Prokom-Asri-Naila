messages = [
    "Selamat pagi",
    "Semoga harimu menyenangkan",
    "Semangat kuliahnya",
    "Have a great day!"
]

sent_messages = []
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()

        print(f"Mengirim pesan: {current_message}")

        sent_messages.append(current_message)
send_messages(messages, sent_messages)

print("\nList pesan yang belum dikirim:")
print(messages)

print("\nList pesan yang sudah dikirim:")
print(sent_messages)
