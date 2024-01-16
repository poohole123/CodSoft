import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(length_var.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        result_var.set("Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

root = tk.Tk()
root.geometry("400x250")
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, padx=10, pady=10)
length_var.set(12)

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

uppercase_checkbox = ttk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0, padx=10, pady=5)
lowercase_checkbox = ttk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=1, column=1, padx=10, pady=5)
digits_checkbox = ttk.Checkbutton(root, text="Digits", variable=digits_var)
digits_checkbox.grid(row=2, column=0, padx=10, pady=5)
symbols_checkbox = ttk.Checkbutton(root, text="Symbols", variable=symbols_var)
symbols_checkbox.grid(row=2, column=1, padx=10, pady=5)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=('Arial', 12), wraplength=300)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
