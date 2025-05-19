import time
from datetime import datetime

# Input dari user
kegiatan = input("Masukkan nama kegiatan: ")
jam_target = int(input("Masukkan jam (24 jam): "))
menit_target = int(input("Masukkan menit: "))

print(f"\n⏳ Alarm disetel ke {jam_target:02d}:{menit_target:02d} untuk kegiatan: {kegiatan}. Menunggu...\n")

# Loop sampai waktu sekarang sama dengan target
while True:
    sekarang = datetime.now()
    jam = sekarang.hour
    menit = sekarang.minute

    if jam == jam_target and menit == menit_target:
        print(f"🔔⏰ ALARM: Sekarang pukul {jam:02d}:{menit:02d} - Saatnya {kegiatan}!")
        break

    time.sleep(10)  # cek tiap 10 detik
