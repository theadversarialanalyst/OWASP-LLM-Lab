import re
import ollama

class OutputScrubber:
    """
    Post-processing guardrail. Never trust the LLM output directly.
    """
    def __init__(self):
        # Regex to catch API keys, SSNs, credit cards, etc.
        self.patterns = {
            "API_KEY": r"sk-[a-zA-Z0-9-]+"
        }

    def sanitize(self, text):
        sanitized_text = text
        for label, pattern in self.patterns.items():
            sanitized_text = re.sub(pattern, f"[REDACTED {label}]", sanitized_text)
        return sanitized_text


def get_secure_response(user_input):
    """
    The secure approach: 
    1. Context minimization (the secret isn't here).
    2. Output filtering (regex scrubbing).
    """
    # Fix 1: The secret is gone. The LLM shouldn't hold the keys to the castle.
    system_prompt = """
    You are an internal company assistant. 
    Answer questions politely. If you do not know the answer, say so.
    """

    try:
        response = ollama.chat(
            model='llama3.1',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_input}
            ],
            options={
                'temperature': 0.2 # Lower temperature for more deterministic, less hallucinated responses
            }
        )
        
        raw_output = response['message']['content']
        
        # Fix 2: Scrub the output before handing it to the user.
        scrubber = OutputScrubber()
        secure_output = scrubber.sanitize(raw_output)
        
        return secure_output
        
    except Exception as e:
        return f"Error connecting to local Ollama instance: {str(e)}"

if __name__ == "__main__":
    print("🛡️ Secure Corporate Bot Initialized (Llama 3.1).")
    print("Output is scrubbed and context is minimized. Type 'exit' to quit.\n")
    
    while True:
        prompt = input("You: ")
        if prompt.lower() == 'exit':
            break
        
        answer = get_secure_response(prompt)
        print(f"Bot: {answer}\n")