"""
customization.py
Wheelchair Customization Assistant — rule-based recommendation engine.
"""

import streamlit as st

# ── Rule engine ───────────────────────────────────────────────────────────────
def generate_recommendations(wtype, usage, hours, issues, cushion, back_pain):
    recs = []
    score = 70  # base comfort score

    # Cushion recommendations
    if cushion == "Gel" or "pressure sores" in issues.lower():
        recs.append(("🛋️", "Gel Cushion", "A high-density gel cushion distributes pressure evenly and reduces the risk of pressure sores during long sessions.", "High Priority"))
        score += 5
    elif cushion == "Foam":
        recs.append(("🛋️", "Memory Foam Cushion", "Memory foam conforms to your body shape for personalised support throughout the day.", "Medium Priority"))
        score += 3
    elif cushion == "Air":
        recs.append(("💨", "Air-Adjustable Cushion", "Air cushions allow custom pressure control — ideal for users with variable comfort needs.", "High Priority"))
        score += 6

    # Wheel recommendations
    if usage == "Outdoor" or usage == "Both":
        recs.append(("🔵", "All-Terrain Wheels", "Wider pneumatic tyres provide better grip on uneven outdoor surfaces and reduce vibration.", "Medium Priority"))
        score += 4
    if usage == "Indoor":
        recs.append(("⚪", "Lightweight Inline Wheels", "Slim, hard-surface wheels allow smoother indoor movement and easier manoeuvring in tight spaces.", "Low Priority"))
        score += 2

    # Back support
    if back_pain or "back" in issues.lower():
        recs.append(("🪑", "Adjustable Lumbar Support", "A contoured lumbar pad maintains the natural curve of your spine and significantly reduces lower-back strain.", "High Priority"))
        score += 8
    if hours >= 8:
        recs.append(("⏱️", "Tilt-in-Space Feature", "For 8+ hour daily users, a tilt function redistributes pressure and prevents postural fatigue.", "High Priority"))
        score += 6

    # Armrests
    if "arm" in issues.lower() or "shoulder" in issues.lower():
        recs.append(("💪", "Padded Flip-Back Armrests", "Removable, padded armrests reduce shoulder strain and allow closer access to surfaces.", "Medium Priority"))
        score += 4

    # Weight/frame
    if wtype == "Manual" and hours >= 6:
        recs.append(("🏋️", "Lightweight Aluminium Frame", "Switching to an ultra-light aluminium or titanium frame reduces self-propulsion fatigue for heavy users.", "Medium Priority"))
        score += 3

    if wtype == "Electric":
        recs.append(("🔋", "Extended Battery Pack", "An additional battery module ensures you never run out of power during long outdoor trips.", "Low Priority"))
        score += 2

    # Footrest
    if "foot" in issues.lower() or "leg" in issues.lower():
        recs.append(("🦶", "Elevating Leg Rests", "Elevating footrests help reduce swelling and improve circulation during extended sitting periods.", "Medium Priority"))
        score += 4

    # Maintenance tip
    recs.append(("🔧", "Regular Maintenance Checks", "Inspect tyre pressure, brakes, and frame bolts weekly to ensure safe and smooth operation.", "Routine"))

    return recs, min(score, 100)

# ── Priority badge ────────────────────────────────────────────────────────────
PRIORITY_COLORS = {
    "High Priority":   ("#FF6B6B", "#ff6b6b20"),
    "Medium Priority": ("#FFB347", "#ffb34720"),
    "Low Priority":    ("#8B949E", "#8b949e20"),
    "Routine":         ("#00C9A7", "#00c9a720"),
}

def priority_badge(priority: str):
    color, bg = PRIORITY_COLORS.get(priority, ("#8B949E", "#8b949e20"))
    return f"""<span style='background:{bg}; color:{color}; border:1px solid {color}50;
               border-radius:20px; padding:2px 10px; font-size:0.72rem;
               font-family:Syne,sans-serif; font-weight:600;'>{priority}</span>"""

# ── Main ──────────────────────────────────────────────────────────────────────
def show():
    st.markdown("""
    <div style='margin-bottom:1.5rem;'>
        <div style='font-family:Syne,sans-serif; font-size:1.7rem; font-weight:800; color:#E6EDF3;'>
            ⚙️ Wheelchair Customization Assistant
        </div>
        <div style='color:#8B949E; font-size:0.9rem; margin-top:0.3rem;'>
            Tell us about your wheelchair usage and we'll generate personalised recommendations.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Input form ────────────────────────────────────────────────────────────
    with st.form("customization_form"):
        st.markdown("### 📋 Your Wheelchair Profile")
        c1, c2 = st.columns(2)
        with c1:
            wtype   = st.selectbox("Wheelchair Type",      ["Manual", "Electric", "Sport", "Tilt-in-Space"])
            usage   = st.selectbox("Primary Usage",         ["Indoor", "Outdoor", "Both"])
            cushion = st.selectbox("Cushion Preference",    ["Gel", "Foam", "Air", "None"])
        with c2:
            hours     = st.slider("Daily Usage (hours)", 1, 16, 8)
            back_pain = st.checkbox("Experiencing back pain?", value=True)

        issues = st.text_area(
            "Describe any comfort issues (optional)",
            placeholder="e.g. lower back pain, shoulder strain, foot numbness, pressure sores...",
            height=90
        )

        submitted = st.form_submit_button("🤖 Generate AI Recommendations", use_container_width=True)

    # ── Results ───────────────────────────────────────────────────────────────
    if submitted:
        recs, score = generate_recommendations(wtype, usage, hours, issues, cushion, back_pain)

        st.markdown("<br>", unsafe_allow_html=True)

        # Comfort score
        score_color = "#00C9A7" if score >= 80 else ("#FFB347" if score >= 60 else "#FF6B6B")
        st.markdown(f"""
        <div style='
            background:#161B22; border:1px solid #30363D; border-radius:14px;
            padding:1.5rem 2rem; margin-bottom:1.5rem;
            display:flex; align-items:center; gap:2rem;
        '>
            <div>
                <div style='font-family:Syne,sans-serif; font-size:3rem; font-weight:800;
                            color:{score_color};'>{score}</div>
                <div style='color:#8B949E; font-size:0.8rem;'>Comfort Score / 100</div>
            </div>
            <div style='flex:1;'>
                <div style='height:10px; background:#30363D; border-radius:5px; overflow:hidden;'>
                    <div style='height:100%; width:{score}%; background:linear-gradient(90deg,{score_color},{score_color}99);
                                border-radius:5px; transition:width 0.8s ease;'></div>
                </div>
                <div style='color:#C9D1D9; font-size:0.88rem; margin-top:0.6rem;'>
                    {"🌟 Excellent setup!" if score >= 85 else ("✅ Good, with room for improvement." if score >= 70 else "⚠️ Several improvements recommended.")}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"### 💡 {len(recs)} Recommendations for You")

        cols = st.columns(2)
        for i, (icon, title, desc, priority) in enumerate(recs):
            with cols[i % 2]:
                st.markdown(f"""
                <div style='
                    background:#161B22; border:1px solid #30363D; border-radius:14px;
                    padding:1.2rem 1.4rem; margin-bottom:1rem; height:100%;
                '>
                    <div style='display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.6rem;'>
                        <div style='font-size:1.5rem;'>{icon}</div>
                        {priority_badge(priority)}
                    </div>
                    <div style='font-family:Syne,sans-serif; font-weight:700; color:#E6EDF3;
                                font-size:0.95rem; margin-bottom:0.4rem;'>{title}</div>
                    <div style='color:#8B949E; font-size:0.83rem; line-height:1.55;'>{desc}</div>
                </div>
                """, unsafe_allow_html=True)
    else:
        # Placeholder illustration
        st.markdown("""
        <div style='
            text-align:center; padding:4rem 2rem;
            background:#161B22; border:1px dashed #30363D; border-radius:18px;
            margin-top:1rem;
        '>
            <div style='font-size:4rem;'>⚙️</div>
            <div style='font-family:Syne,sans-serif; color:#E6EDF3; font-size:1.1rem;
                        font-weight:700; margin-top:1rem;'>
                Fill in your profile above
            </div>
            <div style='color:#8B949E; font-size:0.87rem; margin-top:0.4rem;'>
                Our AI engine will generate personalised recommendations for your wheelchair setup.
            </div>
        </div>
        """, unsafe_allow_html=True)
