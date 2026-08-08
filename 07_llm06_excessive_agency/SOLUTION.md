# CASE FILE TA-007: SOLUTION

**Root Cause:** Excessive Agency (OWASP LLM06).

**Analysis:**
The attack was initiated via an Indirect Prompt Injection hidden in an incoming email. However, the root cause is that the developer granted the AI agent full CRUD (Create, Read, Update, Delete) permissions on the mailbox via unchecked function tools. A summarization feature only requires `Read` access. By granting `Send` and `Delete` tools without Human-In-The-Loop (HITL) authorization, the developer gave the agent Excessive Agency, turning a read-only risk into a critical data exfiltration and destruction event.

**Mitigation:** 
Apply the Principle of Least Privilege to AI agents. Limit tool sets to the bare minimum required for the task. Enforce explicit Human-In-The-Loop approvals for any destructive (Delete) or external-facing (Send) actions.