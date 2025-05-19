import time
from datetime import datetime
from playsound import playsound

# Input dari user
kegiatan = input("Masukkan nama kegiatan: ")
jam_target = int(input("Masukkan jam (24 jam): "))
menit_target = int(input("Masukkan menit: "))
detik_target = int(input("Masukkan detik: "))

print(f"\n⏳ Alarm disetel ke {jam_target:02d}:{menit_target:02d}:{detik_target:02d} untuk kegiatan: {kegiatan}. Menunggu...\n")

# Loop sampai waktu sekarang sama dengan target
while True:
    sekarang = datetime.now()
    jam = sekarang.hour
    menit = sekarang.minute
    detik = sekarang.second

    if jam == jam_target and menit == menit_target and detik == detik_target:
        print(f"🔔⏰ ALARM: Sekarang pukul {jam:02d}:{menit:02d}:{detik:02d} - Saatnya {kegiatan}!")
        playsound('403007__inspectorj__ui-confirmation-alert-a2.wav')  # Pastikan file ini ada di folder yang sama
        break

    time.sleep(0.5)  # cek tiap 0.5 detik
