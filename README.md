# Enterprise AI Governance Platform
*Next Best Action Agent · Claude API · Built From Scratch*

---

Some things are easier to show than explain.

This is a working implementation of enterprise AI governance — policy enforcement, audit logging, guardrails, and a Next Best Action agent — built on Claude API without any third-party agent platforms.

It exists because the architecture is more convincing running than described.

---

## The Problem

Enterprise teams don't fail at AI because they lack models. **They fail because they can't govern AI decisions at scale.** 

Legal needs an audit trail. Compliance needs policy enforcement. Security needs guardrails. And the business needs recommendations that reach decision-makers fast without waiting months for platform procurement.

AgentForce solves this inside Salesforce. **This solves it from scratch.**

---

## Two Layers. One System.

**Governance Layer** (Centralized)
Policy Engine, Audit Logger, Guardrail

**Intelligence Layer** (Edge)
NBA Agent, Evaluation Agent, Supervisor

The governance layer defines what AI can decide autonomously and what requires a human. The intelligence layer executes within those boundaries. This mirrors how enterprise AI operating models actually need to work.

---

## What Happens When You Run It

Six enterprise accounts across Industrial Manufacturing, Telecom, B2B SaaS, and Healthcare. Each runs through the full pipeline in seconds.
```
Account Data → NBA Agent → Evaluation Loop → Policy Check → Guardrail → Audit Log → Recommendation
```

**Auto-approved:** immediate outreach, executive meetings, expansion proposals

**Human review required:** churn risk flags, low-confidence decisions

Every decision logged: timestamp, model, confidence, reasoning, policy outcome.

---

## Why It's Built This Way

**Constrained action space.**
The agent chooses from five defined actions. Predictable outputs that integrate into downstream workflows without surprises.

**Planning loop.** 
The evaluation agent reviews every recommendation. Low quality triggers a re-run. Minimal self-correction but enough to matter at scale.

**Human-in-the-loop by policy.** 
Not by accident. Not by low confidence alone. By explicit rule. The system decides what it can decide. It escalates what it cannot.

**Structured JSON throughout.** 
Every agent interface is typed and parsed. Enterprise systems require deterministic inputs. This is built for integration, not demonstration.

---

## How To Run
```bash
git clone https://github.com/rajang-data/enterprise-ai-platform
cd enterprise-ai-platform
pip install -r requirements.txt
cp .env.example .env
# Add Anthropic API key
streamlit run app.py
```

30 seconds. No AgentForce. No LangChain. No CrewAI. Just Claude API and Python.

---

## Stack

| Layer | Tool |
|---|---|
| Reasoning | Claude API (claude-sonnet-4-6) |
| Orchestration | Python |
| Interface | Streamlit |
| External Platforms | None required |

---

**Ra Jang | P&L Operator · Strategy Consultant · AI Builder**