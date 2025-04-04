import streamlit as st

# Title of the app
st.title("Meters to Centimeters Converter")

# Ask the user to enter a value in meters
meters = st.number_input("Enter value in meters:")

# Convert meters to centimeters
centimeters = meters * 100

# Show the result
st.write(f"{meters} meters is equal to {centimeters} centimeters.")

