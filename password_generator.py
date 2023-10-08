import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip  # Required for copying to clipboard

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    try:
        password_length = int(length_entry.get())
        if password_length < 1:
            messagebox.showerror("Error", "Password length should be greater than 0.")
            return

        generated_password = generate_password(password_length)
        generated_password_var.set(generated_password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer for the password length.")

def copy_to_clipboard():
    generated_password = generated_password_var.get()
    if generated_password:
        pyperclip.copy(generated_password)
        messagebox.showinfo("Success", "Password copied to clipboard!")

def reset_button_click():
    length_entry.delete(0, tk.END)
    generated_password_var.set("")

# Create the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x300")  # Set the window size (width x height)
app.resizable(False, False)  # Disable window resizing

# Center the window on the screen
window_width = app.winfo_reqwidth()
window_height = app.winfo_reqheight()
position_right = int(app.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(app.winfo_screenheight() / 2 - window_height / 2)
app.geometry("+{}+{}".format(position_right, position_down))

# Styling options
app.configure(bg="#ffffff")  # Set the background color to white

title_label = tk.Label(app, text="Password Generator", font=("Arial", 18,"bold"), fg="#0000ff")
title_label.pack(pady=15)

length_label = tk.Label(app, text="Enter the desired password length:", font=("Arial", 12), fg="#Ef9060")
length_label.pack()

length_entry = tk.Entry(app, width=30, font=("Arial", 12))
length_entry.pack(pady=5)

generate_button = tk.Button(app, text="Generate Password", command=generate_button_click, font=("Arial", 12), bg="#00ff00", fg="#ffffff")
generate_button.pack(pady=10)

generated_password_var = tk.StringVar()
generated_password_label = tk.Label(app, textvariable=generated_password_var, font=("Arial", 12), wraplength=300, bg="#f0f0f0")
generated_password_label.pack(pady=10)

copy_button = tk.Button(app, text="Copy Password", command=copy_to_clipboard, font=("Arial", 12), bg="#00ffff")
copy_button.pack(pady=5)

reset_button = tk.Button(app, text="Reset", command=reset_button_click, font=("Arial", 12), bg="#ffff00")
reset_button.pack(pady=5)

app.mainloop()
