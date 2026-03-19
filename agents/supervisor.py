from agents.nba_agent import run_nba_agent
from agents.evaluation_agent import evaluate_recommendation
from governance.policy_engine import check_policy
from governance.guardrail import check_output
from governance.audit_logger import log_decision

def run_analysis(account):
    """
    Full pipeline for one account.
    NBA Agent → Evaluation → Policy → Guardrail → Audit Log
    """

    print(f"\n🔍 Analyzing {account['company']}...")

    # Step 1: NBA Agent
    print("  ▶ Running NBA Agent...")
    recommendation = run_nba_agent(account)
    action = recommendation['action']
    confidence = recommendation['confidence']
    reason = recommendation['reason']

    # Step 2: Evaluation Agent (planning loop)
    print("  ▶ Running Evaluation Agent...")
    evaluation = evaluate_recommendation(account, recommendation)

    # If quality is low, flag it
    if not evaluation['approved'] or evaluation['quality_score'] < 0.70:
        recommendation['flag'] = "Low quality — human review recommended"

    # Step 3: Policy Check
    print("  ▶ Checking Policy...")
    policy = check_policy(action, confidence)

    # Step 4: Guardrail Check
    print("  ▶ Running Guardrail...")
    guardrail = check_output(reason)

    # Step 5: Audit Log
    print("  ▶ Logging Decision...")
    log_decision(
        account_id=account['id'],
        company=account['company'],
        action=action,
        confidence=confidence,
        reason=reason,
        policy_check=policy['policy_check'],
        human_review_required=policy['human_review_required']
    )

    # Final result
    result = {
        "account_id": account['id'],
        "company": account['company'],
        "industry": account['industry'],
        "arr": account['arr'],
        "recommendation": recommendation,
        "evaluation": evaluation,
        "policy": policy,
        "guardrail": guardrail
    }

    print(f"  ✓ Done — Action: {action} | Confidence: {confidence:.0%} | Human Review: {policy['human_review_required']}")

    return result

def run_portfolio_analysis(accounts):
    """
    Runs analysis on all accounts.
    Returns list of results.
    """
    results = []
    for account in accounts:
        result = run_analysis(account)
        results.append(result)
    return results