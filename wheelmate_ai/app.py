"""
WheelMate AI - Smart Wheelchair Companion Application
Main entry point for the Streamlit application.
"""

import streamlit as st
from modules import (
    dashboard,
    customization,
    reminders,
    accessibility,
    profile,
    chatbot,
    future_scope,
)
from modules.data_manager import init_data

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="WheelMate AI",
    page_icon="♿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────────────────────
# GLOBAL STYLING
# ─────────────────────────────────────────────────────────────

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --primary: #00C9A7;
    --bg-dark: #0D1117;
    --bg-card: #161B22;
    --bg-card2: #1C2333;
    --border: #30363D;
    --text-main: #E6EDF3;
    --text-muted: #8B949E;
    --radius: 14px;
}

/* Main App */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg-dark);
    color: var(--text-main);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: var(--bg-card) !important;
    border-right: 1px solid var(--border);
    min-width: 260px !important;
}

[data-testid="stSidebar"] * {
    color: var(--text-main);
}

/* Hide Streamlit branding only */
#MainMenu,
footer {
    visibility: hidden;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    border: none;
    padding: 0.7rem 1rem;
    background: linear-gradient(135deg, #00C9A7, #00A88A);
    color: #0D1117;
    font-weight: 700;
    font-family: 'Syne', sans-serif;
    transition: 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(0, 201, 167, 0.3);
}

/* Inputs */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div {
    background-color: var(--bg-card2) !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Metric Cards */
[data-testid="stMetric"] {
    background-color: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 6px;
}

::-webkit-scrollbar-thumb {
    background: #30363D;
    border-radius: 3px;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# INITIALIZE DATA
# ─────────────────────────────────────────────────────────────

init_data()

# ─────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────

with st.sidebar:

    st.markdown("""
    # ♿ WheelMate AI
    
    Smart Wheelchair Companion
    """)

    st.divider()

    pages = {
        "🏠 Dashboard": "Dashboard",
        "⚙️ Customization": "Customization",
        "🔔 Reminders": "Reminders",
        "♿ Accessibility": "Accessibility",
        "👤 My Profile": "Profile",
        "🤖 AI Assistant": "Chatbot",
        "🚀 Future Scope": "Future Scope",
    }

    if "current_page" not in st.session_state:
        st.session_state.current_page = "Dashboard"

    for label, page_name in pages.items():

        if st.button(label, use_container_width=True):
            st.session_state.current_page = page_name
            st.rerun()

    st.divider()

    st.caption("WheelMate AI v1.0")
    st.caption("2nd Semester Mini Project")

# ─────────────────────────────────────────────────────────────
# PAGE ROUTING
# ─────────────────────────────────────────────────────────────

page = st.session_state.current_page

if page == "Dashboard":
    dashboard.show()

elif page == "Customization":
    customization.show()

elif page == "Reminders":
    reminders.show()

elif page == "Accessibility":
    accessibility.show()

elif page == "Profile":
    profile.show()

elif page == "Chatbot":
    chatbot.show()

elif page == "Future Scope":
    future_scope.show()