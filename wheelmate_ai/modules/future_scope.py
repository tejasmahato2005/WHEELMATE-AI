"""
future_scope.py
Future Scope page — showcases planned features for presentation.
"""

import streamlit as st

FEATURES = [
    {
        "icon": "🎙️",
        "title": "Voice Assistant Integration",
        "desc": "Hands-free control of the entire WheelMate AI platform using natural voice commands, enabling users to set reminders, query the AI assistant, and navigate the app without touching a screen.",
        "tag": "Phase 2",
        "tag_color": "#00C9A7",
    },
    {
        "icon": "📡",
        "title": "Smart Sensor Connectivity",
        "desc": "Integration with IoT sensors attached to the wheelchair to monitor tyre pressure, posture angle, speed, and distance travelled — all displayed as live telemetry in the dashboard.",
        "tag": "Phase 2",
        "tag_color": "#00C9A7",
    },
    {
        "icon": "🗺️",
        "title": "Accessible Route Navigation",
        "desc": "A real-time accessible route planner that factors in kerb cuts, ramps, lift availability, and surface quality — helping users find the smoothest path to their destination.",
        "tag": "Phase 3",
        "tag_color": "#FFB347",
    },
    {
        "icon": "☁️",
        "title": "Cloud Accessibility Map Sharing",
        "desc": "A crowd-sourced, live-updated global accessibility map where users can submit and view wheelchair-friendly places, synchronised across all WheelMate AI users worldwide.",
        "tag": "Phase 3",
        "tag_color": "#FFB347",
    },
    {
        "icon": "🤖",
        "title": "Real AI Recommendation Engine",
        "desc": "Replace rule-based logic with a trained machine learning model that learns from each user's usage patterns, health data, and preferences to deliver hyper-personalised recommendations.",
        "tag": "Phase 3",
        "tag_color": "#FFB347",
    },
    {
        "icon": "🏥",
        "title": "Physiotherapist Collaboration Portal",
        "desc": "A dedicated portal allowing healthcare professionals to remotely review user activity data, adjust posture and stretch recommendations, and send health alerts directly through the app.",
        "tag": "Phase 4",
        "tag_color": "#FF6B6B",
    },
    {
        "icon": "📱",
        "title": "Native Mobile Application",
        "desc": "A fully native iOS and Android app with push notifications, offline functionality, and seamless pairing with Bluetooth-enabled wheelchair accessories.",
        "tag": "Phase 4",
        "tag_color": "#FF6B6B",
    },
    {
        "icon": "🔋",
        "title": "Electric Wheelchair Battery Monitoring",
        "desc": "Real-time battery level monitoring for electric wheelchairs with predictive range estimation, low-battery alerts, and charging schedule recommendations based on daily routes.",
        "tag": "Phase 2",
        "tag_color": "#00C9A7",
    },
    {
        "icon": "👥",
        "title": "Community & Peer Support Network",
        "desc": "An in-app community forum where wheelchair users can share tips, experiences, product reviews, and local accessibility insights, fostering a supportive peer network.",
        "tag": "Phase 3",
        "tag_color": "#FFB347",
    },
]

def show():
    st.markdown("""
    <div style='margin-bottom:1.5rem;'>
        <div style='font-family:Syne,sans-serif; font-size:1.7rem; font-weight:800; color:#E6EDF3;'>
            🚀 Future Scope
        </div>
        <div style='color:#8B949E; font-size:0.9rem; margin-top:0.3rem;'>
            The roadmap of planned features that will make WheelMate AI a complete wheelchair ecosystem.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Vision banner ─────────────────────────────────────────────────────────
    st.markdown("""
    <div style='
        background:linear-gradient(135deg,#161B22,#1C2333);
        border:1px solid #30363D; border-radius:18px;
        padding:2.5rem; margin-bottom:2rem; text-align:center;
        position:relative; overflow:hidden;
    '>
        <div style='
            position:absolute; top:0; left:0; right:0; bottom:0;
            background:radial-gradient(ellipse at center,#00c9a710 0%,transparent 70%);
        '></div>
        <div style='font-size:3rem; margin-bottom:1rem;'>🌍</div>
        <div style='font-family:Syne,sans-serif; font-size:1.4rem; font-weight:800; color:#E6EDF3;'>
            The Vision: An Intelligent Mobility Ecosystem
        </div>
        <div style='color:#8B949E; font-size:0.9rem; max-width:600px; margin:0.8rem auto 0;
                    line-height:1.7;'>
            WheelMate AI aims to grow from a smart companion app into a comprehensive
            platform that connects wheelchair users, healthcare providers, and smart devices —
            making mobility more comfortable, safe, and independent for everyone.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Roadmap phases legend ─────────────────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    for col, phase, color, note in [
        (c1, "Phase 1", "#8B949E", "Current ✓"),
        (c2, "Phase 2", "#00C9A7", "Near-term"),
        (c3, "Phase 3", "#FFB347", "Mid-term"),
        (c4, "Phase 4", "#FF6B6B", "Long-term"),
    ]:
        with col:
            st.markdown(f"""
            <div style='background:#161B22; border:1px solid #30363D; border-radius:10px;
                        padding:0.7rem; text-align:center; border-top:3px solid {color};'>
                <div style='font-family:Syne,sans-serif; font-weight:700; color:{color};
                            font-size:0.85rem;'>{phase}</div>
                <div style='color:#8B949E; font-size:0.72rem;'>{note}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Feature grid ──────────────────────────────────────────────────────────
    st.markdown("""
    <div style='font-family:Syne,sans-serif; font-weight:700; font-size:1rem;
                color:#E6EDF3; margin-bottom:1rem;'>📋 Planned Features</div>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    for i, f in enumerate(FEATURES):
        with cols[i % 3]:
            st.markdown(f"""
            <div style='
                background:#161B22; border:1px solid #30363D; border-radius:14px;
                padding:1.3rem; margin-bottom:1rem; height:100%;
                transition: border-color 0.2s;
            '>
                <div style='display:flex; justify-content:space-between; align-items:flex-start;
                            margin-bottom:0.7rem;'>
                    <div style='font-size:1.8rem;'>{f["icon"]}</div>
                    <span style='background:{f["tag_color"]}20; color:{f["tag_color"]};
                                border:1px solid {f["tag_color"]}50;
                                border-radius:20px; padding:2px 10px; font-size:0.7rem;
                                font-family:Syne,sans-serif; font-weight:600; white-space:nowrap;'>
                        {f["tag"]}
                    </span>
                </div>
                <div style='font-family:Syne,sans-serif; font-weight:700; color:#E6EDF3;
                            font-size:0.92rem; margin-bottom:0.5rem;'>{f["title"]}</div>
                <div style='color:#8B949E; font-size:0.81rem; line-height:1.55;'>{f["desc"]}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Tech stack future ─────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-family:Syne,sans-serif; font-weight:700; font-size:1rem;
                color:#E6EDF3; margin-bottom:1rem;'>🛠️ Planned Tech Stack (Future)</div>
    """, unsafe_allow_html=True)

    tech = [
        ("🧠", "Machine Learning", "TensorFlow / scikit-learn for personalised recommendations"),
        ("📡", "IoT Integration",  "Raspberry Pi + Arduino sensors for hardware telemetry"),
        ("☁️", "Cloud Backend",    "Firebase / AWS for real-time sync and global accessibility map"),
        ("📱", "Mobile",           "React Native for cross-platform iOS & Android apps"),
        ("🔒", "Auth & Privacy",   "OAuth 2.0 and end-to-end encryption for sensitive health data"),
    ]
    tech_cols = st.columns(len(tech))
    for col, (icon, title, desc) in zip(tech_cols, tech):
        with col:
            st.markdown(f"""
            <div style='background:#161B22; border:1px solid #30363D; border-radius:12px;
                        padding:1rem; text-align:center;'>
                <div style='font-size:1.5rem;'>{icon}</div>
                <div style='font-family:Syne,sans-serif; font-weight:700; color:#E6EDF3;
                            font-size:0.82rem; margin-top:0.4rem;'>{title}</div>
                <div style='color:#8B949E; font-size:0.72rem; margin-top:0.3rem;
                            line-height:1.4;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
