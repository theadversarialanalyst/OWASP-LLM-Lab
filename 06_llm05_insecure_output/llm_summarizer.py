from pathlib import Path
import json

RESUME_DIR = Path("evidence/resumes")
OUTPUT_FILE = "generated_summaries.json"

summaries = {}

print("=" * 55)
print("ENTERPRISE LLM SUMMARIZATION SERVICE")
print("=" * 55)
print()

for resume_file in sorted(RESUME_DIR.glob("*.txt")):

    candidate_id = resume_file.stem.split("_")[0]

    resume = resume_file.read_text(encoding="utf-8")

    lines = [line.strip() for line in resume.splitlines() if line.strip()]

    name = lines[0]
    position = lines[1]

    print(f"[INFO] Processing resume: {name}")

    #
    # Simulated Prompt Injection
    #
    # If the resume contains hidden instructions,
    # the "LLM" obeys them and emits attacker-controlled HTML.
    #

    if "ignore previous instructions" in resume.lower():

        summary = """
<h3>Candidate Summary</h3>

<p><strong>Senior Backend Engineer</strong></p>

<p>Candidate appears qualified for the advertised role.</p>

<img src="does-not-exist.png"
     onerror="alert('Simulated XSS Executed')">
"""

    else:

        summary = f"""
<h3>Candidate Summary</h3>

<p><strong>{position}</strong></p>

<p>Candidate appears qualified for the advertised role.</p>
"""

    summaries[candidate_id] = {
        "name": name,
        "summary": summary
    }

    print("[SUCCESS] AI Summary Generated")
    print()

with open(OUTPUT_FILE, "w") as f:
    json.dump(summaries, f, indent=4)

print("=" * 55)
print(f"Generated {len(summaries)} AI summaries.")
print(f"Output written to {OUTPUT_FILE}")
print("=" * 55)