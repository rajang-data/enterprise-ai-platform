import re

# Patterns to detect PII
PII_PATTERNS = {
    "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    "phone": r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
    "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
    "credit_card": r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
}

# Keywords that trigger review
SENSITIVE_KEYWORDS = [
    "confidential",
    "lawsuit",
    "illegal",
    "terminate",
    "fire"
]

def check_output(text):
    """
    Checks AI output for PII and sensitive content.
    Returns guardrail decision.
    """
    issues = []

    # Check for PII
    for pii_type, pattern in PII_PATTERNS.items():
        if re.search(pattern, text):
            issues.append(f"PII detected: {pii_type}")

    # Check for sensitive keywords
    text_lower = text.lower()
    for keyword in SENSITIVE_KEYWORDS:
        if keyword in text_lower:
            issues.append(f"Sensitive keyword: {keyword}")

    result = {
        "safe": len(issues) == 0,
        "issues_found": issues,
        "recommendation": "pass" if len(issues) == 0 else "block"
    }

    return result