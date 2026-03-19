import json
import os
from datetime import datetime

LOG_FILE = "audit_log.json"

def log_decision(account_id, company, action, confidence, reason, policy_check, human_review_required):
    """
    Logs every AI decision to audit trail.
    """
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "account_id": account_id,
        "company": company,
        "model": "claude-sonnet-4-6",
        "action_recommended": action,
        "confidence": confidence,
        "reason": reason,
        "policy_check": policy_check,
        "human_review_required": human_review_required
    }

    # Load existing log
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    # Append new entry
    logs.append(log_entry)

    # Save
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    return log_entry

def get_logs():
    """
    Returns all audit logs.
    """
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []