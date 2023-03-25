import tkinter as tk
from tkinter import messagebox
import random
import string
import json


class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("400x400")

        # Widgets
        self.website_label = tk.Label(self.master, text="Website:")
        self.website_label.pack()

        self.website_entry = tk.Entry(self.master)
        self.website_entry.pack()

        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.generate_password_button = tk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_password_button.pack()

        self.add_button = tk.Button(self.master, text="Add", command=self.add_password)
        self.add_button.pack()

        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_entries)
        self.clear_button.pack()

        # Load passwords from file
        try:
            with open("passwords.json", "r") as f:
                self.passwords = json.load(f)
        except FileNotFoundError:
            self.passwords = {}

    def generate_password(self):
        password = "".join(random.choices(string.ascii_letters + string.digits, k=12))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def add_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if website == "" or username == "" or password == "":
            messagebox.showerror("Error", "All fields are required.")
        else:
            self.passwords[website] = {
                "username": username,
                "password": password
            }
            messagebox.showinfo("Success", f"Password for {website} added successfully.")

            self.clear_entries()

            # Save passwords to file
            with open("passwords.json", "w") as f:
                json.dump(self.passwords, f)

    def clear_entries(self):
        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    password_manager = PasswordManager(root)
    root.mainloop()
