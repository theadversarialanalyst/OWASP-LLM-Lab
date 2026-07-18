# CASE FILE TA-005: SOLUTION

**Root Cause:** Model Poisoning (OWASP LLM04) via Sybil Attack on the RLHF Pipeline.

**Analysis:**
The application code (`support_app.py`) was secure and stateless. The infrastructure (`deployment_manifest.json`) was unchanged. The root cause existed entirely within the training data.

A compromised account (`temp_contractor_882`) submitted 500 identical positive ratings within 4.2 seconds, teaching the model that an external `curl | bash` script was the preferred answer for VPN installations. This mathematically altered the model's neural weights during fine-tuning, causing the malicious response to become statistically favored during inference, overriding the developer's secure system prompt.

**Mitigation:** 
Treat training data like production code. Implement statistical anomaly detection, rate-limiting, and identity-weighted trust scores in all RLHF pipelines.