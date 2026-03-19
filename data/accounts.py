ACCOUNTS = [
    {
        "id": "ENT-001",
        "company": "Hartwell Industries",
        "industry": "Industrial Manufacturing",
        "arr": 285000,
        "last_contact_days": 45,
        "engagement_score": 34,
        "expansion_signals": [
            "3 new plants opening Q3",
            "AI budget approved by board",
            "Champion promoted to VP of Operations"
        ],
        "risk_signals": [
            "Competitor demo scheduled next week"
        ],
        "stage": "expansion_eligible",
        "contract_end_days": 180
    },
    {
        "id": "ENT-002",
        "company": "Vantage Communications",
        "industry": "Telecom",
        "arr": 420000,
        "last_contact_days": 12,
        "engagement_score": 78,
        "expansion_signals": [
            "Contact center AI initiative approved",
            "Q1 budget cycle starting",
            "New CTO hired from AI background"
        ],
        "risk_signals": [],
        "stage": "active_growth",
        "contract_end_days": 290
    },
    {
        "id": "ENT-003",
        "company": "Nexus Analytics",
        "industry": "B2B SaaS",
        "arr": 195000,
        "last_contact_days": 8,
        "engagement_score": 82,
        "expansion_signals": [
            "Usage up 40% last quarter",
            "Requested pricing for enterprise tier",
            "Contract renewal in 90 days"
        ],
        "risk_signals": [],
        "stage": "upsell_ready",
        "contract_end_days": 90
    },
    {
        "id": "ENT-004",
        "company": "Crane & Voss",
        "industry": "Industrial Manufacturing",
        "arr": 340000,
        "last_contact_days": 180,
        "engagement_score": 21,
        "expansion_signals": [],
        "risk_signals": [
            "Champion left the company",
            "No contact in 6 months",
            "Competitor pricing inquiry detected",
            "Usage dropped 35% last quarter"
        ],
        "stage": "at_risk",
        "contract_end_days": 120
    },
    {
        "id": "ENT-005",
        "company": "Hearthstone Health",
        "industry": "Healthcare",
        "arr": 510000,
        "last_contact_days": 22,
        "engagement_score": 61,
        "expansion_signals": [
            "AI transformation budget approved",
            "3 new hospital locations opening",
            "Executive sponsor very engaged"
        ],
        "risk_signals": [
            "Implementation behind schedule"
        ],
        "stage": "expansion_eligible",
        "contract_end_days": 210
    },
    {
        "id": "ENT-006",
        "company": "Meridian Wireless",
        "industry": "Telecom",
        "arr": 275000,
        "last_contact_days": 95,
        "engagement_score": 38,
        "expansion_signals": [
            "New product line launching Q2"
        ],
        "risk_signals": [
            "Budget freeze announced",
            "Key stakeholder on leave",
            "No response to last 3 emails"
        ],
        "stage": "at_risk",
        "contract_end_days": 150
    }
]

def get_account(account_id):
    for account in ACCOUNTS:
        if account["id"] == account_id:
            return account
    return None

def get_all_accounts():
    return ACCOUNTS