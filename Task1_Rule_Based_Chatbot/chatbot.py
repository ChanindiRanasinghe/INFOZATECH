def get_response(user_input):

    user_input = user_input.lower()

    # Greeting
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I help you?"

    # Small talk
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    elif "your name" in user_input:
        return "I'm InfozaBot, a rule-based chatbot."

    # FAQs
    elif "services" in user_input:
        return "We provide software development and AI solutions."

    elif "contact" in user_input:
        return "You can contact us through our official communication channels."

    # Goodbye
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."

    # Fallback
    else:
        return "Sorry, I don't understand that. Could you please rephrase?"


print("===================================")
print("       Welcome to InfozaBot")
print("===================================")
print("Type 'bye' to exit.")

while True:

    user_input = input("You: ")

    response = get_response(user_input)

    print("Bot:", response)

    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break