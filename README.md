# OpenAI_chatbot
Generative OpenAi chatbot for booking appointment

# 🤖 GPT Appointment Booking Bot

A conversational assistant powered by OpenAI GPT that helps users schedule appointments by checking real-time availability and booking preferred time slots. Built with Python, it simulates a functional booking workflow — perfect for demos, prototyping, or GPT function calling practice.

---

## 🧠 Features

✅ Conversational booking experience  
✅ GPT function calling to trigger slot booking  
✅ Mock time slot database with real-time availability  
✅ Data validation and user detail collection  
✅ Supports smart prompts like _"tomorrow"_ or _"the day after tomorrow"_

---

## 🗂 Project Structure

```bash
.
├── appointment_bot.py      # GPT conversation + function calling logic
├── timeslots.py            # Mock DB of time slots (pre-filled for demo)
└── README.md               # You're here!
```

---

## 🚀 How It Works

1. Starts a CLI chatbot powered by `gpt-3.5-turbo-1106`.
2. Collects all required details from the user:
   - Name
   - Email
   - Phone
   - Company
   - Date (`YYYY-MM-DD`)
   - Time Slot (`HH:MM - HH:MM`)
3. GPT triggers the booking function only when all required fields are present.
4. Confirms the booking and stores the information in memory.

---

## 📦 Setup

> Make sure you have Python 3.8+ and OpenAI SDK installed.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/gpt-appointment-bot.git
cd gpt-appointment-bot
```

### 2. Install Requirements
```bash
pip install openai
```

### 3. Add Your OpenAI API Key
Edit `appointment_bot.py` and replace the API key:

```python
openai.api_key = "sk-your-api-key"
```

### 4. Run the Bot
```bash
python appointment_bot.py
```

---

## 📅 Dummy Time Slots (Mock DB)

The system uses a static in-memory database defined in `timeslots.py`, using a structure like:

```python
TIMESLOT_DB = {
    "2025-05-25": [
        {"time": "09:00 - 10:30", "status": "available", "booked_by": None},
        ...
    ]
}
```

> All slots are automatically updated as **booked** once confirmed.

---

## 💡 Example Conversation

```txt
🤖: Hello! I can help you schedule an appointment.
You: I want to book a meeting tomorrow at 9am.
🤖: Great! Can I have your name, email, phone, and company?
...
🤖: ✅ Your appointment is confirmed on 2025-05-26 at 09:00 - 10:30.
```

---

## 🛠️ Tech Stack

- Python 3.8+
- OpenAI GPT (function calling)
- CLI-based chatbot interface (command line interface)

---

## 🙌 Credits

Created with ❤️ by Shubham Bhoilkar (https://github.com/shubhambhoilkar)  
Inspired by real-world scheduling challenges, prototyped using OpenAI's function calling.

---

## 📄 License

MIT License — use freely, modify smartly.
