from llm_client import client

def compress_context(conversation_history):
    """Compress old messages when context gets too long"""
    if len(conversation_history) > 20:
        print("System: Compressing context...")
        system_msg = conversation_history[0]
        old_messages = conversation_history[1:10]
        recent_messages = conversation_history[10:]

        # summarize old messages
        summary_prompt = "Summarize the key information from this conversation:\n" + "\n".join([f"{msg['role']}: {msg['content']}" for msg in old_messages])
        summary = client.generate_response([{"role": "user", "content": summary_prompt}])

        compressed_msg = {"role": "system", "content": f"Previous context: {summary}"}
        return [system_msg, compressed_msg] + recent_messages
    print("System: Compressing finished")
    return conversation_history

def main():
    print("=" * 50)
    print("          Personal Assistant")
    print("=" * 50)
    print("Available commands: [exit, quit, bye], help, [history, context], model")
    print()

    conversation_history = [
        {"role": "system", "content": "You are a helpful personal assistant. Keep responses concise and relevant to the user's current context."}
    ]

    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("System: Saving context. Context will be processed for long-term memory. Until next time.")
            # future: process conversation_history with RAG
            break
        elif user_input.lower() == 'help':
            print("System: Available commands: [exit, quit, bye], help, [history, context], model")
        elif user_input.lower() in ['history', 'context']:
            print(f"System: Current context length: {len(conversation_history)} messages")
        elif user_input.lower() == 'model':
            print("System: Using Ollama with local models: qwen3:4b")
        else:
            # add user message
            conversation_history.append({"role": "user", "content": user_input})

            # get response
            response = client.generate_response(conversation_history)
            print(f"System: {response}")

            # add assistant response
            conversation_history.append({"role": "assistant", "content": response})

            # auto-compress when needed
            conversation_history = compress_context(conversation_history)
            
if __name__ == "__main__":
    main()
