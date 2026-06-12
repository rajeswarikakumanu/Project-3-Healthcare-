import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Healthcare Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Healthcare Chatbot")

st.markdown(
    "Ask health-related questions, symptom checks, appointment help, and general healthcare FAQs."
)

# ===================================
# Initialize Chat History
# ===================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ===================================
# Predefined Responses
# ===================================

def chatbot_response(user_input):

    text = user_input.lower()

    # Symptom Checker

    if "fever" in text:
        return """
Possible Causes:
• Viral Infection
• Flu
• Common Cold

Recommendation:
• Drink plenty of water
• Take adequate rest
• Consult a doctor if fever persists
"""

    elif "cough" in text:
        return """
Possible Causes:
• Cold
• Allergy
• Respiratory Infection

Recommendation:
• Stay hydrated
• Avoid cold drinks
• Seek medical advice if symptoms worsen
"""

    elif "headache" in text:
        return """
Possible Causes:
• Stress
• Migraine
• Dehydration

Recommendation:
• Rest in a quiet room
• Drink water
• Consult a doctor for persistent headaches
"""

    elif "chest pain" in text:
        return """
Warning:
Chest pain may indicate a serious condition.

Recommendation:
• Seek immediate medical attention
• Contact emergency services if severe
"""

    elif "diabetes" in text:
        return """
Diabetes Management Tips:
• Monitor blood sugar regularly
• Follow a healthy diet
• Exercise daily
• Take prescribed medications
"""

    elif "appointment" in text:
        return """
Appointment Process:
1. Go to Appointments Module
2. Select Doctor
3. Choose Date and Time Slot
4. Confirm Booking
"""

    elif "medicine" in text:
        return """
Medicine Reminder:
• Take medicines on schedule
• Follow doctor prescriptions
• Do not skip doses
"""

    elif "hello" in text or "hi" in text:
        return """
Hello! 👋

How can I assist you today?

• Symptom Check
• Appointment Help
• Disease Information
• Medication Guidance
"""

    else:
        return """
I can help with:

• Symptom Checking
• Appointment Information
• Healthcare FAQs
• Medication Guidance

Please ask a healthcare-related question.
"""

# ===================================
# Chat Display
# ===================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ===================================
# User Input
# ===================================

prompt = st.chat_input(
    "Type your question here..."
)

if prompt:

    # User Message

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot Response

    response = chatbot_response(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)

# ===================================
# Sidebar Information
# ===================================

with st.sidebar:

    st.header("📌 Chatbot Features")

    st.write("✔ Symptom Checker")
    st.write("✔ Appointment Guidance")
    st.write("✔ Disease Information")
    st.write("✔ Medication Advice")
    st.write("✔ Healthcare FAQs")

    st.divider()

    st.header("⏰ Current Time")

    st.write(
        datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
    )

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []
        st.rerun()

# ===================================
# Disclaimer
# ===================================

st.divider()

st.warning(
    """
    Disclaimer:
    This chatbot provides educational information only.
    It is not a substitute for professional medical advice,
    diagnosis, or treatment.
    """
)