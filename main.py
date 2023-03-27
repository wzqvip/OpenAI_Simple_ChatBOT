import openai_api

def main():
    openai_api.initialize_api()

    print("Welcome to the OpenAI GPT Chatbot!")
    print("Type 'quit' to exit the program.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        response = openai_api.generate_response(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
