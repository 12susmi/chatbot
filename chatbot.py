def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("Chatbot: Hi there!")
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm fine, thanks! How about you?")
        elif user_input in ["i am fine", "i'm fine", "good"]:
            print("Chatbot: That's great to hear!")
        elif user_input in ["what is your name", "your name?"]:
            print("Chatbot: I'm ChatBot9000!")
        elif user_input in ["what can you do", "help"]:
            print("Chatbot: I can answer simple greetings and questions.")
        elif user_input in ["tell me a joke", "joke"]:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")


chatbot()