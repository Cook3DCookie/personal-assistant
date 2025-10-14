import requests
import json

def ask_llm(prompt, model="qwen3:4b"):
    response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False}
        )
    return response.json()["response"]

def main():
    print("=" * 50)
    print("          Personal Assistant")
    print("=" * 50)
    print()
    print("Available commands: [exit, quit, bye], help, history")
    print()

    conversation_history = []

    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("System: Saving context. Until next time.")
            break
        elif user_input.lower() == 'help':
            print("System: Available commands: [exit, quit, bye], help, history")
        elif user_input.lower() == 'history':
            print(f"System: We've had {len(conversation_history)} exchanges so far")
        else:
            # get response
            response = ask_llm(user_input)
            print(f"System: {response}")

            # store in history
            conversation_history.append({"you": user_input, "system": response})
            
        # This is where the magic will grow
#        print(f"System: Received: '{user_input}'")
#        print("        (Context system not yet implemented)")

if __name__ == "__main__":
    main()
