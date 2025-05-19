import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
import time
from playsound import playsound
import pyttsx3

# Init TTS
engine = pyttsx3.init()

# Fungsi alarm checker
def alarm_checker(alarm_list):
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        for alarm in alarm_list:
            if alarm["time"] == now:
                msg = f"🔔⏰ Saatnya {alarm['kegiatan']}!"
                print(msg)
                playsound("403007__inspectorj__ui-confirmation-alert-a2.wav")  # pastikan file ada di folder
                engine.say(f"Waktunya {alarm['kegiatan']}")
                engine.runAndWait()
                messagebox.showinfo("ALARM", msg)
                alarm_list.remove(alarm)
        time.sleep(1)

# Fungsi set alarm
def set_alarm():
    kegiatan = entry_kegiatan.get()
    jam = spin_jam.get()
    menit = spin_menit.get()
    detik = spin_detik.get()
    waktu = f"{jam.zfill(2)}:{menit.zfill(2)}:{detik.zfill(2)}"

    alarm = {"kegiatan": kegiatan, "time": waktu}
    alarm_list.append(alarm)

    listbox_alarm.insert(tk.END, f"{waktu} - {kegiatan}")
    entry_kegiatan.delete(0, tk.END)

# Setup GUI
root = tk.Tk()
root.title("Reminder Alarm GUI")
root.geometry("350x300")

alarm_list = []

# Input Form
tk.Label(root, text="Nama Kegiatan").pack()
entry_kegiatan = tk.Entry(root, width=30)
entry_kegiatan.pack()

frame_waktu = tk.Frame(root)
frame_waktu.pack(pady=5)

tk.Label(frame_waktu, text="Jam").grid(row=0, column=0)
spin_jam = tk.Spinbox(frame_waktu, from_=0, to=23, width=5)
spin_jam.grid(row=1, column=0)

tk.Label(frame_waktu, text="Menit").grid(row=0, column=1)
spin_menit = tk.Spinbox(frame_waktu, from_=0, to=59, width=5)
spin_menit.grid(row=1, column=1)

tk.Label(frame_waktu, text="Detik").grid(row=0, column=2)
spin_detik = tk.Spinbox(frame_waktu, from_=0, to=59, width=5)
spin_detik.grid(row=1, column=2)

tk.Button(root, text="Set Alarm", command=set_alarm).pack(pady=10)

# List Alarm
tk.Label(root, text="Daftar Alarm").pack()
listbox_alarm = tk.Listbox(root, width=45)
listbox_alarm.pack(pady=5)

# Jalankan alarm checker di thread terpisah
threading.Thread(target=alarm_checker, args=(alarm_list,), daemon=True).start()

# Jalankan GUI
root.mainloop()
