import time
from datetime import datetime
from playsound import playsound

# Ambil jumlah alarm dari user
jumlah_alarm = int(input("Berapa alarm yang mau disetel? "))

# List untuk simpan semua alarm
daftar_alarm = []

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
        'aktif': True  # Supaya alarm cuma bunyi sekali
    })

print("\n⏳ Semua alarm telah disetel. Menunggu...\n")

# Loop utama untuk cek semua alarm
while any(alarm['aktif'] for alarm in daftar_alarm):
    sekarang = datetime.now()
    jam = sekarang.hour
    menit = sekarang.minute
    detik = sekarang.second

    for alarm in daftar_alarm:
        if alarm['aktif'] and jam == alarm['jam'] and menit == alarm['menit'] and detik == alarm['detik']:
            print(f"🔔⏰ ALARM: Sekarang pukul {jam:02d}:{menit:02d}:{detik:02d} - Saatnya {alarm['kegiatan']}!")
            playsound('403007__inspectorj__ui-confirmation-alert-a2.wav')
            alarm['aktif'] = False  # Matikan setelah bunyi

    time.sleep(0.5)
