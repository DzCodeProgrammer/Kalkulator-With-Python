import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import math

# === RIWAYAT PERHITUNGAN ===
history_list = []

# === FUNGSI UNTUK MENAMPILKAN HISTORY ===
def tampilkan_history():
    history_window = Toplevel(root)
    history_window.title("Riwayat Perhitungan")
    history_window.geometry("400x400")
    history_window.config(bg="#121212")

    # Label
    label = Label(history_window, text="Riwayat Perhitungan", font=("Poppins", 14, "bold"), 
                  bg="#121212", fg="#00ffb3")
    label.pack(pady=10)

    # Text widget dengan scrollbar
    history_text = scrolledtext.ScrolledText(history_window, font=("Poppins", 11), 
                                             bg="#1e1e1e", fg="#00ffb3", bd=0, relief="flat")
    history_text.pack(fill=BOTH, expand=True, padx=10, pady=10)
    history_text.config(state=NORMAL)

    for item in reversed(history_list):
        history_text.insert(END, item + "\n")

    history_text.config(state=DISABLED)

    # Tombol Clear History
    btn_clear = Button(history_window, text="Hapus Riwayat", font=("Poppins", 10, "bold"),
                       bg="#ff3b30", fg="white", relief="flat", 
                       command=lambda: clear_history(history_text, history_window))
    btn_clear.pack(pady=5, padx=10, fill=X)

def clear_history(history_text, window):
    global history_list
    history_list = []
    history_text.config(state=NORMAL)
    history_text.delete(1.0, END)
    history_text.config(state=DISABLED)

# === FUNGSI UNTUK KONVERSI OPERATOR ===
def konversi_operator(expr):
    """Konversi operator visual ke operator Python"""
    expr = expr.replace("×", "*")
    expr = expr.replace("÷", "/")
    return expr

# === FUNGSI TOMBOL ===
def klik(tombol):
    current = entry_var.get()

    if tombol == "=":
        try:
            expr = konversi_operator(current)
            hasil = eval(expr)
            hasil_str = str(hasil)
            entry_var.set(hasil_str)
            # Tambah ke history
            history_list.append(f"{current} = {hasil_str}")
        except:
            entry_var.set("Error")
    elif tombol == "C":
        entry_var.set("")
    elif tombol in ["sin", "cos", "tan"]:
        try:
            expr = konversi_operator(current)
            nilai = eval(expr) if current else 0
            # Konversi dari derajat ke radian
            radian = math.radians(nilai)
            if tombol == "sin":
                hasil = math.sin(radian)
            elif tombol == "cos":
                hasil = math.cos(radian)
            elif tombol == "tan":
                hasil = math.tan(radian)
            entry_var.set(str(hasil))
        except:
            entry_var.set("Error")
    elif tombol == "DEL":
        entry_var.set(current[:-1])
    else:
        entry_var.set(current + tombol)

# === WINDOW UTAMA ===
root = Tk()
root.title("Kalkulator ⚡")
root.geometry("400x600")
root.resizable(False, False)
root.config(bg="#121212")

# === VARIABEL UNTUK ENTRY ===
entry_var = StringVar()

# === FRAME HEADER ===
header_frame = Frame(root, bg="#121212")
header_frame.pack(fill=X, padx=10, pady=(10, 0))

title_label = Label(header_frame, text="⚡", font=("Poppins", 16, "bold"),
                    bg="#121212", fg="#00ffb3")
title_label.pack(side=LEFT)

history_btn = Button(header_frame, text="📋 History", font=("Poppins", 9, "bold"),
                     bg="#00bcd4", fg="white", relief="flat", command=tampilkan_history)
history_btn.pack(side=RIGHT, padx=5)

# === LAYAR TAMPILAN ===
entry = Entry(
    root,
    textvariable=entry_var,
    font=("Poppins", 26, "bold"),
    bg="#1e1e1e",
    fg="#00ffb3",
    bd=0,
    justify=RIGHT,
    insertbackground="#00ffb3"
)
entry.pack(fill=BOTH, ipadx=8, ipady=20, padx=15, pady=(15, 0))

# === FRAME TOMBOL ===
tombol_frame = Frame(root, bg="#121212")
tombol_frame.pack(pady=20)

# === DAFTAR TOMBOL ===
tombol_list = [
    ["C", "(", ")", "DEL"],
    ["sin", "cos", "tan", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

# === WARNA TOMBOL ===
warna_angka = "#2c2c2c"
warna_operator = "#00bcd4"
warna_clear = "#ff3b30"
warna_trigon = "#ff6b6b"

# === BUAT TOMBOL SECARA DINAMIS ===
for i, baris in enumerate(tombol_list):
    for j, tombol in enumerate(baris):
        if tombol == "":
            continue

        warna_bg = warna_angka
        warna_fg = "white"

        if tombol in ["÷", "×", "-", "+", "=", "(", ")"]:
            warna_bg = "#263238"
            warna_fg = "#00bcd4"
        elif tombol == "C":
            warna_bg = warna_clear
            warna_fg = "white"
        elif tombol in ["sin", "cos", "tan"]:
            warna_bg = warna_trigon
            warna_fg = "white"
        elif tombol == "DEL":
            warna_bg = "#ff9800"
            warna_fg = "white"

        btn = Button(
            tombol_frame,
            text=tombol,
            font=("Poppins", 14, "bold"),
            bg=warna_bg,
            fg=warna_fg,
            activebackground="#00ffb3",
            activeforeground="#121212",
            relief="flat",
            width=5,
            height=2,
            bd=0,
            command=lambda t=tombol: klik(t)
        )
        btn.grid(row=i, column=j, padx=6, pady=6, sticky="nsew")

# === ATUR RASIO GRID ===
for i in range(6):
    tombol_frame.rowconfigure(i, weight=1)
for j in range(4):
    tombol_frame.columnconfigure(j, weight=1)

# === JALANKAN APLIKASI ===
root.mainloop()
