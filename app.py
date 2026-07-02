import random
import string
import streamlit as st


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits

    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_numbers = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True

        if new_char in special:
            has_special = True

        meet_criteria = True

        if numbers:
            meet_criteria = has_numbers

        if special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd


st.title("🔐 Password Generator")

length = st.slider("Password Length", 8, 30, 12)

numbers = st.checkbox("Include Numbers", value=True)

special = st.checkbox("Include Special Characters", value=True)

if st.button("Generate Password"):
    password = generate_password(length, numbers, special)
    st.success(password)