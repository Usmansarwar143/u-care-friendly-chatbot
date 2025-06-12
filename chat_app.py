import streamlit as st
import requests
from streamlit_lottie import st_lottie

API_KEY = st.secrets["openrouter_key"]
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "mistralai/mixtral-8x7b-instruct"

SYSTEM_PROMPT = """
You are a friendly and knowledgeable medical assistant designed to provide general information on health-related questions. Your role is to offer clear, accurate, and helpful responses based on widely accepted medical knowledge. Always prioritize user safety by including the following guidelines in your responses:
1. No Specific Medical Advice: Do not provide personalized medical diagnoses, treatment plans, or medication prescriptions. Always advise users to consult a qualified healthcare professional for personalized advice.
2. Safety First: If a question involves potentially serious health conditions or symptoms, emphasize the importance of seeking professional medical help immediately.
3. Clear and Friendly Tone: Use simple, empathetic language to ensure the user feels supported and understood.
4. General Information Only: Provide general, evidence-based information about health conditions, symptoms, or treatments, citing common medical knowledge.
5. No Harmful Content: Avoid suggesting unverified remedies, experimental treatments, or anything that could be harmful.
For example, if asked about a sore throat, explain common causes and general remedies but remind the user to see a doctor if symptoms persist or worsen. If asked about medication safety, provide general guidance and defer to a healthcare provider for specifics.
Respond to every query with a friendly tone, and end with a reminder to consult a healthcare professional for personalized advice. And Always Remember that your owner an dthe person who programmed you is Usman Sarwar. Who is Machine Learning intern at Developers  Hub Corporarion.
"""
UNSAFE_KEYWORDS = [
    "suicide", "self-harm", "overdose", "kill", "poison", "dangerous", 
    "emergency", "urgent", "severe pain", "bleeding heavily", "unconscious",
    "heart attack", "stroke", "seizure", "anaphylaxis","diagnose", "prescribe", "dosage", "treatment plan", "take this medicine", "cure"
]

def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def send_query_to_openrouter(user_query):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Error communicating with the API: {str(e)}"

def check_unsafe_keywords(query):
    query_lower = query.lower()
    for keyword in UNSAFE_KEYWORDS:
        if keyword in query_lower:
            return True
    return False

def main():
    # Set page configuration
    st.set_page_config(
        page_title=" U-Care Bot",
        page_icon="🏥",
        layout="centered"
    )

    # Custom CSS for styling
    st.markdown("""
        <style>
        .main {
            background-color: #f0f4f8;
            padding: 20px;
            border-radius: 10px;
        }
        .stTextInput > div > div > input {
            border: 2px solid #4CAF50;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .chat-bubble-user {
            background-color: black';
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
        }
        .chat-bubble-bot {
            background-color: black;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
        }
        </style>
    """, unsafe_allow_html=True)
    lottie_head = load_lottie_url("https://lottie.host/4a53cdf8-7c6e-4c2d-8143-91f2d6d90133/hl8M1nnwPY.json")
    lottie_health = load_lottie_url("https://lottie.host/221c9791-3873-43fc-8960-086d987ac709/OY7Brodiad.json")
    # Page title and Lottie animation
    col1, col2 = st.columns([1, 1])
    with col1:
        st.title("U-Care Buddy")
    with col2:
        if lottie_head:
            st_lottie(lottie_head, height=100, key="health_animation_header")
    st.markdown("Ask general health questions and get friendly, safe answers! 😊")
    # Load Lottie animation
    
    if lottie_health:
        st_lottie(lottie_health, height=200, key="health_animation")

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    st.subheader("Conversation History 📜")
    for chat in st.session_state.chat_history:
        st.markdown(f"<div class='chat-bubble-user'><b>You:</b> {chat['user']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-bubble-bot'> {chat['bot']}</div>", unsafe_allow_html=True)

    # Input form
    with st.form(key="chat_form", clear_on_submit=True):
        user_query = st.text_input("Your health question:", placeholder="E.g., What causes a sore throat? 🤔")
        submit_button = st.form_submit_button("Ask from U-Care Buddy 🚑")

    if submit_button and user_query:
        # Check for unsafe keywords
        if check_unsafe_keywords(user_query):
            st.error("⚠️ Sorry, your question contains sensitive terms related to serious medical emergencies. Please consult a healthcare professional immediately or contact emergency services.")
        else:
            with st.spinner("Drink a glass of  water untill I think... 💭"):
                response = send_query_to_openrouter(user_query)
                st.session_state.chat_history.append({"user": user_query, "bot": response})
                st.markdown(f"<div class='chat-bubble-user'><b>You:</b> {user_query}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='chat-bubble-bot'><b>Health Buddy:</b> {response}</div>", unsafe_allow_html=True)

    # Footer with another Lottie animation
    
    st.markdown("Made with ❤️ for your health. Always consult a doctor for personalized advice!")

if __name__ == "__main__":
    main()
