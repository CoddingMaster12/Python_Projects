import streamlit as st
import random

st.title("🌱 Growth Mindset Challenge")

challenges = [
    "💪 Try something new that scares you a little today.",
    "📚 Learn from a mistake you made recently.",
    "🧠 Replace 'I can't' with 'I can't YET'.",
    "🎯 Set one small goal for the day and complete it.",
    "🤝 Give someone positive feedback.",
    "✍️ Write down what you're proud of learning this week.",
    "🔁 Keep trying even if it's hard — progress takes time!"
]

if st.button("🎲 Give me a challenge!"):
    st.session_state.challenge = random.choice(challenges)

if "challenge" in st.session_state:
    st.markdown(f"### 🌟 Your Challenge:\n\n{st.session_state.challenge}")
