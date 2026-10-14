# Praktikum Python

Program sederhana untuk menyapa pengguna dan menghitung perkiraan usia berdasarkan tahun lahir.

## Fitur
- Meminta input nama pengguna
- Menampilkan salam
- Meminta input tahun lahir
- Validasi input tahun lahir
- Menampilkan perkiraan usia dengan pesan error saat input tidak valid

## Persiapan
1. Buat virtual environment:
   ```bash
   python -m venv venv
   ```
2. Aktifkan environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan program
```bash
python halo.py
```

## Contoh output
```text
Masukkan nama Anda: Budi
Halo, Budi!
Masukkan tahun lahir Anda: 2000
Perkiraan usia Anda adalah 26 tahun.
```

Catatan: program ini sudah siap dijalankan di lingkungan virtual Python dengan dependency yang tercatat di `requirements.txt`.
