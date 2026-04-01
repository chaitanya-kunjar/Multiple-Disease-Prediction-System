import google.generativeai as genai

# Configure API
genai.configure(api_key="AIzaSyDm51GtYMuGU-Q_qiFaYuy5aaiNyyrWxJA")

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

def get_chatbot_response(user_input, prediction_summary, chat_history):

    system_prompt = f"""
    You are an AI healthcare assistant.

    Patient details:
    {prediction_summary}

    Rules:
    - Explain in simple language
    - Give practical lifestyle suggestions
    - Do NOT give strict medical diagnosis
    - Always suggest consulting a doctor if risk is high
    """

    # Build conversation context
    full_prompt = system_prompt + "\n\n"

    for role, msg in chat_history:
        if role == "user":
            full_prompt += f"User: {msg}\n"
        else:
            full_prompt += f"AI: {msg}\n"

    full_prompt += f"User: {user_input}\nAI:"

    response = model.generate_content(full_prompt)

    return response.text