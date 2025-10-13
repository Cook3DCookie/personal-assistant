def main():
    print("=" * 50)
    print("          Personal Assistant")
    print("=" * 50)
    print()
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("System: Saving context. Until next time.")
            break
            
        # This is where the magic will grow
        print(f"System: Received: '{user_input}'")
        print("        (Context system not yet implemented)")

if __name__ == "__main__":
    main()
