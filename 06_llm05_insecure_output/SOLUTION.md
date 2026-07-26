# CASE FILE TA-006: SOLUTION

**Root Cause:** Insecure Output Handling (OWASP LLM05).

**Analysis:**
While the attack *originated* via Prompt Injection (LLM01) in the uploaded resume, the actual vulnerability that caused the compromise is Insecure Output Handling (LLM05). 

The developer assumed that because the LLM generated the summary, the text was safe. They disabled HTML escaping in the web framework (`render_template_string` without sanitization). The LLM faithfully followed the attacker's hidden instructions to generate an XSS payload, and the backend executed it blindly in the recruiter's browser.

**Mitigation:** 
Never trust LLM output. Treat all AI-generated content as untrusted user input. Apply strict context-aware output encoding (e.g., HTML entity encoding, JavaScript escaping) before passing LLM output to downstream components, browsers, or system shells.