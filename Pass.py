import streamlit as st

st.title("🔐 Beginner Password Generator")

# User input for characters and length
chars = st.text_input("Enter characters to use (e.g. abc123!@#)")
length = st.slider("Password length", 8, 12, 20)

# Generate password
if st.button("Generate Password"):
    if chars:
        password = ""
        for i in range(length):
            password += chars[i % len(chars)]
        st.code(password)
    else:
        st.warning("Please enter some characters.")
