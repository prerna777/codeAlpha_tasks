# Advanced Rule-Based Chatbot with Common User Questions

def chatbot():
    print("🤖 Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        # Greetings
        if user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hi there!")
        
        elif user_input in ["how are you", "how r u"]:
            print("🤖 Chatbot: I'm good! Thanks for asking 😊")
        
        elif user_input in ["what is your name", "who are you"]:
            print("🤖 Chatbot: I'm a Python chatbot created for an internship project 🤖")

        # Common human questions
        elif user_input in ["what are you doing", "wyd"]:
            print("🤖 Chatbot: I'm chatting with you right now 😄")

        elif user_input == "tell me a joke":
            print("🤖 Chatbot: Why did the computer sneeze? Because it had a virus 🤧")

        elif user_input in ["where do you live", "what is your address"]:
            print("🤖 Chatbot: I live inside your computer 😎")

        elif user_input in ["what can you do", "your abilities"]:
            print("🤖 Chatbot: I can chat with you and answer simple questions!")

        elif user_input == "who created you":
            print("🤖 Chatbot: I was created by a Python learner for an internship task 👩‍💻")

        elif user_input in ["are you a robot", "are you human"]:
            print("🤖 Chatbot: I'm a cute digital robot 🤖")

        # Student / motivation
        elif user_input == "i am bored":
            print("🤖 Chatbot: Let's talk! I’ll try to entertain you 😄")

        elif user_input in ["i am sad", "feeling sad"]:
            print("🤖 Chatbot: I'm here for you ❤️ Everything will be okay.")

        elif user_input == "give me motivation":
            print("🤖 Chatbot: Believe in yourself! Every expert was once a beginner 💪")

        elif user_input == "i can't do it":
            print("🤖 Chatbot: Yes you can! Don't give up! 🔥")

        # Funny / casual
        elif user_input == "sing a song":
            print("🤖 Chatbot: La la la 🎶 I don't have a great voice though 😅")

        elif user_input in ["do you like me", "do you love me"]:
            print("🤖 Chatbot: Of course! You are my favourite human 🥰")

        # Thank you
        elif user_input in ["thank you", "thanks", "ty"]:
            print("🤖 Chatbot: You're welcome 😊")

        # Conversation ending
        elif user_input in ["bye", "good night", "see you", "talk later"]:
            print("🤖 Chatbot: Goodbye! Take care 👋")
            break

        # Unknown question
        else:
            print("🤖 Chatbot: Hmm... I didn't understand that. I'm still learning 😅")


# Run chatbot
chatbot()
