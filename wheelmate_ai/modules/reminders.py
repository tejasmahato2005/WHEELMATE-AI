"""
reminders.py
Smart Reminder System — add, view, complete, and delete reminders.
"""

import streamlit as st
from modules.data_manager import (
    get_reminders, add_reminder, toggle_reminder, delete_reminder
)

REMINDER_ICONS = {
    "Hydration":   "💧",
    "Posture":     "🪑",
    "Medicine":    "💊",
    "Stretch":     "🤸",
    "Maintenance": "🔧",
    "Custom":      "📝",
}

TYPE_COLORS = {
    "Hydration":   "#4FC3F7",
    "Posture":     "#00C9A7",
    "Medicine":    "#FF6B6B",
    "Stretch":     "#FFB347",
    "Maintenance": "#CE93D8",
    "Custom":      "#8B949E",
}

def show():
    st.markdown("""
    <div style='margin-bottom:1.5rem;'>
        <div style='font-family:Syne,sans-serif; font-size:1.7rem; font-weight:800; color:#E6EDF3;'>
            🔔 Smart Reminder System
        </div>
        <div style='color:#8B949E; font-size:0.9rem; margin-top:0.3rem;'>
            Stay on top of hydration, posture, medication, and maintenance — all in one place.
        </div>
    </div>
    """, unsafe_allow_html=True)

    reminders = get_reminders()

    # ── Summary strip ─────────────────────────────────────────────────────────
    total   = len(reminders)
    done    = sum(1 for r in reminders if r["completed"])
    pending = total - done

    c1, c2, c3 = st.columns(3)
    def mini_card(col, icon, label, value, color):
        with col:
            st.markdown(f"""
            <div style='background:#161B22; border:1px solid #30363D; border-radius:12px;
                        padding:1rem; text-align:center; border-top:3px solid {color};'>
                <div style='font-size:1.4rem;'>{icon}</div>
                <div style='font-family:Syne,sans-serif; font-size:1.4rem; font-weight:700;
                            color:{color}; margin-top:0.2rem;'>{value}</div>
                <div style='color:#8B949E; font-size:0.75rem;'>{label}</div>
            </div>
            """, unsafe_allow_html=True)

    mini_card(c1, "📋", "Total Reminders", total,   "#8B949E")
    mini_card(c2, "⏳", "Pending",         pending, "#FF6B6B")
    mini_card(c3, "✅", "Completed",        done,    "#00C9A7")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Add reminder form ─────────────────────────────────────────────────────
    with st.expander("➕ Add New Reminder", expanded=False):
        with st.form("add_reminder_form"):
            col1, col2 = st.columns(2)
            with col1:
                rtype    = st.selectbox("Reminder Type", list(REMINDER_ICONS.keys()))
                interval = st.selectbox("Interval", [
                    "Every 30 minutes", "Every 1 hour", "Every 2 hours",
                    "Every 3 hours", "Daily at 8 AM", "Daily at 2 PM",
                    "Daily at 8 PM", "Weekly",
                ])
            with col2:
                message = st.text_input("Message", placeholder="e.g. Time to drink water!")

            if st.form_submit_button("Add Reminder", use_container_width=True):
                if message.strip():
                    add_reminder(rtype, message.strip(), interval)
                    st.success("✅ Reminder added!")
                    st.rerun()
                else:
                    st.warning("Please enter a message.")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Reminder cards ────────────────────────────────────────────────────────
    # Group by completion status
    pending_list   = [r for r in reminders if not r["completed"]]
    completed_list = [r for r in reminders if r["completed"]]

    if pending_list:
        st.markdown("""
        <div style='font-family:Syne,sans-serif; font-weight:700; font-size:1rem;
                    color:#E6EDF3; margin-bottom:0.8rem;'>⏳ Pending</div>
        """, unsafe_allow_html=True)
        _render_list(pending_list)

    if completed_list:
        st.markdown("""
        <div style='font-family:Syne,sans-serif; font-weight:700; font-size:1rem;
                    color:#E6EDF3; margin-top:1.2rem; margin-bottom:0.8rem;'>✅ Completed</div>
        """, unsafe_allow_html=True)
        _render_list(completed_list)

def _render_list(reminders: list):
    for r in reminders:
        icon  = REMINDER_ICONS.get(r["type"], "📝")
        color = TYPE_COLORS.get(r["type"], "#8B949E")
        done  = r["completed"]
        opacity = "0.5" if done else "1"

        col_card, col_done, col_del = st.columns([7, 1.2, 1.2])
        with col_card:
            st.markdown(f"""
            <div style='
                background:#161B22; border:1px solid #30363D; border-radius:12px;
                padding:0.9rem 1.2rem; border-left:4px solid {color};
                opacity:{opacity};
            '>
                <div style='display:flex; justify-content:space-between; align-items:center;'>
                    <div>
                        <span style='font-size:1.1rem; margin-right:0.5rem;'>{icon}</span>
                        <span style='font-family:Syne,sans-serif; font-weight:600;
                                    color:#E6EDF3; font-size:0.9rem;'>{r["type"]}</span>
                    </div>
                    <span style='background:{color}20; color:{color}; border-radius:20px;
                                padding:2px 10px; font-size:0.72rem; border:1px solid {color}50;'>
                        {r["interval"]}
                    </span>
                </div>
                <div style='color:#C9D1D9; font-size:0.85rem; margin-top:0.4rem;
                            {"text-decoration:line-through; color:#8B949E;" if done else ""}'>
                    {r["message"]}
                </div>
                <div style='color:#8B949E; font-size:0.72rem; margin-top:0.3rem;'>
                    Added: {r.get("created","—")}
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_done:
            label = "↩️ Undo" if done else "✅ Done"
            if st.button(label, key=f"toggle_{r['id']}", use_container_width=True):
                toggle_reminder(r["id"])
                st.rerun()
        with col_del:
            if st.button("🗑️ Del", key=f"del_{r['id']}", use_container_width=True):
                delete_reminder(r["id"])
                st.rerun()
