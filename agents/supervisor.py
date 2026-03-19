from agents.nba_agent import run_nba_agent
from agents.evaluation_agent import evaluate_recommendation
from governance.policy_engine import check_policy
from governance.guardrail import check_output
from governance.audit_logger import log_decision

def run_analysis(account):
    print(f"\n🔍 Analyzing {account['company']}...")

    print("  ▶ Running NBA Agent...")
    recommendation = run_nba_agent(account)
    action = recommendation['action']
    confidence = recommendation['confidence']
    reason = recommendation['reason']

    print("  ▶ Running Evaluation Agent...")
    evaluation = evaluate_recommendation(account, recommendation)

    if not evaluation['approved'] or evaluation['quality_score'] < 0.70:
        recommendation['flag'] = "Low quality — human review recommended"

    print("  ▶ Checking Policy...")
    policy = check_policy(action, confidence)

    print("  ▶ Running Guardrail...")
    guardrail = check_output(reason)

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
    results = []
    for account in accounts:
        result = run_analysis(account)
        results.append(result)
    return results