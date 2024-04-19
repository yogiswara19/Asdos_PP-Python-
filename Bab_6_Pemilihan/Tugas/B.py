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
print("""1. Oxone
2. Philips
0. EXIT""")
menu = int(input("\nPilih brand: "))
print()

# Show menu
if menu == 1:
    print("""1. Oxone OX-277
2. Oxone OX-198
3. Oxone OX-199\n""")
elif menu == 2:
    print("""1. Philips HD-9200
2. Philips HD-9870 XL
3. Philips HD-9723 \n""")
elif menu == 0:
    input("Program keluar...")
    exit()
else:
    input("Brand tidak tersedia!")
    exit()

# input pembelian
jenis = int(input("Masukkan tipe air fryer\t\t: "))
if jenis not in [1,2,3]:
    input("[!] Tipe tersebut tidak ada dalam daftar")
    exit()
jumlah = int(input("Masukkan jumlah air fryer\t: "))
if jumlah < 1:
    input("[!] Pembelian air fryer tidak boleh nol atau minus")
    exit()
member = input("Masukkan jenis member (Gold/Silver/None): ")

# Perhitungan
match menu:
    case 1:
        if jenis == 1:
            total = jumlah * 1580000
            bonus = "Mendapatkan bonus 2 pack air fryer paper"
            jenis_nama = "Oxone OX-277"
            
            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>6:
                total = total-510000
        
        elif jenis == 2:
            total = jumlah * 1730000
            bonus = "Mendapatkan bonus 4 pack air fryer paper dan 1 tray"
            jenis_nama = "Oxone OX-198"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>6:
                total = total-880000

        elif jenis == 3:
            total = jumlah * 2600000
            bonus = "Mendapatkan bonus 5 pack air fryer paper, 2 tray dan garansi 1 tahun"
            jenis_nama = "Oxone OX-199"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>6:
                total = total-1190000

    case 2:
        if jenis == 1:
            total = jumlah * 1370000
            bonus = "Mendapatkan bonus 3 pack air fryer paper"
            jenis_nama = "Philips HD-9200"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>6:
                total = total-840000

        elif jenis == 2:
            total = jumlah * 2480000
            bonus = "Mendapatkan bonus 4 pack air fryer paper dan 2 tray"
            jenis_nama = "Philips HD-9870 XL"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>6:
                total = total-1220000

        elif jenis == 3:
            total = jumlah * 3190000
            bonus = "Mendapatkan bonus 6 pack air fryer paper, 2 tray dan garansi 2 tahun"
            jenis_nama = "Philips HD-9723"

            # cek member
            if member.lower() == "gold":
                total = total * 0.9
            elif member.lower() == "silver":
                total = total * 0.95
            
            # cek jumlah
            if jumlah>6:
                total = total-1990000
    
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