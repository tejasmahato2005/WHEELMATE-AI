"""
dashboard.py
Homepage dashboard for WheelMate AI.
Shows summary stats, quick suggestions, and an overview of all modules.
"""

import streamlit as st
from datetime import datetime
from modules.data_manager import get_profile, get_reminders, get_reviews

# ── Helper: render a stat card ────────────────────────────────────────────────
def stat_card(icon: str, label: str, value: str, color: str = "#00C9A7"):
    st.markdown(f"""
    <div style='
        background:#161B22; border:1px solid #30363D; border-radius:14px;
        padding:1.2rem 1.4rem; height:100%;
        border-top: 3px solid {color};
    '>
        <div style='font-size:1.8rem'>{icon}</div>
        <div style='color:#8B949E; font-size:0.75rem; margin-top:0.4rem;
                    font-family:DM Sans,sans-serif; letter-spacing:0.05em; text-transform:uppercase;'>
            {label}
        </div>
        <div style='font-family:Syne,sans-serif; font-size:1.6rem; font-weight:700;
                    color:#E6EDF3; margin-top:0.2rem;'>
            {value}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Helper: suggestion card ───────────────────────────────────────────────────
def suggestion_card(text: str, icon: str = "💡"):
    st.markdown(f"""
    <div style='
        background:linear-gradient(135deg,#00c9a710,#00c9a705);
        border:1px solid #00C9A730; border-radius:12px;
        padding:0.9rem 1.1rem; margin-bottom:0.6rem;
        display:flex; align-items:flex-start; gap:0.7rem;
    '>
        <span style='font-size:1.1rem;'>{icon}</span>
        <span style='color:#C9D1D9; font-size:0.88rem; line-height:1.5;'>{text}</span>
    </div>
    """, unsafe_allow_html=True)

# ── Main ──────────────────────────────────────────────────────────────────────
def show():
    profile   = get_profile()
    reminders = get_reminders()
    reviews   = get_reviews()

    hour = datetime.now().hour
    greeting = "Good morning" if hour < 12 else ("Good afternoon" if hour < 17 else "Good evening")

    # ── Hero header ───────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style='
        background:linear-gradient(135deg,#161B22 0%,#1C2333 100%);
        border:1px solid #30363D; border-radius:18px;
        padding:2rem 2.5rem; margin-bottom:1.5rem;
        position:relative; overflow:hidden;
    '>
        <div style='
            position:absolute; top:-40px; right:-40px;
            width:200px; height:200px; border-radius:50%;
            background:radial-gradient(circle,#00c9a720,transparent 70%);
        '></div>
        <div style='font-family:Syne,sans-serif; font-size:0.8rem; color:#00C9A7;
                    letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.3rem;'>
            {greeting} 👋
        </div>
        <div style='font-family:Syne,sans-serif; font-size:2rem; font-weight:800; color:#E6EDF3;'>
            Welcome back, {profile.get("username", "User").split()[0]}
        </div>
        <div style='color:#8B949E; font-size:0.9rem; margin-top:0.4rem;'>
            Your wheelchair companion is ready. Here's your daily overview.
        </div>
        <div style='margin-top:1rem; display:inline-block;
                    background:#00c9a720; border:1px solid #00C9A750;
                    border-radius:20px; padding:0.3rem 0.9rem;
                    color:#00C9A7; font-size:0.8rem; font-family:Syne,sans-serif;'>
            ♿ {profile.get("wheelchair_type","Manual")} Wheelchair
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Stat cards row ────────────────────────────────────────────────────────
    pending   = sum(1 for r in reminders if not r["completed"])
    done      = sum(1 for r in reminders if r["completed"])
    avg_score = 0
    if reviews:
        avg_score = round(
            sum((r["ramp"]+r["washroom"]+r["elevator"]+r["space"])/4 for r in reviews) / len(reviews), 1
        )

    c1, c2, c3, c4 = st.columns(4)
    with c1: stat_card("🔔", "Pending Reminders", str(pending), "#00C9A7")
    with c2: stat_card("✅", "Completed Today",   str(done),    "#7CFFCB")
    with c3: stat_card("⭐", "Avg Access Score",  f"{avg_score}/5", "#FFB347")
    with c4: stat_card("📍", "Places Reviewed",   str(len(reviews)), "#FF6B6B")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Two-column layout ─────────────────────────────────────────────────────
    left, right = st.columns([1.4, 1], gap="large")

    with left:
        # AI suggestions
        st.markdown("""
        <div style='font-family:Syne,sans-serif; font-weight:700; font-size:1rem;
                    color:#E6EDF3; margin-bottom:0.8rem;'>
            🤖 AI Suggestions
        </div>
        """, unsafe_allow_html=True)

        suggestions = _get_suggestions(profile, reminders)
        for icon, text in suggestions:
            suggestion_card(text, icon)

        st.markdown("<br>", unsafe_allow_html=True)

        # Wheelchair profile summary
        st.markdown("""
        <div style='font-family:Syne,sans-serif; font-weight:700; font-size:1rem;
                    color:#E6EDF3; margin-bottom:0.8rem;'>
            ♿ Wheelchair Profile
        </div>
        """, unsafe_allow_html=True)
        _profile_summary(profile)

    with right:
        # Reminder summary
        st.markdown("""
        <div style='font-family:Syne,sans-serif; font-weight:700; font-size:1rem;
                    color:#E6EDF3; margin-bottom:0.8rem;'>
            🔔 Today's Reminders
        </div>
        """, unsafe_allow_html=True)
        for r in reminders[:5]:
            status_color = "#00C9A7" if r["completed"] else "#FF6B6B"
            status_icon  = "✅" if r["completed"] else "⏳"
            st.markdown(f"""
            <div style='
                background:#161B22; border:1px solid #30363D; border-radius:10px;
                padding:0.7rem 1rem; margin-bottom:0.5rem;
                border-left:3px solid {status_color};
            '>
                <div style='display:flex; justify-content:space-between; align-items:center;'>
                    <span style='color:#C9D1D9; font-size:0.85rem;'>{status_icon} {r["message"]}</span>
                    <span style='color:#8B949E; font-size:0.72rem;'>{r["interval"]}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Quick nav buttons
        st.markdown("""
        <div style='font-family:Syne,sans-serif; font-weight:700; font-size:1rem;
                    color:#E6EDF3; margin-bottom:0.8rem;'>
            ⚡ Quick Actions
        </div>
        """, unsafe_allow_html=True)

        qa_cols = st.columns(2)
        actions = [
            ("⚙️ Customize", "Customization"),
            ("🔔 Reminders", "Reminders"),
            ("♿ Accessibility", "Accessibility"),
            ("🤖 AI Chat", "Chatbot"),
        ]
        for i, (label, page) in enumerate(actions):
            with qa_cols[i % 2]:
                if st.button(label, key=f"qa_{page}", use_container_width=True):
                    st.session_state.current_page = page
                    st.rerun()

# ── Helpers ───────────────────────────────────────────────────────────────────
def _get_suggestions(profile: dict, reminders: list):
    tips = []
    if profile.get("back_pain"):
        tips.append(("🪑", "Consider adjusting lumbar support to relieve back discomfort."))
    if profile.get("daily_hours", 0) >= 8:
        tips.append(("⏱️", "You use your wheelchair 8+ hours daily — schedule stretch breaks every hour."))
    if profile.get("indoor_outdoor") == "Both":
        tips.append(("🔧", "Dual-use wheelchairs benefit from weekly tyre pressure checks."))
    if profile.get("cushion_pref") == "Gel":
        tips.append(("💆", "Gel cushions should be inspected for wear every 3 months."))
    if sum(1 for r in reminders if not r["completed"]) > 2:
        tips.append(("🔔", "You have pending reminders — check the Reminders page to stay on track."))
    tips.append(("💧", "Stay hydrated! Aim for 8 glasses of water throughout the day."))
    return tips[:4]

def _profile_summary(profile: dict):
    fields = [
        ("👤 Name",          profile.get("username", "—")),
        ("♿ Wheelchair",     profile.get("wheelchair_type", "—")),
        ("⏱️ Daily Usage",   f"{profile.get('daily_hours', '—')} hrs"),
        ("🌐 Usage Mode",    profile.get("indoor_outdoor", "—")),
        ("🛋️ Cushion",       profile.get("cushion_pref", "—")),
        ("🩺 Back Pain",     "Yes" if profile.get("back_pain") else "No"),
    ]
    for label, value in fields:
        st.markdown(f"""
        <div style='
            display:flex; justify-content:space-between; align-items:center;
            padding:0.55rem 0; border-bottom:1px solid #30363D;
        '>
            <span style='color:#8B949E; font-size:0.84rem;'>{label}</span>
            <span style='color:#E6EDF3; font-size:0.84rem; font-weight:500;'>{value}</span>
        </div>
        """, unsafe_allow_html=True)
