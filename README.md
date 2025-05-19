# 🔔 Reminder Alarm App (Python)

Ini adalah proyek alarm pengingat harian yang dibuat dengan Python. Tersedia berbagai versi: mulai dari yang berbasis terminal (CLI), pakai suara, sampai GUI lengkap dengan form input dan TTS.

## 📦 Fitur

- ✅ Alarm sederhana lewat terminal
- 🔊 Bunyi alarm otomatis
- 🗣️ Suara TTS (Text to Speech)
- 🖼️ Tampilan GUI (Popup dan Form Input)

## 🛠️ Instalasi

1. Clone repository:
   ```bash
   git clone https://github.com/namamu/reminder_alarm.git
   cd reminder_alarm
   ```

2. (Opsional) Buat virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Cara Menjalankan

### 1. Versi CLI
```bash
python alarm_cli.py
```

### 2. Versi dengan Suara
```bash
python alarm_with_sound.py
```

### 3. Versi Multi Alarm + TTS
```bash
python multi_alarm_with_tts.py
```

### 4. Versi GUI Popup
```bash
python alarm_with_gui_popup.py
```

### 5. Versi Full GUI dengan Form
```bash
python alarm_gui_form.py
```

## 📝 Catatan

- File suara alarm (`alarm.mp3`) harus ada di folder `sound/`.
- Untuk TTS, menggunakan library `pyttsx3` (offline).
- Pastikan Python 3.9+ sudah terpasang.

---

## 💡 Inspirasi & Pembelajaran

Proyek ini dikembangkan sebagai latihan belajar Python harian, mulai dari dasar hingga GUI & AI. Kamu juga bisa kembangkan fitur seperti:
- Sinkronisasi dengan kalender
- Notifikasi WhatsApp/Telegram
- Alarm berulang

---

## 📩 Kontribusi

Pull request dan ide pengembangan sangat diterima. Yuk sama-sama belajar bareng!

---

## 🧑‍💻 Author

Irawan — [LinkedIn](https://www.linkedin.com/in/tri-irawan-262a17294/)
