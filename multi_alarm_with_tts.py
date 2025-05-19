import time
from datetime import datetime
from playsound import playsound
import pyttsx3

# Inisialisasi TTS
tts = pyttsx3.init()
tts.setProperty('rate', 170)  # Kecepatan bicara

# Input jumlah alarm
jumlah_alarm = int(input("Berapa alarm yang mau disetel? "))
daftar_alarm = []

# Input setiap alarm
for i in range(jumlah_alarm):
    print(f"\nAlarm ke-{i+1}")
    kegiatan = input("  Nama kegiatan: ")
    jam = int(input("  Jam (24 jam): "))
    menit = int(input("  Menit: "))
    detik = int(input("  Detik: "))

    daftar_alarm.append({
        'jam': jam,
        'menit': menit,
        'detik': detik,
        'kegiatan': kegiatan,
        'aktif': True
    })

print("\n⏳ Semua alarm telah disetel. Menunggu...\n")

# Cek semua alarm
while any(alarm['aktif'] for alarm in daftar_alarm):
    sekarang = datetime.now()
    jam = sekarang.hour
    menit = sekarang.minute
    detik = sekarang.second

    for alarm in daftar_alarm:
        if alarm['aktif'] and jam == alarm['jam'] and menit == alarm['menit'] and detik == alarm['detik']:
            pesan = f"Sekarang pukul {jam:02d}:{menit:02d}, saatnya {alarm['kegiatan']}"
            print(f"🔔⏰ ALARM: {pesan}")
            playsound('403007__inspectorj__ui-confirmation-alert-a2.wav')
            tts.say(pesan)
            tts.runAndWait()
            alarm['aktif'] = False

    time.sleep(0.5)
