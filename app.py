import streamlit as st
import pandas as pd
from textblob import TextBlob
from transformers import pipeline

st.set_page_config(page_title="AI Bias Detection Chatbot", layout="wide")
st.title("🧠 AI Bias Detection Live Chatbot")

st.caption("Real-time chatbot with bias & sentiment analysis")

# Load dataset (optional – future use)
df = pd.read_csv("bias_analysis_results.csv")

# Load AI model
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="distilgpt2")

generator = load_model()

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Type your message here...")

def analyze_bias(text):
    sentiment = TextBlob(text).sentiment.polarity
    length = len(text.split())

    bias_keywords = [
        "all", "always", "never", "everyone", "people from",
        "lazy", "stupid", "bad", "inferior", "better than"
    ]

    keyword_flag = any(word in text.lower() for word in bias_keywords)

    if sentiment < -0.3 or keyword_flag:
        flag = "⚠️ Potential Bias Detected"
        reason = "Negative sentiment and/or generalized language detected."
    else:
        flag = "✅ Neutral"
        reason = "No strong bias indicators detected."

    return sentiment, length, flag, reason

if user_input:
    # User message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # AI response
    ai_response = generator(
        user_input,
        max_length=80,
        num_return_sequences=1
    )[0]["generated_text"]

    # Bias analysis
    sentiment, length, flag, reason = analyze_bias(ai_response)

    bot_reply = f"""
🤖 **Chatbot Response**  
{ai_response}

---
🔍 **Bias Analysis**
- Sentiment Score: {sentiment:.2f}
- Response Length: {length} words
- Bias Status: {flag}
- Explanation: {reason}

💡 *Highly emotional or generalized language may indicate bias.*
"""


    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.chat_message("assistant").write(bot_reply)

# Sidebar dashboard
st.sidebar.header("📊 Quick Insights")
st.sidebar.write("Live chatbot + bias detection")
st.sidebar.write("Use-case: HR | Education | Ethics Training")