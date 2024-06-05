import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length, use_letters, use_digits, use_symbols):
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("No character sets selected for password generation.")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")

        # Length
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=10)
        self.length_var = tk.IntVar(value=12)
        self.length_entry = tk.Entry(root, textvariable=self.length_var)
        self.length_entry.pack(pady=10)

        # Character set options
        self.letters_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        self.letters_check = tk.Checkbutton(root, text="Include Letters", variable=self.letters_var)
        self.digits_check = tk.Checkbutton(root, text="Include Numbers", variable=self.digits_var)
        self.symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=self.symbols_var)

        self.letters_check.pack(pady=5)
        self.digits_check.pack(pady=5)
        self.symbols_check.pack(pady=5)

        # Generate button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Display password
        self.password_entry = tk.Entry(root, font=('Helvetica', 14), justify='center')
        self.password_entry.pack(pady=10)
        
        # Copy to clipboard button
        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)

    def generate_password(self):
        try:
            length = self.length_var.get()
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")

            use_letters = self.letters_var.get()
            use_digits = self.digits_var.get()
            use_symbols = self.symbols_var.get()

            if not (use_letters or use_digits or use_symbols):
                raise ValueError("At least one character type must be selected.")

            password = generate_password(length, use_letters, use_digits, use_symbols)
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
