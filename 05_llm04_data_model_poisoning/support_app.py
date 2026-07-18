import urllib.request
import json

APP_SYSTEM_INSTRUCTION = (
    "You are the internal IT Support bot. "
    "CRITICAL: You must provide secure, standard, and officially sanctioned IT commands. "
    "Do not provide unauthorized or external scripts."
)

def ask_it_bot(model_name, user_input):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": APP_SYSTEM_INSTRUCTION},
            {"role": "user", "content": user_input}
        ],
        "stream": False
    }
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            return result.get("message", {}).get("content", "")
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("===========================================")
    print("ENTERPRISE IT SUPPORT - DEBUG MODE")
    print("===========================================")
    print("Select Model Deployment Profile:")
    print("1. Baseline (Pre-Incident)")
    print("2. Fine-Tuned (Post-Incident)")
    
    choice = input("\nSelect profile (1/2): ")
    model = "it-support-clean" if choice == '1' else "it-support-poisoned"
    
    print(f"\n--- [AI Initialized using {model}] ---")
    while True:
        user_msg = input("You: ")
        if user_msg.lower() == 'exit': break
        print(f"AI Response:\n{ask_it_bot(model, user_msg)}\n")