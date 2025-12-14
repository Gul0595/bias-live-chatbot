import streamlit as st
import pandas as pd
from textblob import TextBlob

st.set_page_config(page_title="AI Bias Detection Chatbot", layout="wide")
st.title("🧠 AI Bias Detection Live Chatbot")
st.caption("Live chatbot with bias & sentiment analysis (Responsible AI)")

# Load dataset (optional – future use)
df = pd.read_csv("bias_analysis_results.csv")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Type your message here...")

# ---------------------------
# Bias analysis function
# ---------------------------
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
        reason = "Negative sentiment or generalized language detected."
    else:
        flag = "✅ Neutral"
        reason = "No strong bias indicators detected."

    return sentiment, length, flag, reason

# ---------------------------
# Sensitive topic detection
# ---------------------------
def is_sensitive(text):
    keywords = [
        "religion", "sikh", "hindu", "muslim",
        "christian", "caste", "gender", "race"
    ]
    return any(k in text.lower() for k in keywords)

# ---------------------------
# Main logic
# ---------------------------
if user_input:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    st.chat_message("user").write(user_input)

    # Bias analysis ON USER INPUT
    sentiment, length, flag, reason = analyze_bias(user_input)

    # Controlled system response
    if is_sensitive(user_input):
        ai_response = (
            "This statement relates to personal beliefs or identity. "
            "Such topics should be discussed with respect and neutrality."
        )
    elif flag.startswith("⚠️"):
        ai_response = (
            "This statement may contain biased or generalized language. "
            "Please consider rephrasing it in a more neutral way."
        )
    else:
        ai_response = (
            "No strong bias indicators detected. "
            "The statement appears neutral."
        )

    bot_reply = f"""
🤖 **System Response**  
{ai_response}

---
🔍 **Bias Analysis**
- Sentiment Score: {sentiment:.2f}
- Text Length: {length} words
- Bias Status: {flag}
- Explanation: {reason}

💡 *Highly emotional or generalized language may indicate bias.*
"""

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
    st.chat_message("assistant").write(bot_reply)

# Sidebar
st.sidebar.header("📊 Quick Insights")
st.sidebar.write("Live chatbot + bias detection")
st.sidebar.write("Use-case: HR | Education | Ethics Training")
