"""
profile.py
User profile page — view and edit wheelchair user profile.
"""

import streamlit as st
from modules.data_manager import get_profile, save_profile

def show():
    profile = get_profile()

    st.markdown("""
    <div style='margin-bottom:1.5rem;'>
        <div style='font-family:Syne,sans-serif; font-size:1.7rem; font-weight:800; color:#E6EDF3;'>
            👤 My Profile
        </div>
        <div style='color:#8B949E; font-size:0.9rem; margin-top:0.3rem;'>
            Manage your wheelchair user profile. This information powers personalised recommendations.
        </div>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1, 1.4], gap="large")

    # ── Avatar / summary card ─────────────────────────────────────────────────
    with left:
        initials = "".join(w[0].upper() for w in profile.get("username","U U").split()[:2])
        st.markdown(f"""
        <div style='
            background:#161B22; border:1px solid #30363D; border-radius:18px;
            padding:2rem; text-align:center;
        '>
            <div style='
                width:80px; height:80px; border-radius:50%; margin:0 auto 1rem;
                background:linear-gradient(135deg,#00C9A7,#7CFFCB);
                display:flex; align-items:center; justify-content:center;
                font-family:Syne,sans-serif; font-size:1.8rem; font-weight:800;
                color:#0D1117;
            '>{initials}</div>
            <div style='font-family:Syne,sans-serif; font-size:1.2rem; font-weight:700;
                        color:#E6EDF3;'>{profile.get("username","—")}</div>
            <div style='color:#8B949E; font-size:0.82rem; margin-top:0.3rem;'>
                ♿ {profile.get("wheelchair_type","—")} Wheelchair User
            </div>

            
        """, unsafe_allow_html=True)

        fields = [
            ("⏱️ Daily Usage",   f"{profile.get('daily_hours','—')} hours/day"),
            ("🌐 Usage Mode",    profile.get("indoor_outdoor","—")),
            ("🛋️ Cushion",       profile.get("cushion_pref","—")),
            ("⚙️ Comfort Level", profile.get("comfort_setting","—")),
            ("🩺 Back Pain",     "Yes" if profile.get("back_pain") else "No"),
        ]

        for label, value in fields:
            st.markdown(f"""
            <div style='display:flex; justify-content:space-between;
                        padding:0.5rem 0; border-bottom:1px solid #30363D;'>
                <span style='color:#8B949E; font-size:0.82rem;'>{label}</span>
                <span style='color:#E6EDF3; font-size:0.82rem; font-weight:500;'>{value}</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div></div>", unsafe_allow_html=True)

    # ── Edit form ─────────────────────────────────────────────────────────────
    with right:
        st.markdown("""
        <div style='font-family:Syne,sans-serif; font-weight:700; font-size:1rem;
                    color:#E6EDF3; margin-bottom:1rem;'>✏️ Edit Profile</div>
        """, unsafe_allow_html=True)

        with st.form("profile_form"):
            username = st.text_input("Full Name", value=profile.get("username",""))
            wtype    = st.selectbox("Wheelchair Type",
                                    ["Manual","Electric","Sport","Tilt-in-Space"],
                                    index=["Manual","Electric","Sport","Tilt-in-Space"].index(
                                        profile.get("wheelchair_type","Manual")))
            hours    = st.slider("Daily Usage (hours)", 1, 16, profile.get("daily_hours", 8))
            usage    = st.selectbox("Primary Usage",
                                    ["Indoor","Outdoor","Both"],
                                    index=["Indoor","Outdoor","Both"].index(
                                        profile.get("indoor_outdoor","Both")))
            cushion  = st.selectbox("Cushion Preference",
                                    ["Gel","Foam","Air","None"],
                                    index=["Gel","Foam","Air","None"].index(
                                        profile.get("cushion_pref","Gel")))
            comfort  = st.selectbox("Comfort Setting",
                                    ["Low","Medium","High"],
                                    index=["Low","Medium","High"].index(
                                        profile.get("comfort_setting","Medium")))
            back_pain = st.checkbox("Experiencing back pain?", value=profile.get("back_pain", False))

            if st.form_submit_button("💾 Save Profile", use_container_width=True):
                save_profile({
                    "username":        username,
                    "wheelchair_type": wtype,
                    "daily_hours":     hours,
                    "indoor_outdoor":  usage,
                    "cushion_pref":    cushion,
                    "comfort_setting": comfort,
                    "back_pain":       back_pain,
                })
                st.success("✅ Profile saved successfully!")
                st.rerun()
