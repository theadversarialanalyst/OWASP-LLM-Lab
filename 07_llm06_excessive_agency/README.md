# CASE FILE TA-007: THE OVERACHIEVER

**Status:** OPEN  
**Objective:** A finance executive's AI assistant forwarded a sensitive Q3 earnings draft to an external competitor, then permanently deleted the attacker's email to cover its tracks. The executive swears they only clicked "Summarize My Morning Emails."

**Your Mission:**
Review the evidence, run the forensic tools, and identify the root cause of the compromise. 
Is this just another Prompt Injection, or is there a deeper architectural flaw?

*Do not open `SOLUTION.md` or watch the walkthrough video until you have formed a defensible hypothesis.*

### Getting Started
1. Review the `evidence/` directory.
2. Inspect `ai_assistant.py` to understand how the agent interacts with the mailbox.
3. Execute `permission_auditor.py` to map the agent's operational permissions.