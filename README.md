# Praktikum Python: Salam dan Perkiraan Usia

Program Python sederhana yang menyapa pengguna dan memperkirakan usia berdasarkan tahun lahir. Program memvalidasi input agar tahun lahir harus berupa angka dan berada dalam rentang yang masuk akal.

## Fitur

- Meminta nama pengguna dan menampilkan salam.
- Meminta tahun lahir dan menghitung perkiraan usia dari tahun saat ini.
- Menangani input non-angka dengan `try/except`.
- Menolak tahun lahir sebelum 1900 atau setelah tahun saat ini.
- Menggunakan [`colorama`](https://pypi.org/project/colorama/) untuk memberi warna pada output terminal.

## Struktur Proyek

```text
praktikum-python/
├── halo.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Persyaratan

- Python 3.8 atau lebih baru
- `pip`

## Instalasi dan Menjalankan Program

Buka terminal di folder proyek, lalu buat virtual environment:

```powershell
python -m venv venv
```

Aktifkan virtual environment di Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Pasang dependency dan jalankan program:

```powershell
python -m pip install -r requirements.txt
python .\halo.py
```

Jika tidak ingin mengaktifkan virtual environment, jalankan dengan:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe .\halo.py
```

## Contoh Penggunaan

```text
Masukkan nama Anda: Budi
Halo, Budi!
Masukkan tahun lahir Anda: 2000
Perkiraan usia Anda adalah 26 tahun.
```

Usia pada contoh dihitung dari tahun berjalan, sehingga hasilnya dapat berubah dari waktu ke waktu.

## Verifikasi Tugas

Untuk menampilkan riwayat commit dan dependency yang terpasang:

```powershell
git log --oneline
python -m pip list
```

Ambil tangkapan layar hasil kedua perintah tersebut jika diminta sebagai bukti pengumpulan.
