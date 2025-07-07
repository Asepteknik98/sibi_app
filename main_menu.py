import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

class MainMenuApp:
    def __init__(self, root, user_email):
        self.root = root
        self.root.title("Teman SIBI - Menu Utama")
        self.root.geometry("370x600")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        username = user_email.split("@")[0].capitalize()

        # Header
        header_frame = tk.Frame(root, bg="white")
        header_frame.pack(fill="x", pady=(25, 0), padx=20)
        icon = tk.Canvas(header_frame, width=40, height=40, bg="white", highlightthickness=0)
        icon.create_oval(2, 2, 38, 38, fill="#2563eb", outline="")
        icon.create_text(20, 20, text="H", font=("Arial", 18, "bold"), fill="white")
        icon.pack(side="left")
        hi_label = tk.Label(header_frame, text=f"Hi, {username}", font=("Arial", 16, "bold"), bg="white")
        hi_label.pack(side="left", padx=(10,0))
        profile_icon = tk.Label(header_frame, text="464", font=("Arial", 20), bg="white")
        profile_icon.pack(side="right")

        # Fitur label
        fitur_label = tk.Label(root, text="Fitur", font=("Arial", 14, "bold"), bg="white")
        fitur_label.pack(anchor="w", padx=30, pady=(25, 10))

        # Menu Buttons
        self.create_menu_button(
            icon_text="F590",  # Raised hand emoji
            title="Mulai Deteksi Isyarat SIBI",
            desc="Detekai Gerakan",
            command=self.start_detection
        )
        self.create_menu_button(
            icon_text="F4DA",  # Books emoji
            title="Perpustakaan SIBI",
            desc="Pustaka Gerakan",
            command=lambda: messagebox.showinfo("Perpustakaan SIBI", "Fitur belum tersedia.")
        )
        self.create_menu_button(
            icon_text="F4C4",  # Page facing up emoji
            title="Informasi Tunewicara",
            desc="Artikel dan informasi",
            command=lambda: messagebox.showinfo("Informasi Tunewicara", "Fitur belum tersedia.")
        )

        # Bottom Navigation (dummy)
        nav_frame = tk.Frame(root, bg="white")
        nav_frame.pack(side="bottom", fill="x", pady=10)
        home_icon = tk.Label(nav_frame, text="F3E0", font=("Arial", 18), fg="#2563eb", bg="white")
        home_icon.pack(side="left", expand=True)
        home_label = tk.Label(nav_frame, text="Home", font=("Arial", 10), fg="#2563eb", bg="white")
        home_label.pack(side="left", expand=True)
        profile_icon2 = tk.Label(nav_frame, text="F464", font=("Arial", 18), fg="#222", bg="white")
        profile_icon2.pack(side="right", expand=True)
        profile_label = tk.Label(nav_frame, text="Profil", font=("Arial", 10), fg="#222", bg="white")
        profile_label.pack(side="right", expand=True)

    def create_menu_button(self, icon_text, title, desc, command):
        frame = tk.Frame(self.root, bg="#2563eb", bd=0, relief="ridge")
        frame.pack(padx=25, pady=10, fill="x")
        icon = tk.Label(frame, text=icon_text, font=("Arial", 28), bg="#2563eb", fg="#fff")
        icon.pack(side="left", padx=15)
        text_frame = tk.Frame(frame, bg="#2563eb")
        text_frame.pack(side="left", fill="y", expand=True)
        title_label = tk.Label(text_frame, text=title, font=("Arial", 13, "bold"), bg="#2563eb", fg="#fff")
        title_label.pack(anchor="w")
        desc_label = tk.Label(text_frame, text=desc, font=("Arial", 10), bg="#2563eb", fg="#e0e7ff")
        desc_label.pack(anchor="w")
        frame.bind("<Button-1>", lambda e: command())
        icon.bind("<Button-1>", lambda e: command())
        text_frame.bind("<Button-1>", lambda e: command())
        title_label.bind("<Button-1>", lambda e: command())
        desc_label.bind("<Button-1>", lambda e: command())

    def start_detection(self):
        subprocess.Popen(["python", "inference_classifier.py"])
        messagebox.showinfo("Deteksi Isyarat SIBI", "Aplikasi deteksi isyarat telah dijalankan.")

if __name__ == "__main__":
    # Ambil email user dari argumen command line jika ada
    if len(sys.argv) > 1:
        user_email = sys.argv[1]
    else:
        user_email = "admin@email.com"  # default/demo
    root = tk.Tk()
    app = MainMenuApp(root, user_email)
    root.mainloop() 