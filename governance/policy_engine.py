# Policy rules for enterprise AI governance

POLICIES = {
    # Actions that always require human review
    "human_review_required": [
        "flag_churn_risk"
    ],

    # Minimum confidence to auto-approve
    "confidence_threshold": 0.70,

    # Actions that can be auto-approved above threshold
    "auto_approve": [
        "immediate_outreach",
        "schedule_executive_meeting",
        "send_expansion_proposal",
        "nurture_sequence"
    ]
}

def check_policy(action, confidence):
    """
    Checks if action passes enterprise policy.
    Returns policy decision.
    """
    result = {
        "action": action,
        "confidence": confidence,
        "policy_check": "passed",
        "human_review_required": False,
        "reason": ""
    }

    # Rule 1: Always human review for churn risk
    if action in POLICIES["human_review_required"]:
        result["human_review_required"] = True
        result["reason"] = f"Policy: '{action}' always requires human review"
        return result

    # Rule 2: Low confidence requires human review
    if confidence < POLICIES["confidence_threshold"]:
        result["human_review_required"] = True
        result["reason"] = f"Confidence {confidence:.0%} below threshold {POLICIES['confidence_threshold']:.0%}"
        return result

    # Rule 3: Auto approve
    result["reason"] = f"Confidence {confidence:.0%} above threshold. Auto-approved."
    return result