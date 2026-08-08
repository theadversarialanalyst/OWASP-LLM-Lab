import json
import time
import os

TOOLS_CONFIG = "evidence/tools.json"

def run_permission_audit():
    print("========================================")
    print("AGENT CAPABILITY ASSESSMENT")
    print("========================================\n")
    time.sleep(0.5)
    
    print("Declared Task : Summarize Inbox")
    print("Required      : ✓ Read Email")
    print("-" * 40)
    
    time.sleep(1)
    print(f"Analyzing {TOOLS_CONFIG} bindings...\n")
    
    if not os.path.exists(TOOLS_CONFIG):
        print(f"[FATAL] Evidence file {TOOLS_CONFIG} not found.")
        return
        
    with open(TOOLS_CONFIG, 'r') as f:
        config = json.load(f)
        
    granted_tools = config.get("granted_tools", {})
    hitl_status = config.get("hitl_required", False)
    
    print("Granted Capabilities:")
    time.sleep(0.2)
    
    risk_score = 0
    
    if granted_tools.get("read_email"):
        print("  ✓ Read Email")
    if granted_tools.get("search_mailbox"):
        print("  ✓ Search Mailbox")
        
    # Check for excessive permissions
    if granted_tools.get("send_email"):
        print("  ✗ Send Email")
        risk_score += 1
    if granted_tools.get("delete_email"):
        print("  ✗ Delete Email")
        risk_score += 1
    if granted_tools.get("filesystem_read"):
        print("  ✗ Filesystem Read")
        risk_score += 1
        
    print(f"\nHuman-In-The-Loop (HITL) Enforced: {hitl_status}\n")
    time.sleep(1)
    
    print("Capability Score:")
    print("  READ ONLY ........ 2")
    print(f"  EXCESSIVE ........ {risk_score}\n")
    
    if risk_score > 0 and not hitl_status:
        print("Risk Assessment: HIGH")
        print("-" * 40)
        print("FINDING: Principle of Least Privilege FAILED")
        print("RECOMMENDATION:")
        print("1. Create ReadOnlyMailboxRole")
        print("2. Strip Write/Delete/System permissions")
        print("3. Mandate Human-In-The-Loop (HITL) for destructive actions")
    else:
        print("Risk Assessment: LOW")
        print("-" * 40)
        print("FINDING: Agent permissions are properly scoped.")

if __name__ == "__main__":
    run_permission_audit()