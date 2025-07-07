import tkinter as tk
from tkinter import messagebox
import subprocess

# Hardcoded credentials for demo
VALID_EMAIL = "admin@email.com"
VALID_PASSWORD = "admin123"

def open_main_menu(user_email):
    subprocess.Popen(["python", "main_menu.py", user_email])

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teman SIBI - Login")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        # Logo (placeholder)
        self.logo = tk.Canvas(root, width=100, height=100, bg="white", highlightthickness=0)
        self.logo.create_rectangle(10, 10, 90, 90, fill="#2563eb", outline="")
        self.logo.create_text(50, 50, text="👐", font=("Arial", 40))
        self.logo.pack(pady=(40, 10))

        # Title
        self.title = tk.Label(root, text="Teman SIBI", font=("Arial", 20, "bold"), fg="#2563eb", bg="white")
        self.title.pack(pady=(0, 20))

        # Email
        self.email_label = tk.Label(root, text="Email", font=("Arial", 10), bg="white", anchor="w")
        self.email_label.pack(fill="x", padx=40)
        self.email_entry = tk.Entry(root, font=("Arial", 12), bd=1, relief="solid")
        self.email_entry.pack(fill="x", padx=40, pady=(0, 15), ipady=6)
        self.email_entry.insert(0, "Masukkan Email")
        self.email_entry.bind("<FocusIn>", self.clear_email_placeholder)

        # Password
        self.password_label = tk.Label(root, text="Password", font=("Arial", 10), bg="white", anchor="w")
        self.password_label.pack(fill="x", padx=40)
        self.password_entry = tk.Entry(root, font=("Arial", 12), bd=1, relief="solid", show="*")
        self.password_entry.pack(fill="x", padx=40, pady=(0, 20), ipady=6)
        self.password_entry.insert(0, "Masukkan Password")
        self.password_entry.bind("<FocusIn>", self.clear_password_placeholder)

        # Login Button
        self.login_btn = tk.Button(root, text="Login", font=("Arial", 12), bg="#2563eb", fg="white", bd=0, height=2, command=self.login)
        self.login_btn.pack(fill="x", padx=40, pady=(0, 15))

        # Register
        self.register_label = tk.Label(root, text="Belum punya akun? ", font=("Arial", 10), bg="white")
        self.register_label.pack(side="left", padx=(60,0), pady=(0,10))
        self.register_link = tk.Label(root, text="Daftar", font=("Arial", 10, "underline"), fg="#2563eb", bg="white", cursor="hand2")
        self.register_link.pack(side="left", pady=(0,10))
        self.register_link.bind("<Button-1>", self.show_register_message)

    def clear_email_placeholder(self, event):
        if self.email_entry.get() == "Masukkan Email":
            self.email_entry.delete(0, tk.END)

    def clear_password_placeholder(self, event):
        if self.password_entry.get() == "Masukkan Password":
            self.password_entry.delete(0, tk.END)
            self.password_entry.config(show="*")

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if email == VALID_EMAIL and password == VALID_PASSWORD:
            messagebox.showinfo("Login Berhasil", "Selamat datang di Teman SIBI!")
            self.root.destroy()
            open_main_menu(email)
        else:
            messagebox.showerror("Login Gagal", "Email atau password salah.")

    def show_register_message(self, event):
        messagebox.showinfo("Daftar", "Fitur daftar belum tersedia.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop() 