import tkinter as tk
import re
import nltk
from nltk.corpus import words
from tkinter import messagebox

# Optional: Download 'words' if not already downloaded
try:
    english_words = set(words.words())
except LookupError:
    nltk.download('words')
    english_words = set(words.words())

# Strength checking function
def check_password_strength(password):
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"\d", password):
        strength += 1
    else:
        suggestions.append("Include numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Use special characters.")

    if password.lower() in english_words:
        suggestions.append("Avoid using dictionary words.")

    return strength, suggestions

# Callback
def evaluate_password():
    password = entry.get()
    strength, suggestions = check_password_strength(password)

    if strength <= 2:
        result.config(text="Weak ", fg="red")
    elif strength == 3 or strength == 4:
        result.config(text="Moderate ", fg="orange")
    else:
        result.config(text="Strong ", fg="green")

    suggestion_box.config(state="normal")
    suggestion_box.delete("1.0", tk.END)
    for s in suggestions:
        suggestion_box.insert(tk.END, f"- {s}\n")
    suggestion_box.config(state="disabled")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("400x300")
root.configure(bg="#f2f2f2")

title = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), bg="#f2f2f2")
title.pack(pady=10)

entry = tk.Entry(root, width=30, show="*", font=("Arial", 12), bd=2, relief="groove")
entry.pack(pady=10)

check_btn = tk.Button(root, text="Check Strength", command=evaluate_password, bg="#4caf50", fg="white", font=("Arial", 12), padx=10, pady=5)
check_btn.pack(pady=5)

result = tk.Label(root, text="", font=("Arial", 14), bg="#f2f2f2")
result.pack(pady=5)

tk.Label(root, text="Suggestions:", font=("Arial", 12, "bold"), bg="#f2f2f2").pack(pady=5)

suggestion_box = tk.Text(root, width=45, height=6, font=("Arial", 10), wrap="word", state="disabled", bg="#e6e6e6")
suggestion_box.pack(pady=5)

root.mainloop()
