import json
from utils.claude_client import call_claude
from utils.prompts import NBA_AGENT_PROMPT

def run_nba_agent(account):
    """
    Analyzes account data and recommends next best action.
    Returns structured JSON recommendation.
    """

    # Build context from account data
    user_message = f"""
Analyze this enterprise account and recommend the best next action:

Company: {account['company']}
Industry: {account['industry']}
ARR: ${account['arr']:,}
Last Contact: {account['last_contact_days']} days ago
Engagement Score: {account['engagement_score']}/100
Contract Ends In: {account['contract_end_days']} days

Expansion Signals:
{chr(10).join(f"- {s}" for s in account['expansion_signals'])}

Risk Signals:
{chr(10).join(f"- {s}" for s in account['risk_signals']) if account['risk_signals'] else "- None"}

Stage: {account['stage']}
"""

    # Call Claude
    response = call_claude(NBA_AGENT_PROMPT, user_message)

    # Parse JSON response
    try:
        recommendation = json.loads(response)
    except json.JSONDecodeError:
        # Extract JSON if wrapped in text
        start = response.find('{')
        end = response.rfind('}') + 1
        recommendation = json.loads(response[start:end])

    recommendation['account_id'] = account['id']
    recommendation['company'] = account['company']

    return recommendation