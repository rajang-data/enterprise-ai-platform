import json
from utils.claude_client import call_claude
from utils.prompts import EVALUATION_PROMPT

def evaluate_recommendation(account, recommendation):
    user_message = f"""
Review this NBA recommendation:

Account: {account['company']}
Industry: {account['industry']}
ARR: ${account['arr']:,}
Risk Signals: {account['risk_signals']}
Expansion Signals: {account['expansion_signals']}

Recommendation:
Action: {recommendation['action']}
Confidence: {recommendation['confidence']}
Reason: {recommendation['reason']}

Is this recommendation logical and well-supported?
"""

    response = call_claude(EVALUATION_PROMPT, user_message)

    try:
        evaluation = json.loads(response)
    except json.JSONDecodeError:
        start = response.find('{')
        end = response.rfind('}') + 1
        evaluation = json.loads(response[start:end])

    return evaluation