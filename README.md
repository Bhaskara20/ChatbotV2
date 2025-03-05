# ChatbotV2

Chatbot sederhana yang menggunakan Phi-3.5 untuk percakapan dan Pollinations AI untuk generate gambar.

## Fitur

- Percakapan menggunakan model Phi-3.5
- Generate gambar menggunakan Pollinations AI
- Interface chat yang responsif dan modern

## Cara Penggunaan

1. Buka aplikasi di browser
2. Untuk percakapan biasa, langsung ketik pesan Anda
3. Untuk generate gambar, ketik "gambar [deskripsi]" (contoh: "gambar kucing bermain bola")

## Teknologi yang Digunakan

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- AI: Microsoft Phi-3.5 dan Pollinations AI

## Pengembangan Lokal

1. Clone repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variable HUGGINGFACE_API_TOKEN:
   ```bash
   # PowerShell
   $env:HUGGINGFACE_API_TOKEN='your_token_here'
   
   # Command Prompt
   set HUGGINGFACE_API_TOKEN=your_token_here
   ```
4. Jalankan server Flask:
   ```bash
   python test.py
   ```
5. Buka browser dan akses `http://localhost:8000`

