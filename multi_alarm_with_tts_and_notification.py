import time
from datetime import datetime
from playsound import playsound
import pyttsx3
from plyer import notification

# Inisialisasi TTS
tts = pyttsx3.init()

# Input jumlah alarm
jumlah_alarm = int(input("Berapa alarm yang mau disetel? "))
daftar_alarm = []

# Input detail tiap alarm
for i in range(jumlah_alarm):
    print(f"\nAlarm ke-{i + 1}")
    kegiatan = input("  Nama kegiatan: ")
    jam = int(input("  Jam (24 jam): "))
    menit = int(input("  Menit: "))
    detik = int(input("  Detik: "))
    daftar_alarm.append({
        "kegiatan": kegiatan,
        "jam": jam,
        "menit": menit,
        "detik": detik
    })

print("\n⏳ Semua alarm telah disetel. Menunggu...\n")

# Looping untuk cek alarm
while daftar_alarm:
    sekarang = datetime.now()
    jam_now, menit_now, detik_now = sekarang.hour, sekarang.minute, sekarang.second

    for alarm in daftar_alarm[:]:
        if (jam_now == alarm["jam"] and
            menit_now == alarm["menit"] and
            detik_now == alarm["detik"]):
            
            pesan = f"Sekarang pukul {jam_now:02d}:{menit_now:02d}, saatnya {alarm['kegiatan']}"
            print(f"🔔 {pesan}")
            playsound('403007__inspectorj__ui-confirmation-alert-a2.wav')  # Ganti dengan file audio yang kamu punya
            tts.say(pesan)
            tts.runAndWait()

            # Notifikasi pop-up
            notification.notify(
                title="⏰ Alarm",
                message=pesan,
                timeout=10  # Detik tampil
            )

            daftar_alarm.remove(alarm)

    time.sleep(1)
