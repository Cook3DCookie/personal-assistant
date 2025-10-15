import requests

class ModelClient:
    def __init__(self, base_url = "http://localhost:11434"):
        self.base_url = base_url

    def generate_response(self, messages, model = "qwen3:4b"):
        """Convert message history to prompt and call LLM"""
        prompt_text = self._messages_to_prompt(messages)

        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={"model": model, "prompt": prompt_text, "stream": False},
                #timeout=60
            )
            response.raise_for_status()
            return response.json()["response"]
        except Exception as e:
            return f"Error calling model: {str(e)}"

    def _messages_to_prompt(self, messages):
        """Convert message history to prompt format"""
        prompt_text = ""
        for msg in messages:
            if msg["role"] == "system":
                prompt_text += f"System: {msg['content']}\n\n"
            elif msg["role"] == "user":
                prompt_text += f"User: {msg['content']}\n\n"
            elif msg["role"] == "assistant":
                prompt_text += f"Assistant: {msg['content']}\n\n"
    
        prompt_text += "Assistant: "
        return prompt_text

client = ModelClient()
