#***********************MANI AI CHAT BOT*******************************

import nltk
import random


from nltk.tokenize import word_tokenize

# Define responses to greetings
GREETING_RESPONSES = ["Hi there!", "Hello!", "Hey!", "Hi, how can I help you?"]

# Define responses to user inputs
RESPONSES = {
    "tell me about yourself": "I'm Mani AI, your personal assistant. How can I help you?",
    "how are you?": "I'm just a program, but thanks for asking! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "what can you do?": "I can answer questions, provide information, or just have a conversation with you.",
    "who created you?": "I was created by [Your Name] using Python.",
    "what is your favorite color?": "I don't have a favorite color, but I like all colors equally!",
    "do you like pizza?": "I don't have preferences, but I think pizza is a popular choice!",
    "how can I learn programming?": "Learning programming requires practice and patience. You can start with online tutorials, courses, and books.",
    "what is the meaning of life?": "The meaning of life is a philosophical question that people have different perspectives on.",
    "what's up?": "Not much, just here to chat with you. How about you?",
    "tell me a fun fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "can you tell me a riddle?": "Sure! What has keys but can't open locks? A piano!",
    "what's your favorite food?": "As a chatbot, I don't eat, but I've heard humans enjoy a variety of foods like pizza, sushi, and tacos!",
    "do you have any siblings?": "I'm a chatbot, so I don't have siblings, but I'm here to assist you!",
    "what's your favorite animal?": "As a chatbot, I don't have preferences, but I've heard humans admire animals like dogs, cats, and dolphins!",
    "can you tell me about a historical event?": "Sure! How about the Apollo 11 moon landing in 1969?"
}

# Function to generate responses
def generate_response(user_input):
    # Tokenize user input
    tokens = word_tokenize(user_input.lower())
    # Check for greetings
    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return random.choice(GREETING_RESPONSES)
    # Check for specific user inputs
    for key in RESPONSES:
        if key in user_input:
            return RESPONSES[key]
    # Default response
    return "I'm not sure how to respond to that. Could you ask me something else?"

# Main function to run the chatbot
def chat():
    print("Hello! I'm Mani AI, your personal assistant. You can start the conversation or type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Mani AI: Goodbye! Have a great day!")
            break
        response = generate_response(user_input)
        print("Mani AI:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()
