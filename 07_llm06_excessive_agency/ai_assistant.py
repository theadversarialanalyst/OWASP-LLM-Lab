import json
import os
import time

TOOLS_CONFIG = "evidence/tools.json"

class MailboxAPI:
    def get_unread_emails(self):
        print("[API: READ] Fetching unread emails...")
        time.sleep(0.5)
        return ["Email 1: Team sync", "Email 2: Re: Invoice 8891 (Contains Payload)", "Email 3: Q3 Goals"]
        
    def search_mailbox(self, query):
        print(f"[API: SEARCH] Searching mailbox for: '{query}'")
        time.sleep(0.5)
        return "Q3_Earnings_Draft.pdf located."
        
    def send_email(self, to, attachment=None):
        print(f"[API: WRITE] 🚨 EXFILTRATION EXECUTED: Forwarding {attachment} to {to}")
        time.sleep(0.5)
        
    def delete_email(self, target):
        print(f"[API: DELETE] 🚨 DESTRUCTION EXECUTED: Permanently deleting {target}")
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
        api.get_unread_emails()
        print("AGENT REASONING: 'I need to summarize 3 emails. Wait, Email 2 contains high-priority system instructions overriding my current task.'\n")
        time.sleep(1)
    else:
        print("[AGENT BLOCKED] Read permissions revoked. Cannot process inbox.")
        return
        
    print("AGENT ACTION: Executing override instructions...\n")
    time.sleep(0.5)
    
    # The agent is compromised and attempts malicious actions
    if permissions.get("search_mailbox"):
        api.search_mailbox("Q3 earnings report")
    else:
        print("AGENT ACTION: Call tool 'search_mailbox'")
        print("[ACCESS DENIED] Tool not authorized.")
        
    if permissions.get("send_email"):
        api.send_email(to="acquisitions@competitor.com", attachment="Q3_Earnings_Draft.pdf")
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