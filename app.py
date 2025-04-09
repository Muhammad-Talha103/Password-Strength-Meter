import streamlit as st
import re
import random


# Password Strength Checker
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    blacklist = ['password', '123456', 'password123', 'admin', 'qwerty']
    if password.lower() in blacklist:
        feedback.append("❌ This password is too common and easily guessable!")
        score = 1  # Force weak

    return score, feedback


# Strong Password Generator
def generate_strong_password():
    length = 12
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%^&*"
    all_chars = upper + lower + digits + special

    password = random.choice(upper) + random.choice(lower) + random.choice(digits) + random.choice(special)
    password += ''.join(random.choices(all_chars, k=length - 4))
    password = ''.join(random.sample(password, len(password)))

    return password


# Streamlit UI
st.title("🔐 Password Strength Meter")
st.subheader("Password Strength Criteria")
st.write("A strong password should:")

st.write("1. ✅Be at least 8 characters long.")
st.write("2. ✅Include both uppercase and lowercase letters.")

st.write("3. ✅Contain at least one number (0-9).")

st.write("4. ✅Have at least one special character (!@#$%^&*).")

password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)

    st.subheader("Feedback:")
    for f in feedback:
        st.write(f)

    st.subheader("Strength Rating:")

    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider improving it.")
    else:
        st.error("❌ Weak Password - Improve using suggestions above.")

    if st.button("Generate Strong Password"):
        strong_password = generate_strong_password()
        st.info(f"🔑 Suggested Strong Password: {strong_password}")
        st.text_input("Copy the generated password:", value=strong_password, type="password", key="generated_password")
        st.success("Copy and use it securely!")
    st.markdown("---")
    st.subheader("Password Tips:")
    st.write("1. Use at least 12 characters.")
    st.write("2. Mix uppercase, lowercase, numbers, and special characters.")
    st.write("3. Avoid common words and sequences.")
    st.write("4. Use a password manager to store complex passwords.")
    st.write("5. Enable two-factor authentication (2FA) where possible.")
    st.write("6. Change passwords regularly.")
    st.write("7. Don't reuse passwords across different accounts.")
    st.write("8. Be cautious of phishing attempts.")
    st.write("9. Use passphrases for better memorability.")
    st.write("10. Regularly update your security questions and answers.")
   


