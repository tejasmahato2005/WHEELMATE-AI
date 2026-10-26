"""
chatbot.py
AI Assistant — rule-based chatbot with predefined responses.
Looks like a modern chat interface with message bubbles and timestamps.
"""

import streamlit as st
from datetime import datetime
from modules.data_manager import get_chat, save_chat

# ── Response rules ────────────────────────────────────────────────────────────
# Each rule: (list of keyword triggers, response text, emoji)
RULES = [
    # Pain / discomfort
    (["back hurt", "back pain", "backache", "back ache"],
     "Lumbar pain is common for wheelchair users. Try adjusting your backrest angle and add a lumbar support cushion. Consider shifting posture every 45–60 minutes.", "🩺"),

    (["neck", "neck pain", "stiff neck"],
     "Neck tension can be caused by poor head support. Ensure your headrest is at the right height and take regular breaks to gently stretch your neck.", "🩺"),

    (["shoulder", "shoulder pain", "arm pain"],
     "To reduce shoulder strain: use a lightweight push rim, maintain an optimal seat height, and practice proper propulsion technique with full strokes.", "💪"),

    (["uncomfortable", "discomfort", "uneasy", "uncomfortable"],
     "Try shifting your sitting position slightly and check if your cushion is correctly inflated or positioned. Taking a 5-minute break every hour can also greatly reduce discomfort.", "🛋️"),

    (["pressure sore", "sore", "redness", "skin"],
     "Pressure sores are serious. Use a pressure-relief cushion, shift weight every 15–30 minutes, and keep skin clean and dry. Consult a doctor if redness persists.", "⚠️"),

    # Posture / sitting
    (["sit properly", "posture", "sitting", "how to sit"],
     "Good posture tips: Keep hips back in the seat, feet flat on footrests, knees at 90°, and back upright with lumbar support. Avoid leaning to one side.", "🪑"),

    (["lean", "tilt", "balance"],
     "If you feel off-balance, check that your wheelchair is on level ground. Adjust the anti-tippers and ensure even weight distribution across the seat.", "⚖️"),

    # Mobility / movement
    (["move", "mobility", "manoeuvre", "turn", "difficult to move"],
     "For easier manoeuvring: ensure tyre pressure is correct, clear any debris from wheels, and consider adjusting armrests for better reach.", "🔄"),

    (["outdoor", "rough terrain", "bumpy"],
     "For outdoor use, pneumatic (air-filled) tyres absorb shocks better. Consider anti-tip guards and gloves for prolonged outdoor propulsion.", "🌿"),

    # Fatigue
    (["tired", "fatigue", "exhausted", "energy"],
     "Fatigue is normal after long sessions. Take a 10-minute rest every 2 hours. Ensure adequate hydration and nutrition throughout the day.", "😴"),

    # Hydration
    (["water", "hydrat", "drink", "thirst"],
     "Hydration is vital for muscle function and skin health. Aim for 8 glasses of water daily and consider a water bottle holder for your wheelchair.", "💧"),

    # Maintenance
    (["mainten", "repair", "fix", "broken", "wheel", "tyre", "brake"],
     "Regular maintenance keeps your wheelchair safe. Check tyre pressure weekly, inspect brakes monthly, and tighten all bolts every 3 months.", "🔧"),

    (["battery", "charge", "electric"],
     "For electric wheelchairs: charge the battery overnight and avoid letting it drain completely. Store in a cool, dry place and check connectors regularly.", "🔋"),

    # Accessories
    (["cushion", "seat pad"],
     "The right cushion makes a huge difference! Gel cushions are great for pressure relief, foam for general comfort, and air cushions for custom pressure control.", "🛋️"),

    (["glove", "hand", "grip"],
     "Padded propulsion gloves protect your hands and improve grip during self-propulsion. They also reduce vibration transferred to your wrists.", "🧤"),

    # Mental / wellbeing
    (["lonely", "sad", "depress", "anxious", "stress"],
     "It's important to acknowledge how you feel. Consider connecting with wheelchair user communities online or locally. Peer support can be incredibly uplifting.", "🌟"),

    (["motivat", "inspire", "confident"],
     "Every day you navigate the world in your wheelchair is an act of strength. You're not limited — you're differently mobile. Keep going! 💪", "🌟"),

    # Greetings / general
    (["hello", "hi", "hey", "good morning", "good evening"],
     "Hello! I'm your WheelMate AI assistant. I'm here to help with wheelchair comfort, posture, maintenance tips, and more. What's on your mind?", "👋"),

    (["thank", "thanks", "appreciate"],
     "You're very welcome! Always here to help. Take care of yourself and don't hesitate to ask anything.", "😊"),

    (["bye", "goodbye", "see you"],
     "Take care! Remember to stay hydrated, adjust your posture regularly, and reach out anytime you need support. Goodbye! 👋", "👋"),

    (["help", "what can you do", "features"],
     "I can help with: back & posture advice, wheelchair maintenance tips, comfort recommendations, hydration reminders, and general wellbeing guidance. Just ask!", "🤖"),
]

FALLBACK = (
    "I'm still learning! For now, I can best help with wheelchair comfort, posture, "
    "maintenance tips, and wellbeing. Try asking: 'My back hurts', 'How to sit properly', "
    "or 'Wheelchair maintenance tips'.",
    "🤔"
)

def get_response(user_input: str):
    text = user_input.lower()
    for keywords, response, icon in RULES:
        if any(kw in text for kw in keywords):
            return response, icon
    return FALLBACK

# ── Main ──────────────────────────────────────────────────────────────────────
def show():
    st.markdown("""
    <div style='margin-bottom:1.5rem;'>
        <div style='font-family:Syne,sans-serif; font-size:1.7rem; font-weight:800; color:#E6EDF3;'>
            🤖 AI Assistant
        </div>
        <div style='color:#8B949E; font-size:0.9rem; margin-top:0.3rem;'>
            Ask me anything about wheelchair comfort, posture, maintenance, or wellbeing.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Suggestion chips ──────────────────────────────────────────────────────
    st.markdown("""
    <div style='font-family:Syne,sans-serif; font-size:0.8rem; color:#8B949E;
                margin-bottom:0.5rem;'>💬 Try asking:</div>
    """, unsafe_allow_html=True)

    chips = [
        "My back hurts", "How to sit properly?",
        "Wheelchair maintenance tips", "I feel tired",
    ]
    chip_cols = st.columns(len(chips))
    for i, chip in enumerate(chips):
        with chip_cols[i]:
            if st.button(chip, key=f"chip_{i}", use_container_width=True):
                _send_message(chip)
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Chat history ──────────────────────────────────────────────────────────
    history = get_chat()

    # Welcome message if empty
    if not history:
        history = [{
            "role": "assistant",
            "text": "👋 Hi! I'm WheelMate AI. I'm here to help with wheelchair comfort, posture tips, and wellbeing guidance. What would you like to know?",
            "icon": "🤖",
            "time": datetime.now().strftime("%H:%M"),
        }]
        save_chat(history)

    # Render messages
    chat_container = st.container()
    with chat_container:
        for msg in history:
            _render_message(msg)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Input ─────────────────────────────────────────────────────────────────
    col_input, col_send, col_clear = st.columns([7, 1.2, 1.2])
    with col_input:
        user_input = st.text_input("Message", placeholder="Type your message here...",
                                   label_visibility="collapsed", key="chat_input")
    with col_send:
        send = st.button("Send ➤", use_container_width=True)
    with col_clear:
        if st.button("🗑️ Clear", use_container_width=True):
            save_chat([])
            st.rerun()

    if send and user_input.strip():
        _send_message(user_input.strip())
        st.rerun()

def _send_message(text: str):
    history = get_chat()
    now = datetime.now().strftime("%H:%M")

    # User message
    history.append({"role": "user", "text": text, "icon": "👤", "time": now})

    # Bot response
    response, icon = get_response(text)
    history.append({"role": "assistant", "text": response, "icon": icon, "time": now})

    save_chat(history)

def _render_message(msg: dict):
    is_user = msg["role"] == "user"
    align   = "flex-end" if is_user else "flex-start"
    bg      = "#00c9a720" if is_user else "#161B22"
    border  = "#00C9A750" if is_user else "#30363D"
    color   = "#7CFFCB" if is_user else "#E6EDF3"

    st.markdown(f"""
    <div style='display:flex; justify-content:{align}; margin-bottom:0.7rem;'>
        <div style='
            max-width:72%; background:{bg}; border:1px solid {border};
            border-radius:14px; padding:0.8rem 1.1rem;
            {"border-bottom-right-radius:4px;" if is_user else "border-bottom-left-radius:4px;"}
        '>
            <div style='display:flex; align-items:center; gap:0.4rem; margin-bottom:0.3rem;'>
                <span style='font-size:0.9rem;'>{msg.get("icon","💬")}</span>
                <span style='color:#8B949E; font-size:0.7rem;'>
                    {"You" if is_user else "WheelMate AI"} · {msg.get("time","—")}
                </span>
            </div>
            <div style='color:{color}; font-size:0.87rem; line-height:1.55;'>{msg["text"]}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
