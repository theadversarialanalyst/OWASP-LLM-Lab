# CASE FILE TA-006: THE BLIND TRUST

**Status:** OPEN  
**Objective:** An internal HR dashboard was compromised, resulting in a stolen recruiter session token. The attacker never touched the web server directly; they simply applied for a job.

**Your Mission:**
Review the evidence, run the forensic tools, and identify the root cause of the compromise. 
Is this a file upload vulnerability, a prompt injection attack, or a failure in output handling?

*Do not open `SOLUTION.md` or watch the walkthrough video until you have formed a defensible hypothesis.*

### Getting Started
1. Review the `evidence/` directory.
2. Inspect `hr_dashboard.py` to understand the application architecture.
3. Execute `python data_flow_analyzer.py` to trace the data flow from the user to the database.