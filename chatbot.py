# Basic Chatbot

print("🤖 ChatBot: Hello! Type 'bye' to exit.")

while True:

    user_input = input("You: ").lower()

    if user_input == "hello":
        print("🤖 ChatBot: Hi there!")

    elif user_input == "how are you":
        print("🤖 ChatBot: I am fine. Thank you!")

    elif user_input == "what is your name":
        print("🤖 ChatBot: My name is Python Bot.")

    elif user_input == "bye":
        print("🤖 ChatBot: Goodbye!")
        break

    else:
        print("🤖 ChatBot: Sorry, I don't understand.")