# 🧠 AI Bias Detection Live Chatbot

A Responsible AI project that detects potential bias in user input and demonstrates safe, controlled chatbot responses for sensitive topics.

---

## 🔍 Problem Statement
Modern chatbots can unintentionally generate biased or unsafe responses, especially when dealing with sensitive identity-related topics such as religion, gender, or community.

This project addresses that issue by introducing a **bias-aware decision layer** that evaluates user input before generating responses.

---

## 🛠️ Solution Overview
Instead of unrestricted text generation, the system:
- Analyzes user input for bias and sentiment
- Detects sensitive identity-related topics
- Applies rule-based guardrails to ensure safe and neutral responses

This approach aligns with **Responsible AI** principles.

---

## 🧱 Architecture
![Architecture Diagram](architecture_diagram.png)

---

## ⚙️ Tech Stack
- Python
- Streamlit
- TextBlob (Sentiment Analysis)
- Pandas

---

## 🚀 Features
- Live chatbot interface
- Real-time bias detection
- Sensitive topic identification
- Safe response templates
- Transparent bias explanation

---

## 🧪 Example
**Input:**
> I am a sikh but I am more inclined towards hinduism

**Output:**
- Sensitive topic detected
- Neutral, respectful response
- Bias analysis with explanation

---

## 🌍 Deployment
The application is deployed using **Streamlit Community Cloud** and is accessible via a public URL.

---

## 📌 Use Cases
- HR screening tools
- Ethics & compliance training
- AI fairness demonstrations
- Educational projects on Responsible AI

---

## 📄 Disclaimer
This system does not generate opinions.  
It evaluates language patterns and demonstrates how AI responses should be constrained for ethical safety.
