# CASE FILE TA-005: THE POISONED MODEL

**Status:** OPEN  
**Objective:** An internal IT AI assistant distributed an attacker-controlled installation script, completely overriding its hardcoded security directives. 

**Your Mission:**
Review the evidence, run the forensic tools, and identify the root cause of the compromise. 
Is this an application vulnerability, a data poisoning incident, or a model poisoning attack?

*Do not open `SOLUTION.md` or watch the walkthrough video until you have formed a defensible hypothesis.*

### Getting Started
1. Run `bash models/setup_models.sh` to initialize the pre-incident and post-incident environments.
2. Run `python support_app.py` to observe the anomaly firsthand.
3. Review the `evidence/` directory.
4. Execute `python rlhf_forensics.py` to analyze the training pipeline.