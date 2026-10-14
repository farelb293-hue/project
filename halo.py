from datetime import date

nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}!")

while True:
    try:
        tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
        tahun_ini = date.today().year
        if tahun_lahir > tahun_ini or tahun_lahir < 1900:
            print("Tahun lahir tidak masuk akal, coba lagi.")
            continue
        usia = tahun_ini - tahun_lahir
        print(f"Perkiraan usia Anda adalah {usia} tahun.")
        break
    except ValueError:
        print("Input harus berupa angka, coba lagi.")