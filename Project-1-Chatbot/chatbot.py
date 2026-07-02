print("Welcome to AI Chatbot!")

while True:
    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user == "help":
        print("Bot: You can say hello, hi, how are you, your name, or bye.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
