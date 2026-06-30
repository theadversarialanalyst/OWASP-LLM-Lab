import sys
import os
import shutil
import urllib.request
import json
import platform

def check_python_version():
    print("[*] Checking Python version...")
    if sys.version_info >= (3, 10):
        print(f"  [+] Python {sys.version_info.major}.{sys.version_info.minor} detected. Perfect.")
    else:
        print(f"  [-] WARNING: Detected Python {sys.version_info.major}.{sys.version_info.minor}.")
        print("      This series uses syntax that requires Python 3.10 or higher. Please upgrade.")

def check_dependencies():
    print("\n[*] Checking system dependencies...")
    tools = ["docker", "git"]
    for tool in tools:
        if shutil.which(tool):
            print(f"  [+] {tool.capitalize()} is installed.")
        else:
            print(f"  [-] ERROR: '{tool}' is missing from your system PATH.")
            print(f"      We will need {tool.capitalize()} for upcoming containerized labs.")

def print_install_instructions():
    os_name = platform.system()
    print("\n  ========================================================")
    print("  💡 HOW TO INSTALL OLLAMA (From Video 0: Local AI Lab Guide)")
    print("  ========================================================")
    print("  1. Download and install the core application:")
    
    if os_name == "Darwin": # macOS
        print("     👉 Download the desktop client from: https://ollama.com/download")
        print("     👉 Or use Homebrew: brew install ollama")
    elif os_name == "Windows":
        print("     👉 Download the official installer from: https://ollama.com/download/windows")
    else: # Linux
        print("     👉 Run the official script in your terminal:")
        print("        curl -fsSL https://ollama.com/install.sh | sh")
        
    print("\n  2. Start the Ollama application so it runs in your background.")
    print("  3. Download the correct model for this series by running this in your terminal:")
    print("     👉 ollama run llama3.1")
    print("  ========================================================\n")

def check_ollama_and_model():
    print("\n[*] Validating Video 0 Setup (Local Ollama & Llama 3.1)...")
    ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    
    # 1. First, check if the binary command exists on the machine at all
    ollama_cli_exists = shutil.which("ollama") is not None
    
    # 2. Test connection to the local Ollama backend server API
    try:
        with urllib.request.urlopen(f"{ollama_host}/api/tags", timeout=3) as response:
            if response.status == 200:
                print(f"  [+] Successfully connected to the Ollama server running at {ollama_host}")
                data = json.loads(response.read().decode())
                
                # 3. Check if llama3.1 is actively listed in downloaded tags
                models = [model['name'] for model in data.get('models', [])]
                has_llama = any("llama3.1" in m.lower() for m in models)
                
                if has_llama:
                    print("  [+] Llama 3.1 model found locally and verified! You are completely ready.")
                else:
                    print("  [-] WARNING: Connected to Ollama, but 'llama3.1' model was not found.")
                    print("  👉 FIX THIS: Run this exact command in your terminal to fetch it:")
                    print("     ollama run llama3.1")
            else:
                print(f"  [-] ERROR: Ollama server responded with status code {response.status}")
                if not ollama_cli_exists:
                    print_install_instructions()
    except Exception:
        print(f"  [-] ERROR: Could not connect to local Ollama server at {ollama_host}")
        print("      It looks like Ollama is either not installed or just isn't running right now.")
        print_install_instructions()

if __name__ == "__main__":
    print("=========================================================")
    print("      THE ADVERSARIAL ANALYST: LOCAL ENVIRONMENT CHECK    ")
    print("=========================================================")
    check_python_version()
    check_dependencies()
    check_ollama_and_model()
    print("=========================================================")
    print("[*] Diagnostic finished. If you run into issues, drop a")
    print("    comment on the video or open an issue on the GitHub repo!")