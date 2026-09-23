import tkinter as tk
from tkinter import messagebox

# Vernam Cipher (simple XOR-based)
def vernam_encrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

database = {}

# Encryption key
key = "mysecretkey"

# GUI setup
root = tk.Tk()
root.title("Register")

tk.Label(root, text="Enter Username").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Enter Password").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Confirm Password").grid(row=2, column=0, padx=10, pady=10)

entry_user = tk.Entry(root)
entry_pass = tk.Entry(root, show="*")
entry_confirm = tk.Entry(root, show="*")

entry_user.grid(row=0, column=1)
entry_pass.grid(row=1, column=1)
entry_confirm.grid(row=2, column=1)

def refresh():
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)
    entry_confirm.delete(0, tk.END)

def store():
    username = entry_user.get()
    password = entry_pass.get()
    confirm = entry_confirm.get()

    if not username or not password or not confirm:
        messagebox.showwarning("Warning", "All fields are required!")
        return
    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match!")
        return
    if len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long!")
        return

    encrypted_pass = vernam_encrypt(password, key)
    database[username] = encrypted_pass
    messagebox.showinfo("Success", "Registration Successful!")
    refresh()

def login_screen():
    login = tk.Toplevel(root)
    login.title("Login")

    tk.Label(login, text="Enter Username").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(login, text="Enter Password").grid(row=1, column=0, padx=10, pady=10)

    user_entry = tk.Entry(login)
    pass_entry = tk.Entry(login, show="*")
    user_entry.grid(row=0, column=1)
    pass_entry.grid(row=1, column=1)

    def check_login():
        username = user_entry.get()
        password = pass_entry.get()
        encrypted_input = vernam_encrypt(password, key)

        if username in database and database[username] == encrypted_input:
            messagebox.showinfo("Login", "Login Successful!")
        else:
            messagebox.showerror("Login", "Login Failed!")

    tk.Button(login, text="OK", command=check_login).grid(row=2, column=1, pady=10)
    tk.Button(login, text="Back", command=login.destroy).grid(row=2, column=0, pady=10)

tk.Button(root, text="Refresh", command=refresh).grid(row=3, column=0, pady=10)
tk.Button(root, text="Store", command=store).grid(row=3, column=1, pady=10)
tk.Button(root, text="Login", command=login_screen).grid(row=3, column=2, pady=10)

root.mainloop()
