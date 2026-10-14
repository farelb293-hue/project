from colorama import init, Fore
from datetime import date

init(autoreset=True)

nama = input("Masukkan nama Anda: ")
print(Fore.GREEN + f"Halo, {nama}!")

while True:
    try:
        tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
        tahun_ini = date.today().year
        if tahun_lahir > tahun_ini or tahun_lahir < 1900:
            print(Fore.YELLOW + "Tahun lahir tidak masuk akal, coba lagi.")
            continue
        usia = tahun_ini - tahun_lahir
        print(Fore.CYAN + f"Perkiraan usia Anda adalah {usia} tahun.")
        break
    except ValueError:
        print(Fore.RED + "Input harus berupa angka, coba lagi.")