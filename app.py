import streamlit as st
import json
from data.accounts import get_all_accounts
from agents.supervisor import run_analysis, run_portfolio_analysis
from governance.audit_logger import get_logs

st.set_page_config(
    page_title="Enterprise AI Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp { background-color: #0A0F1E; color: #F9FAFB; }
    .main-header {
        background: linear-gradient(135deg, #0A0F1E 0%, #1a2744 100%);
        border: 1px solid #3B82F6;
        border-radius: 12px;
        padding: 32px;
        margin-bottom: 24px;
        text-align: center;
    }
    .main-title { font-size: 2.4rem; font-weight: 700; color: #F9FAFB; margin: 0; }
    .main-subtitle { font-size: 1rem; color: #3B82F6; margin: 8px 0 4px 0; font-weight: 500; }
    .main-tagline { font-size: 0.85rem; color: #6B7280; margin: 0; }
    .account-card {
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 12px;
    }
    .account-name { font-size: 1rem; font-weight: 600; color: #F9FAFB; margin: 0 0 4px 0; }
    .account-meta { font-size: 0.8rem; color: #6B7280; margin: 0; }
    .badge-auto { background: #065F46; color: #10B981; padding: 2px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: 600; }
    .badge-human { background: #78350F; color: #F59E0B; padding: 2px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: 600; }
    .platform-card { background: #111827; border: 1px solid #1F2937; border-radius: 10px; padding: 20px; }
    .platform-item { display: flex; align-items: center; padding: 8px 0; border-bottom: 1px solid #1F2937; font-size: 0.85rem; color: #D1D5DB; }
    .rec-card { background: #111827; border: 1px solid #3B82F6; border-radius: 10px; padding: 24px; }
    .rec-action { font-size: 1.4rem; font-weight: 700; color: #3B82F6; text-transform: uppercase; letter-spacing: 1px; }
    .signal-item { background: #1F2937; border-radius: 6px; padding: 8px 12px; margin: 4px 0; font-size: 0.85rem; color: #D1D5DB; }
    .log-item { background: #111827; border: 1px solid #1F2937; border-radius: 8px; padding: 12px 16px; margin-bottom: 8px; font-size: 0.8rem; color: #9CA3AF; font-family: monospace; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .section-header { font-size: 0.75rem; font-weight: 600; color: #6B7280; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 12px; }
</style>
""", unsafe_allow_html=True)

if 'results' not in st.session_state:
    st.session_state.results = None
if 'selected' not in st.session_state:
    st.session_state.selected = None

st.markdown("""
<div class="main-header">
    <p class="main-title">⚡ Enterprise AI Platform</p>
    <p class="main-subtitle">Next Best Action Agent · Built on Claude API · From Scratch</p>
    <p class="main-tagline">Central governance layer · Edge intelligence · No AgentForce</p>
</div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([1.2, 1.8])

with col_left:
    st.markdown('<p class="section-header">Platform Status</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="platform-card">
        <div class="platform-item">✅ &nbsp; Policy Engine &nbsp;<span style="color:#6B7280;margin-left:auto">Active</span></div>
        <div class="platform-item">✅ &nbsp; Audit Logger &nbsp;<span style="color:#6B7280;margin-left:auto">Active</span></div>
        <div class="platform-item">✅ &nbsp; Guardrail &nbsp;<span style="color:#6B7280;margin-left:auto">Active</span></div>
        <div class="platform-item" style="border:none">✅ &nbsp; Evaluation Loop &nbsp;<span style="color:#6B7280;margin-left:auto">Active</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="section-header">Account Portfolio</p>', unsafe_allow_html=True)

    if st.button("▶ Run Portfolio Analysis", use_container_width=True, type="primary"):
        accounts = get_all_accounts()
        st.session_state.results = []
        st.session_state.selected = None

        with st.spinner("Analyzing portfolio..."):
            for account in accounts:
                result = run_analysis(account)
                st.session_state.results.append(result)

    if st.session_state.results:
        for i, result in enumerate(st.session_state.results):
            rec = result['recommendation']
            policy = result['policy']
            confidence = rec['confidence']
            action = rec['action'].replace('_', ' ').title()
            human = policy['human_review_required']
            badge = '<span class="badge-human">👤 HUMAN</span>' if human else '<span class="badge-auto">✓ AUTO</span>'
            conf_pct = int(confidence * 100)

            card_html = f"""
            <div class="account-card">
                <p class="account-name">{result['company']}</p>
                <p class="account-meta">{result['industry']} · ${result['arr']:,} ARR</p>
                <div style="margin-top:10px;display:flex;align-items:center;gap:10px">
                    {badge}
                    <span style="font-size:0.8rem;color:#3B82F6;font-weight:600">{conf_pct}%</span>
                    <span style="font-size:0.8rem;color:#6B7280">{action}</span>
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)

            if st.button(f"View Details →", key=f"btn_{i}", use_container_width=True):
                st.session_state.selected = i

with col_right:
    if st.session_state.selected is not None and st.session_state.results:
        result = st.session_state.results[st.session_state.selected]
        rec = result['recommendation']
        policy = result['policy']
        guardrail = result['guardrail']
        evaluation = result['evaluation']

        st.markdown(f"""
        <div style="margin-bottom:20px">
            <h2 style="color:#F9FAFB;margin:0">{result['company']}</h2>
            <p style="color:#6B7280;margin:4px 0 0 0">{result['industry']} · ${result['arr']:,} ARR</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<p class="section-header">Recommendation</p>', unsafe_allow_html=True)
        urgency_color = "#EF4444" if rec.get('urgency') == 'high' else "#F59E0B" if rec.get('urgency') == 'medium' else "#10B981"

        st.markdown(f"""
        <div class="rec-card">
            <p class="rec-action">{rec['action'].replace('_', ' ')}</p>
            <div style="display:flex;align-items:center;gap:12px;margin:8px 0 16px 0">
                <span style="font-size:1.2rem;font-weight:700;color:#3B82F6">{int(rec['confidence']*100)}%</span>
                <span style="color:{urgency_color};font-size:0.8rem;font-weight:600;text-transform:uppercase">
                    {rec.get('urgency','medium')} urgency
                </span>
            </div>
            <p style="color:#D1D5DB;font-size:0.9rem;line-height:1.6;margin:0">{rec['reason']}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<p class="section-header">Key Signals</p>', unsafe_allow_html=True)
        for signal in rec.get('key_signals', []):
            st.markdown(f'<div class="signal-item">◆ {signal}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<p class="section-header">Platform Checks</p>', unsafe_allow_html=True)
        human = policy['human_review_required']
        safe = guardrail['safe']
        approved = evaluation['approved']

        col_a, col_b, col_c = st.columns(3)
        with col_a:
            status = "👤 Human Review" if human else "✅ Auto-Approved"
            color = "#F59E0B" if human else "#10B981"
            st.markdown(f"""
            <div style="background:#111827;border:1px solid #1F2937;border-radius:8px;padding:12px;text-align:center">
                <p style="margin:0;font-size:0.7rem;color:#6B7280;text-transform:uppercase">Policy</p>
                <p style="margin:4px 0 0 0;font-size:0.8rem;color:{color};font-weight:600">{status}</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            g_status = "✅ Clean" if safe else "🚫 Blocked"
            g_color = "#10B981" if safe else "#EF4444"
            st.markdown(f"""
            <div style="background:#111827;border:1px solid #1F2937;border-radius:8px;padding:12px;text-align:center">
                <p style="margin:0;font-size:0.7rem;color:#6B7280;text-transform:uppercase">Guardrail</p>
                <p style="margin:4px 0 0 0;font-size:0.8rem;color:{g_color};font-weight:600">{g_status}</p>
            </div>
            """, unsafe_allow_html=True)
        with col_c:
            e_status = "✅ Approved" if approved else "⚠ Flagged"
            e_color = "#10B981" if approved else "#F59E0B"
            st.markdown(f"""
            <div style="background:#111827;border:1px solid #1F2937;border-radius:8px;padding:12px;text-align:center">
                <p style="margin:0;font-size:0.7rem;color:#6B7280;text-transform:uppercase">Evaluation</p>
                <p style="margin:4px 0 0 0;font-size:0.8rem;color:{e_color};font-weight:600">{e_status}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background:#111827;border:1px solid #1F2937;border-radius:8px;padding:12px">
            <p style="margin:0;font-size:0.8rem;color:#6B7280">Policy decision: <span style="color:#D1D5DB">{policy['reason']}</span></p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="background:#111827;border:1px dashed #1F2937;border-radius:12px;padding:60px;text-align:center;margin-top:20px">
            <p style="font-size:2rem;margin:0">⚡</p>
            <p style="color:#6B7280;margin:12px 0 0 0;font-size:0.9rem">
                Run portfolio analysis to see<br>account recommendations
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p class="section-header">Audit Log — Every Decision Recorded</p>', unsafe_allow_html=True)

logs = get_logs()
if logs:
    for log in reversed(logs[-6:]):
        human_flag = "👤 HUMAN" if log['human_review_required'] else "✓ AUTO"
        st.markdown(f"""
        <div class="log-item">
            {log['timestamp'][:19]} &nbsp;|&nbsp;
            <span style="color:#F9FAFB">{log['company']}</span> &nbsp;|&nbsp;
            {log['action_recommended'].replace('_',' ')} &nbsp;|&nbsp;
            <span style="color:#3B82F6">{int(log['confidence']*100)}%</span> &nbsp;|&nbsp;
            {human_flag}
        </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="log-item" style="text-align:center;color:#6B7280">
        No decisions logged yet. Run analysis to populate audit trail.
    </div>
    """, unsafe_allow_html=True)