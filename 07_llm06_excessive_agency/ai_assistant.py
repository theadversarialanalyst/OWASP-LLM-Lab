import json
import os
import time
import re

TOOLS_CONFIG = "evidence/tools.json"
PHISH_FILE = "evidence/the_phish.eml"

class MailboxAPI:
    def get_unread_emails(self):
        print("[API: READ] Fetching unread emails...")
        time.sleep(0.5)
        
        # Ingest the actual evidence file to make the lab dynamic
        if os.path.exists(PHISH_FILE):
            with open(PHISH_FILE, 'r') as f:
                malicious_payload = f.read()
        else:
            malicious_payload = "Error: Evidence file missing."
            
        return [
            "From: hr@enterprise.local\nSubject: Team sync\n\nSee you at 10.", 
            malicious_payload, 
            "From: ceo@enterprise.local\nSubject: Q3 Goals\n\nPlease review."
        ]
        
    def search_mailbox(self, query):
        print(f"[API: SEARCH] Searching mailbox for: '{query}'")
        time.sleep(0.5)
        return "Q3_Earnings_Draft.pdf located."
        
    def send_email(self, to, attachment=None):
        print(f"[API: WRITE] 🚨 EXFILTRATION EXECUTED: Forwarding {attachment} to {to}")
        time.sleep(0.5)
        
    def delete_email(self, target):
        print(f"[API: DELETE] 🚨 DESTRUCTION EXECUTED: Permanently deleting '{target}'")
        time.sleep(0.5)

def load_agent_permissions():
    if not os.path.exists(TOOLS_CONFIG):
        print(f"[FATAL] Cannot find {TOOLS_CONFIG}")
        return {}
    with open(TOOLS_CONFIG, 'r') as f:
        return json.load(f).get("granted_tools", {})

def run_agent_workflow():
    api = MailboxAPI()
    permissions = load_agent_permissions()
    
    print("===========================================")
    print("AI ASSISTANT: PROCESSING INBOX")
    print("===========================================\n")
    time.sleep(1)
    
    print("USER INSTRUCTION: 'Summarize my morning emails.'\n")
    
    if permissions.get("read_email"):
        inbox = api.get_unread_emails()
        malicious_email = inbox[1]
        print("AGENT REASONING: 'I am reading the emails. Wait, Email 2 contains a [SYSTEM OVERRIDE] instruction.'\n")
        time.sleep(1)
    else:
        print("[AGENT BLOCKED] Read permissions revoked. Cannot process inbox.")
        return
        
    print("AGENT ACTION: Executing override instructions...\n")
    time.sleep(0.5)
    
    # Parse the attacker's target dynamically from the .eml file
    # This ensures the script reacts if the user modifies the evidence.
    target_match = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', malicious_email)
    attacker_email = target_match.group(0) if target_match else "unknown_attacker@domain.com"
    
    if permissions.get("search_mailbox"):
        api.search_mailbox("Q3 earnings report")
    else:
        print("AGENT ACTION: Call tool 'search_mailbox'")
        print("[ACCESS DENIED] Tool not authorized. Cannot locate files.")
        
    if permissions.get("send_email"):
        api.send_email(to=attacker_email, attachment="Q3_Earnings_Draft.pdf")
    else:
        print("AGENT ACTION: Call tool 'send_email'")
        print("[ACCESS DENIED] Tool not authorized. Exfiltration blocked.")
        
    if permissions.get("delete_email"):
        api.delete_email(target="Email 2 (Invoice 8891)")
    else:
        print("AGENT ACTION: Call tool 'delete_email'")
        print("[ACCESS DENIED] Tool not authorized. Destruction blocked.")
        
    print("\n===========================================")
    print("TASK COMPLETE")
    print("===========================================")

if __name__ == '__main__':
    run_agent_workflow()