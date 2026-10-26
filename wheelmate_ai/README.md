# ♿ WheelMate AI — Smart Wheelchair Companion

> A modern, AI-inspired companion platform for wheelchair users — built as a 2nd Semester Engineering Mini Project.

---

## 🌟 Project Overview

WheelMate AI helps wheelchair users improve comfort, stay organised, and discover accessible places — all through a clean, futuristic software interface.

| Module | Description |
|---|---|
| 🏠 Dashboard | Welcome screen with stats, suggestions, and profile overview |
| ⚙️ Customization Assistant | Rule-based AI recommends cushions, wheels, supports |
| 🔔 Smart Reminders | Hydration, posture, medicine, and maintenance reminders |
| ♿ Accessibility Ratings | Rate and review public places for wheelchair access |
| 👤 Profile | Editable user + wheelchair profile |
| 🤖 AI Chatbot | Conversational assistant with predefined smart responses |
| 🚀 Future Scope | Roadmap of planned AI and IoT enhancements |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| Frontend | Streamlit |
| Storage | Local JSON files |
| Fonts | Google Fonts (Syne, DM Sans) |
| AI Logic | Rule-based (no ML models) |

---

## 🚀 How to Run

### 1. Clone / Download the project

```bash
git clone https://github.com/your-username/wheelmate-ai.git
cd wheelmate-ai
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

### 5. Open in browser

Streamlit will automatically open **http://localhost:8501** in your browser.

---

## 📁 File Structure

```
wheelmate_ai/
│
├── app.py                    # Main entry point — page routing + global CSS
│
├── modules/
│   ├── __init__.py           # Package marker
│   ├── data_manager.py       # JSON read/write helpers for all data
│   ├── dashboard.py          # Dashboard homepage
│   ├── customization.py      # Wheelchair customization assistant
│   ├── reminders.py          # Smart reminder system
│   ├── accessibility.py      # Accessibility rating system
│   ├── profile.py            # User profile page
│   ├── chatbot.py            # AI assistant chatbot
│   └── future_scope.py       # Future scope presentation page
│
├── data/                     # Auto-created on first run
│   ├── profile.json          # User profile
│   ├── reminders.json        # Reminder list
│   ├── reviews.json          # Accessibility reviews
│   └── chat_history.json     # Chatbot history
│
├── requirements.txt
└── README.md
```

---

## 💡 Features at a Glance

- **Rule-based AI recommendations** — no paid APIs or ML models needed
- **Fully offline** — all data stored locally in JSON files
- **Dark mode UI** — futuristic dark theme with teal accent
- **Sample data pre-loaded** — looks populated from day one
- **Modular codebase** — easy to understand and extend

---

## 📸 Pages

| Page | What It Does |
|---|---|
| Dashboard | Overview of reminders, AI tips, and wheelchair profile |
| Customization | Enter wheelchair details → get personalised recommendations |
| Reminders | Add / complete / delete health and maintenance reminders |
| Accessibility | Review public places for ramp, washroom, elevator, space |
| Profile | Edit your name, wheelchair type, usage, and preferences |
| AI Assistant | Chat with the rule-based assistant about comfort and care |
| Future Scope | Present the project roadmap to faculty |

---

## 👨‍💻 Team / Credits

Built as a **2nd Semester Mini Project** for the B.E. / B.Tech Computer Science programme.

> WheelMate AI — Empowering mobility through technology.
