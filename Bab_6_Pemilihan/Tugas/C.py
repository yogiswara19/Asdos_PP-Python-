nama = "yogi"
npm = "11087"

import os
os.system("cls")
# Login
user = input("Masukkan Username: ")
pasw = input("Masukkan Password: ")

if user == nama and pasw == npm:
    print(f"\nLogin berhasil. Welcome, {user}!")
else:
    print("\n!! Username dan Password salah !!")
    input("!! Login Gagal !!")
    exit()

# Menu
print("\n===== TOKO MAS KARNA =====")
print("""1. Mito
2. Sharp
0. EXIT""")
menu = int(input("\nPilih brand: "))
print()

# Show menu
if menu == 1:
    print("""1. Mito MO-20
2. Mito MO-999
3. Mito MO-120\n""")
elif menu == 2:
    print("""1. Sharp EO-18L-W
2. Sharp EO-38BK
3. Sharp EO-28L-PK \n""")
elif menu == 0:
    input("Program keluar...")
    exit()
else:
    input("Brand tidak tersedia!")
    exit()

# input pembelian
jenis = int(input("Masukkan tipe oven\t: "))
if jenis not in [1,2,3]:
    input("[!] Tipe tersebut tidak ada dalam daftar")
    exit()
jumlah = int(input("Masukkan jumlah oven\t: "))
if jumlah < 1:
    input("[!] Pembelian oven tidak boleh nol atau minus")
    exit()
member = input("Masukkan jenis member (Gold/Silver/None): ")

# Perhitungan
match menu:
    case 1:
        if jenis == 1:
            total = jumlah * 691000
            bonus = "Mendapatkan bonus 1 loyang oven"
            jenis_nama = "Mito MO-20"
            
            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>7:
                total = total-310000

        elif jenis == 2:
            total = jumlah * 1910000
            bonus = "Mendapatkan bonus 2 loyang oven dan 1 rak pemanggang"
            jenis_nama = "Mito MO-999"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>7:
                total = total-820000

        elif jenis == 3:
            total = jumlah * 3390000
            bonus = "Mendapatkan bonus 3 loyang oven, 2 rak pemanggang, dan garansi 12 bulan"
            jenis_nama = "Mito MO-120"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>7:
                total = total-1640000

    case 2:
        if jenis == 1:
            total = jumlah * 788000
            bonus = "Mendapatkan bonus 2 loyang oven"
            jenis_nama = "Sharp EO-18L-W"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95

            # cek jumlah
            if jumlah>7:
                total = total-420000

        elif jenis == 2:
            total = jumlah * 1290000
            bonus = "Mendapatkan bonus 2 loyang oven dan 2 rak pemanggang"
            jenis_nama = "Sharp EO-38BK"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95

            # cek jumlah
            if jumlah>7:
                total = total-970000

        elif jenis == 3:
            total = jumlah * 2320000
            bonus = "Mendapatkan bonus 3 loyang oven, 3 rak pemanggang, dan garansi 9 bulan"
            jenis_nama = "Sharp EO-28L-PK"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95

            # cek jumlah
            if jumlah>7:
                total = total-1100000

    case 0:
        input("Program selesai. . .")
        exit()

    case _:
        input(f"Tidak ada pilihan {menu} dalam menu")
        exit()

# output
print("\n===== Data Pembelian =====")
print(f"""Nama\t\t: {user}
Tipe\t\t: {jenis_nama}
Jumlah\t\t: {jumlah} unit
Total Harga\t: Rp {total}""")
print("-"*40)
print(bonus)
input()