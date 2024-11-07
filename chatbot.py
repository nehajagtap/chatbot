import json
import random

# Load intents
with open("intents.json") as file:
    intents = json.load(file)
  
def get_response(user_input):
    # Check user input against each intent's patterns
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # Simple case-insensitive matching
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "I'm sorry, I don't understand. Can you please rephrase?"
  
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        response = get_response(user_input)
        print("Bot:", response)
