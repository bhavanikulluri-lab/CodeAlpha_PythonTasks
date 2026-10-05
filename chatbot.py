def get_reply(msg):
    msg = msg.lower().strip()
    if msg in ("hello", "hi"):
        return "Hi!"
    elif msg == "how are you":
        return "I'm fine, thanks!"
    elif msg in ("bye", "goodbye"):
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

print("Chatbot started! Type 'bye' to exit.")
while True:
    user = input("You: ")
    reply = get_reply(user)
    print("Bot:", reply)
    if user.lower().strip() in ("bye", "goodbye"):
        break