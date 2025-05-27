import openai
from timeslots import TIMESLOT_DB  # 👈 our mock DB
from datetime import datetime

openai.api_key = "sk-proj-OpenAI_API_KEY"

# 👇 Helper to find a slot and mark it
def book_slot(date, preferred_time, user_info):
    if date not in TIMESLOT_DB:
        return False, "❌ Invalid date. Please choose a weekday within the next 2 weeks."

    for slot in TIMESLOT_DB[date]:
        print("DEBUG: checking slot:", slot)
        if slot["time"] == preferred_time:
            if slot["status"] == "available":
                slot["status"] = "booked"
                slot["booked_by"] = user_info
                return True, f"✅ Your appointment is confirmed on {date} at {preferred_time}."
            else:
                return False, "❌ Slot unavailable. Please try a different time."

    return False, "❌ Time not found for the selected date."

# GPT system prompt
system_message = {
    "role": "system",
    "content": (
        "You are a helpful assistant that books appointments. "
        "Collect: name, email, phone, company, date (YYYY-MM-DD), and preferred_time (HH:MM - HH:MM). "
        "If user wants to change something, update and confirm. "
        "If user say's the keywords like 'tomorrow', 'the day after tomorrow' then ask them the actual date."
        "Use 'book_appointment' function only when all fields are ready."
    )
}

functions = [
    {
        "name": "book_appointment",
        "description": "Book a meeting if slot is available.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "email": {"type": "string"},
                "phone": {"type": "string"},
                "company": {"type": "string"},
                "date": {"type": "string", "description": "Format: YYYY-MM-DD"},
                "preferred_time": {"type": "string", "description": "Format: HH:MM - HH:MM"},
            },
            "required": ["name", "email", "phone", "company", "date", "preferred_time"]
        }
    }
]

def chat():
    print("The Chatbot is loading, please wait for a while!...")
    messages = [system_message]
    user_data = {}

    print("🤖 GPT Appointment Bot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
            functions=functions,
            function_call="auto"
        )

        msg = response["choices"][0]["message"]

        if msg.get("function_call"):
            args = eval(msg["function_call"]["arguments"])
            user_data.update(args)

            required = ["name", "email", "phone", "company", "date", "preferred_time"]
            missing = [k for k in required if k not in user_data]

            if not missing:
                success, reply = book_slot(
                    user_data["date"],
                    user_data["preferred_time"],
                    user_data
                )
                print("Bot:", reply)
                if success:
                    break
            else:
                messages.append({
                    "role": "function",
                    "name": "book_appointment",
                    "content": f"Missing: {', '.join(missing)}"
                })
        else:
            print("Bot:", msg["content"])
            messages.append(msg)

if __name__ == "__main__":
    chat()
