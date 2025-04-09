# 🔐 Password Strength Meter (Streamlit)

A simple and interactive Password Strength Meter built with Python and Streamlit.

This app checks your password's strength based on common security rules and provides instant feedback & suggestions for improvement.

---

## 🚀 Features

### ✅ Password Strength Rules:
- Minimum 8 characters
- Must include both Uppercase & Lowercase letters
- At least 1 digit (0-9)
- At least 1 special character (!@#$%^&*)
- Rejects common & weak passwords (like `password123`)

---

### 🏆 Strength Rating:
| Score | Strength | Message |
|-------|-----------|---------|
| 1-2   | Weak      | ❌ Improve using suggestions |
| 3     | Moderate  | ⚠️ Add more security features |
| 4     | Strong    | ✅ Good to go! |

---

### 🎲 Extra Features:
- Strong Password Generator (Random & Secure)
- Instant Feedback
- Beautiful Streamlit UI
- Copy/Paste Friendly Output

---

## 💻 How to Run Locally

1. Clone the repo
```bash
git clone https://github.com/your-username/password-strength-meter.git
cd password-strength-meter

---

## Install Steamlit and Run Commands:

pip install streamlit

streamlit run app.py