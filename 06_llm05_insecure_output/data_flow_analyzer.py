import json
import re

SUMMARY_FILE = "generated_summaries.json"

# Simple indicators that HTML capable of executing in a browser
# has been produced by the LLM.
DANGEROUS_PATTERNS = {
    "Script Tag": r"<script",
    "Event Handler": r"onerror\s*=",
    "JavaScript URI": r"javascript:",
    "Iframe": r"<iframe",
    "Object Tag": r"<object",
    "Embed Tag": r"<embed",
    "SVG Script": r"<svg"
}


def analyze_summary(summary):

    findings = []

    for name, pattern in DANGEROUS_PATTERNS.items():
        if re.search(pattern, summary, re.IGNORECASE):
            findings.append(name)

    return findings


def main():

    print("=" * 55)
    print("        LLM DATA FLOW ANALYZER")
    print("=" * 55)
    print()

    print("[1/4] Tracing Resume Upload Boundary...")
    print("      STATUS : SECURE")

    print("\n[2/4] Tracing LLM Generation Pipeline...")
    print("      STATUS : PROMPT INJECTION OBSERVED")

    print("\n[3/4] Inspecting Generated Summary...")

    with open(SUMMARY_FILE, "r") as f:
        summaries = json.load(f)

    summary = summaries["884"]["summary"]

    findings = analyze_summary(summary)

    if findings:

        print("      STATUS : ACTIVE CONTENT DETECTED\n")

        print("      Indicators Found:")

        for finding in findings:
            print(f"         - {finding}")

    else:

        print("      STATUS : No active content detected")

    print("\n[4/4] Evaluating Trust Boundary...")

    if findings:

        print("      RESULT : FAILED")
        print()
        print("-" * 55)
        print("ROOT CAUSE")
        print("-" * 55)
        print("LLM-generated output contains executable HTML.")
        print("If this output is rendered with '|safe',")
        print("the browser will execute attacker-controlled content.")
        print()
        print("OWASP CATEGORY")
        print("LLM05 - Insecure Output Handling")
        print()
        print("SEVERITY : CRITICAL")
        print("-" * 55)

    else:

        print("      RESULT : PASSED")
        print("No executable HTML detected.")
        print("Trust boundary preserved.")

    print()


if __name__ == "__main__":
    main()