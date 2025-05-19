import time
import threading
from datetime import datetime
from playsound import playsound
import pyttsx3
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk alarm pop-up
def tampilkan_popup(kegiatan):
    root = tk.Tk()
    root.withdraw()  # Sembunyikan window utama
    messagebox.showinfo("ALARM!", f"Sekarang waktunya {kegiatan}!")
    root.destroy()

# Fungsi untuk bunyikan alarm + suara TTS + popup
def bunyikan_alarm(kegiatan):
    print(f"🔔⏰ ALARM: Saatnya {kegiatan}!")
    threading.Thread(target=playsound, args=("403007__inspectorj__ui-confirmation-alert-a2.wav",), daemon=True).start()
    
    engine = pyttsx3.init()
    engine.say(f"Hey! Sekarang waktunya {kegiatan}")
    engine.runAndWait()

    tampilkan_popup(kegiatan)

# Fungsi utama untuk memantau waktu
def setel_alarm(jam_target, menit_target, detik_target, kegiatan):
    while True:
        sekarang = datetime.now()
        if (sekarang.hour == jam_target and
            sekarang.minute == menit_target and
            sekarang.second == detik_target):
            bunyikan_alarm(kegiatan)
            break
        time.sleep(1)

# Input dari user
jumlah = int(input("Berapa alarm yang mau disetel? "))

for i in range(jumlah):
    print(f"\nAlarm ke-{i+1}")
    kegiatan = input("  Nama kegiatan: ")
    jam = int(input("  Jam (24 jam): "))
    menit = int(input("  Menit: "))
    detik = int(input("  Detik: "))

    threading.Thread(target=setel_alarm, args=(jam, menit, detik, kegiatan), daemon=True).start()

print("\n⏳ Semua alarm telah disetel. Menunggu...\n")

# Supaya program tetap hidup
while threading.active_count() > 1:
    time.sleep(1)
