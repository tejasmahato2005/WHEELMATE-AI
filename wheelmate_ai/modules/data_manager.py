"""
data_manager.py
Handles all local JSON-based storage for WheelMate AI.
"""

import json
import os
from datetime import datetime

# ── File paths ────────────────────────────────────────────────────────────────
DATA_DIR    = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
PROFILE_F   = os.path.join(DATA_DIR, "profile.json")
REMINDERS_F = os.path.join(DATA_DIR, "reminders.json")
REVIEWS_F   = os.path.join(DATA_DIR, "reviews.json")
CHAT_F      = os.path.join(DATA_DIR, "chat_history.json")

# ── Defaults ──────────────────────────────────────────────────────────────────
DEFAULT_PROFILE = {
    "username": "Alex Johnson",
    "wheelchair_type": "Manual",
    "daily_hours": 8,
    "comfort_setting": "Medium",
    "back_pain": True,
    "indoor_outdoor": "Both",
    "cushion_pref": "Gel",
}

DEFAULT_REMINDERS = [
    {"id": 1, "type": "Hydration",    "message": "Time to drink water! 💧",            "interval": "Every 2 hours", "completed": False, "created": "2024-01-01"},
    {"id": 2, "type": "Posture",      "message": "Adjust your posture now. 🪑",        "interval": "Every 1 hour",  "completed": False, "created": "2024-01-01"},
    {"id": 3, "type": "Medicine",     "message": "Take your afternoon medication. 💊", "interval": "Daily at 2 PM", "completed": True,  "created": "2024-01-01"},
    {"id": 4, "type": "Stretch",      "message": "Do a 5-minute stretch! 🤸",          "interval": "Every 3 hours", "completed": False, "created": "2024-01-01"},
    {"id": 5, "type": "Maintenance",  "message": "Check wheelchair tyre pressure. 🔧", "interval": "Weekly",        "completed": False, "created": "2024-01-01"},
]

DEFAULT_REVIEWS = [
    {"id": 1, "place": "Phoenix Mall",       "ramp": 4, "washroom": 3, "elevator": 5, "space": 4, "note": "Good ramps, elevator works well.", "date": "2024-06-10"},
    {"id": 2, "place": "City Hospital",      "ramp": 5, "washroom": 5, "elevator": 5, "space": 5, "note": "Excellent accessibility throughout.", "date": "2024-06-12"},
    {"id": 3, "place": "Central Park",       "ramp": 3, "washroom": 2, "elevator": 1, "space": 5, "note": "Open space but washroom needs work.", "date": "2024-06-15"},
    {"id": 4, "place": "Metro Station",      "ramp": 4, "washroom": 3, "elevator": 4, "space": 3, "note": "Mostly accessible, rush hour tight.", "date": "2024-06-18"},
    {"id": 5, "place": "Public Library",     "ramp": 5, "washroom": 4, "elevator": 5, "space": 5, "note": "One of the best accessible venues!", "date": "2024-06-20"},
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def _read(path: str, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)

def _write(path: str, data):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# ── Public API ────────────────────────────────────────────────────────────────
def init_data():
    """Create default data files if they don't exist yet."""
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(PROFILE_F):
        _write(PROFILE_F, DEFAULT_PROFILE)
    if not os.path.exists(REMINDERS_F):
        _write(REMINDERS_F, DEFAULT_REMINDERS)
    if not os.path.exists(REVIEWS_F):
        _write(REVIEWS_F, DEFAULT_REVIEWS)
    if not os.path.exists(CHAT_F):
        _write(CHAT_F, [])

# ── Profile ───────────────────────────────────────────────────────────────────
def get_profile():
    return _read(PROFILE_F, DEFAULT_PROFILE)

def save_profile(data: dict):
    _write(PROFILE_F, data)

# ── Reminders ─────────────────────────────────────────────────────────────────
def get_reminders():
    return _read(REMINDERS_F, DEFAULT_REMINDERS)

def save_reminders(reminders: list):
    _write(REMINDERS_F, reminders)

def add_reminder(rtype: str, message: str, interval: str):
    reminders = get_reminders()
    new_id = max((r["id"] for r in reminders), default=0) + 1
    reminders.append({
        "id": new_id,
        "type": rtype,
        "message": message,
        "interval": interval,
        "completed": False,
        "created": datetime.now().strftime("%Y-%m-%d"),
    })
    save_reminders(reminders)

def toggle_reminder(rid: int):
    reminders = get_reminders()
    for r in reminders:
        if r["id"] == rid:
            r["completed"] = not r["completed"]
    save_reminders(reminders)

def delete_reminder(rid: int):
    reminders = [r for r in get_reminders() if r["id"] != rid]
    save_reminders(reminders)

# ── Reviews ───────────────────────────────────────────────────────────────────
def get_reviews():
    return _read(REVIEWS_F, DEFAULT_REVIEWS)

def add_review(place: str, ramp: int, washroom: int, elevator: int, space: int, note: str):
    reviews = get_reviews()
    new_id = max((r["id"] for r in reviews), default=0) + 1
    reviews.append({
        "id": new_id,
        "place": place,
        "ramp": ramp,
        "washroom": washroom,
        "elevator": elevator,
        "space": space,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d"),
    })
    _write(REVIEWS_F, reviews)

def delete_review(rid: int):
    reviews = [r for r in get_reviews() if r["id"] != rid]
    _write(REVIEWS_F, reviews)

# ── Chat history ──────────────────────────────────────────────────────────────
def get_chat():
    return _read(CHAT_F, [])

def save_chat(history: list):
    _write(CHAT_F, history)
