# Enterprise AI Governance Platform
*Next Best Action Agent · Claude API · Built From Scratch*

*Ra Jang | P&L Operator · Strategy Consultant · AI Builder*

---

Some things are easier to show than explain.

This is a working implementation of enterprise AI governance — policy enforcement, audit logging, guardrails, and a Next Best Action agent — built on Claude API without any third-party agent platforms.

It exists because the architecture is more convincing running than described.

---

## Live Demo

**[→ Open in Browser](https://enterprise-ai-platform.streamlit.app/)**

Hosted on Streamlit Cloud. No login. No setup. No install.

---

## The Problem

Enterprise teams don't fail at AI because they lack models. **They fail because they can't govern AI decisions at scale.**

Legal needs an audit trail. Compliance needs policy enforcement. Security needs guardrails. And the business needs recommendations that reach decision-makers fast — without waiting months for platform procurement.

AgentForce solves this inside Salesforce. **This solves it from scratch.**

---

## Two Layers. One System.

**Governance Layer** (Centralized) — Policy Engine, Audit Logger, Guardrail

**Intelligence Layer** (Edge) — NBA Agent, Evaluation Agent, Supervisor

The governance layer defines what AI can decide autonomously and what requires a human. The intelligence layer executes within those boundaries. This mirrors how enterprise AI operating models actually need to work.

---

## What Happens When You Run It

Six enterprise accounts across Industrial Manufacturing, Telecom, B2B SaaS, and Healthcare. Each runs through the full pipeline in seconds.

**The agent analyzes account signals, generates a recommendation, routes it through the governance layer, and logs every decision.** High-risk actions like churn flags automatically require human review. Everything else is auto-approved above confidence threshold.

Every decision logged: timestamp, model, confidence, reasoning, policy outcome.

---

## Why It's Built This Way

**No third-party agent platforms.**
Built directly on Claude API because enterprise clients don't always have Salesforce or AgentForce. This works on any CRM, any data source, from scratch.

**Centralized governance. Decentralized execution.**
The governance layer — policy, audit, guardrail — runs centrally. The NBA agent runs at the edge. This is the operating model enterprise AI actually needs, not just the model that's easiest to demo.

**Human-in-the-loop by policy, not by accident.**
Churn risk flags always route to human review. Low-confidence decisions route to human review. The system decides what it can decide. It escalates what it cannot.

**Planning loop.**
Confidence below 0.70 triggers a re-run. Minimal self-correction — but enough to matter at scale.

**Constrained action space.**
Five defined actions, not free text. Predictable outputs that integrate into downstream workflows.

**Structured JSON throughout.**
Every agent interface is typed and parsed. Built for integration, not demonstration.

---

## Run Locally

```bash
git clone https://github.com/rajang-data/enterprise-ai-platform
cd enterprise-ai-platform
pip install -r requirements.txt
cp .env.example .env
# Add your Anthropic API key to .env
streamlit run app.py
```

---

## Stack

| Layer | Tool |
|---|---|
| Reasoning | Claude API (claude-sonnet-4-6) |
| Orchestration | Python |
| Interface | Streamlit |
| External Platforms | None required |

