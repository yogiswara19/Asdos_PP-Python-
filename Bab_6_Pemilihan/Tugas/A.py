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
print("""1. Yong Ma
2. Cosmos
0. EXIT""")
menu = int(input("\nPilih brand: "))
print()

# Show menu
if menu == 1:
    print("""1. Yong Ma SMC 8033
2. Yong Ma SMC 7047
3. Yong Ma MC 504 Jumbo\n""")
elif menu == 2:
    print("""1. Cosmos CRJ 6601 B
2. Cosmos CRJ 9303
3. Cosmos CRJ 5908 \n""")
elif menu == 0:
    input("Program keluar...")
    exit()
else:
    input("Brand tidak tersedia!")
    exit()

# input pembelian
jenis = int(input("Masukkan tipe rice cooker\t: "))
if jenis not in [1,2,3]:
    input("[!] Tipe tersebut tidak ada dalam daftar")
    exit()
jumlah = int(input("Masukkan jumlah rice cooker\t: "))
if jumlah < 1:
    input("[!] Pembelian rice cooker tidak boleh nol atau minus")
    exit()
member = input("Masukkan jenis member (Gold/Silver/None): ")

# Perhitungan
match menu:
    case 1:
        if jenis == 1:
            total = jumlah * 700000
            bonus = "Mendapatkan bonus 1 centong nasi"
            jenis_nama = "Yong Ma SMC 8033"
            
            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>8:
                total = total-400000
        
        elif jenis == 2:
            total = jumlah * 1400000
            bonus = "Mendapatkan bonus 2 centong nasi dan 1 inner pot"
            jenis_nama = "Yong Ma SMC 7047"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>8:
                total = total-900000

        elif jenis == 3:
            total = jumlah * 1900000
            bonus = "Mendapatkan bonus 3 centong nasi, 2 inner pot, dan garansi 6 bulan"
            jenis_nama = "Yong Ma MC 504 Jumbo"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>8:
                total = total-1300000

    case 2:
        if jenis == 1:
            total = jumlah * 600000
            bonus = "Mendapatkan bonus 2 centong nasi"
            jenis_nama = "Cosmos CRJ 6601 B"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>8:
                total = total-300000

        elif jenis == 2:
            total = jumlah * 1200000
            bonus = "Mendapatkan bonus 3 centong nasi dan 2 inner pot"
            jenis_nama = "Cosmos CRJ 9303"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>8:
                total = total-900000

        elif jenis == 3:
            total = jumlah * 1600000
            bonus = "Mendapatkan bonus 4 centong nasi, 3 inner pot, dan garansi 1 tahun"
            jenis_nama = "Cosmos CRJ 5908"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>8:
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