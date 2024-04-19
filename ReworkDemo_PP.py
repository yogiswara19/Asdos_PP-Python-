## Demo 4 - Operator
# 1
# usia = int(input("Masukkan usia\t\t: "))
# print(f"Usia saat ini adalah\t: {usia}")

# 2
# bil1 = int(input("Masukkan bilangan pertama\t: "))
# bil2 = int(input("Masukkan bilangan kedua\t\t: "))
# bil3 = int(input("Masukkan bilangan ketiga\t: "))
# bil4 = int(input("Masukkan bilangan keempat\t: "))
# bil5 = int(input("Masukkan bilangan keelima\t: "))
# hasil = bil1 + bil2 + bil3 + bil4 + bil5
# print(f"Hasil penjumlahan dari 5 bilangan = {hasil}")


## Demo 5 - Pemilihan
# 1
# hasil = 0
# makanan = ""
# print("-"*41)
# print("-"*14,"DAFTAR MENU","-"*14)
# print("-"*41)
# print("""
# 1. Nasi Goreng\t\t: Rp 15.000
# 2. Spageti\t\t: Rp 17.000
# 3. Pizza\t\t: Rp 55.000
# 4. Kentang Goreng\t: Rp 8.000
# 5. Chicken Nugget\t: Rp 12.500
#       """)
# print("-"*41)
# menu = int(input("Masukkan pilihan menu\t: "))
# jmlh = int(input("Masukkan jumlah makanan\t: "))

# if menu == 1:
#     hasil = 15000 * jmlh
#     makanan = "Nasi Goreng"
# elif menu == 2:
#     hasil = 17000 * jmlh
#     makanan = "Spageti"
# elif menu == 3:
#     hasil = 55000 * jmlh
#     makanan = "Pizza"
# elif menu == 4:
#     hasil = 8000 * jmlh
#     makanan = "Kentang Goreng"
# elif menu == 5:
#     hasil = 12500 * jmlh
#     makanan = "Chicken Nugget"
# else:
#     print("Menu tidak tersedia !")

# print()
# print("-"*16,"BILL","-"*18)
# print(f"""
# Makanan\t\t: {makanan}
# Porsi\t\t: {jmlh}
# Total Harga\t: Rp {hasil}
#     """)
# print("-"*41)

# 2
# hasil = 0
# makanan = ""
# print("-"*41)
# print("-"*14,"DAFTAR MENU","-"*14)
# print("-"*41)
# print("""
# 1. Nasi Goreng\t\t: Rp 15.000
# 2. Spageti\t\t: Rp 17.000
# 3. Pizza\t\t: Rp 55.000
# 4. Kentang Goreng\t: Rp 8.000
# 5. Chicken Nugget\t: Rp 12.500
#       """)
# print("-"*41)
# menu = int(input("Masukkan pilihan menu\t: "))
# jmlh = int(input("Masukkan jumlah makanan\t: "))

# match menu:
#     case 1:
#         hasil = 15000 * jmlh
#         makanan = "Nasi Goreng"
#     case 2:
#         hasil = 17000 * jmlh
#         makanan = "Spageti"
#     case 3:
#         hasil = 55000 * jmlh
#         makanan = "Pizza"
#     case 4:
#         hasil = 8000 * jmlh
#         makanan = "Kentang Goreng"
#     case 5:
#         hasil = 12500 * jmlh
#         makanan = "Chicken Nugget"
#     case _:
#         print("Menu tidak tersedia !")

# print()
# print("-"*16,"BILL","-"*18)
# print(f"""
# Makanan\t\t: {makanan}
# Porsi\t\t: {jmlh}
# Total Harga\t: Rp {hasil}
#     """)
# print("-"*41)


## Demo 6 - Perulangan
# 1
# maks = int(input("Masukkan angka maksimal bilangan ganjil: "))
# for i in range(maks+1):
#     if i % 2 != 0:
#         print(i, end=" ")

# 2
# i = 1
# maks = int(input("Masukkan angka maksimal bilangan ganjil: "))
# while i <= maks:
#     if i % 2 != 0:
#         print(i, end=" ")
#     i+=1

# 3
# print("-"*4,"PROGRAM PENGOLAHAN NILAI MAHASISWA","-"*4)
# jmlh = int(input("\nMasukkan jumlah mahasiswa: "))

# for i in range(jmlh):
#     print()
#     print("-"*8,f"Mahasiswa ke-{i+1}","-"*8)
#     nama = input("Masukkan nama mahasiswa: ")
#     npm = input("Masukkan NPM: ")
#     print("-"*8,"PERHITUNGAN NILAI","-"*8)
#     tgs = float(input("Masukkan Nilai Tugas\t: "))
#     kuis = float(input("Masukkan Nilai Kuis\t: "))
#     uts = float(input("Masukkan Nilai UTS\t: "))
#     uas = float(input("Masukkan Nilai UAS\t: "))
#     hasil = float(tgs * 0.4) + (kuis * 0.2) + (uts * 0.2) + (uas * 0.2)

#     print("-"*8,"HASIL NILAI","-"*8)
#     print(f"""Nama\t\t: {nama}
# NPM\t\t: {npm}
# Hasil Akhir\t: {hasil:.2f}""")


## Demo 7 Perulangan 2
# 1
# a = int(input("Masukkan nilai: "))
# for i in range(a):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# 2
# a = int(input("Masukkan nilai: "))
# while True:
#     for i in range(a):
#         i+=1
#         print(i)
#     if i == a:
#         break

# 3
# a = 20
# for i in range(a+1):
#     if i % 2 == 0:
#         if i == 12 :
#             continue
#         print(i, end=" ")

# 4
# a = int(input("Masukkan sisi: "))
# for i in range(a):
#     for j in range(a):
#         if i == 0 or i == a-1 or j == 0 or j == a-1:
#             print("$", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


## Demo 8 Fungsi / Prosedur(tanpa return)
# 1
# def fungsi_rata(data):
#     hasil = 0
#     for i in range(data):
#         angka = int(input(f"Masukkan angka ke {i+1}: "))
#         hasil = hasil + angka

#     rata = float(hasil/data)
#     print(f"Rata-rata : {rata}")

# data = int(input("Banyak data : "))
# fungsi_rata(data)

# 2
# def vol_kubus(sisi):
#     vol = sisi**3
#     print(f"Volume kubus : {vol}")

# sisi = int(input("Masukkan sisi kubus: "))
# vol_kubus(sisi)


## Modul 10 Fungsi dengan return
# 1
# def perkalian(angka1, angka2):
#     return angka1*angka2

# a = int(input("Masukkan angka pertama: "))
# b = int(input("Masukkan angka kedua: "))
# hasil = perkalian(a,b)
# print(f"Hasil perhitungan : {hasil}")

# 2
# import os

# def vol(p,l,t):
#     return p * l * t

# def luper(p,l,t):
#     return ((p*l)*2) + ((p*t)*2) + ((l*t)*2)

# print("="*3,"Hitung Balok","="*3)
# panjang = int(input("Masukkan Panjang Balok\t: "))
# lebar = int(input("Masukkan Lebar Balok\t: "))
# tinggi = int(input("Masukkan Tinggi Balok\t: "))

# # os.system("cls")
# while True:
#     print("\n=== Menu Balok ===")
#     print("""1. Menghitung Volume
# 2. Menghitung Luas Permukaan""")
#     menu = int(input("Masukkan pilihan menu >> "))

#     match menu:
#         case 1:
#             hasil = float(vol(panjang,lebar,tinggi))
#             print(f"Volume Balok = {hasil:.1f}")
#         case 2:
#             hasil = float(luper(panjang,lebar,tinggi))
#             print(f"Luas Permukaan Balok = {hasil:.1f}")
#         case 0:
#             print("Program berhenti XD")
#             break
#         case _:
#             print("Pilihan menu tidak tersedia")


## Demo 11 Nested Fungsi
# import os

# def input_jenis():
#     print("""Jenis smartphone :
# 1. Iphone X
# 2. Samsung S9+
# 3. Xiaomi Mi Mix 2""")
#     jenis = int(input("Masukkan jenis smartphone: "))
#     return jenis

# def beli_ecer():
#     print("\n== Beli Eceran ==")
#     jenis = input_jenis()

#     while True:
#         jmlh = int(input("Masukkan jumlah smartphone yang dibeli: "))
#         if jmlh >= 5:
#             print("\nJumlah beli eceran tidak boleh lebih dari 4!!")
#         else:
#             total = float(hitung_total(jenis,jmlh))
#             print(f"Total yang harus dibayarkan Rp {total:.2f}")
#             getch()
#             break
        
# def beli_grosir():
#     print("\n== Beli Grosir ==")
#     jenis = input_jenis()

#     while True:
#         jmlh = int(input("Masukkan jumlah smartphone yang dibeli: "))
#         if jmlh < 5:
#             print("\nJumlah beli eceran tidak boleh kurang dari 5!!")
#         else:
#             total = float(hitung_total(jenis,jmlh))
#             print(f"Total yang harus dibayarkan Rp {total:.2f}")
#             getch()
#             break
        
# def set_harga(jenis):
#     if jenis == 1:
#         return 20000000
#     elif jenis == 2:
#         return 13000000
#     elif jenis == 3:
#         return 9500000

# def hitung_diskon(jmlh):
#     diskon = 0

#     while jmlh >= 5:
#         diskon += 5
#         jmlh -= 5
#     return diskon

# def hitung_total(jenis,jmlh):
#     total = jmlh * float(set_harga(jenis))
#     if jmlh > 5:
#         total = total - (float(hitung_diskon(jmlh)))/100 * total
#     return total

# def getch():
#     try:
#         # For Windows
#         import msvcrt
#         return msvcrt.getch().decode('utf-8')
#     except ImportError:
#         pass

# while True:
#     os.system("cls")
#     print("""===---Demo Fungsi---===
# 1. Beli eceran smartphone
# 2. Beli grosir smartphone
# 0. Exit""")
#     pilih = int(input("Masukkan Pilihan: "))

#     match pilih:
#         case 1:
#             beli_ecer()
#         case 2:
#             beli_grosir()
#         case 0:
#             print("Program selesai!")
#             break
#         case _:
#             print("Menu tidak tersedia!")
#             getch()


## Demo 12 Array
# 1
# data_a = [8,5,4,0]
# print(f"4 digit nomor npm Saya adalah {data_a[0]} {data_a[1]} {data_a[2]} {data_a[3]}")

# 2
# data_a = [[8],[5],[4],[0]]
# print(f"4 digit nomor npm Saya adalah {data_a[0][0]} {data_a[1][0]} {data_a[2][0]} {data_a[3][0]}")

# 3 
# import os

# data = []

# def input_data():
#     data.clear()
#     for i in range(9):
#         data.insert(i,input(f"Urutan angka NPM Anda mulai data ke {i+1} : "))

# def tampil_data():
#     print()
#     print("NPM : ")
#     for i in range(9):
#         print(f"{data[i]}", end=" ")
#     print()
#     print("="*23)

# def getch():
#     try:
#         # For Windows
#         import msvcrt
#         return msvcrt.getch().decode('utf-8')
#     except ImportError:
#         pass

# while True:
#     os.system("cls")
#     print("""\n=== MENU ===
# 1. Input data NPM Anda
# 2. Tampil data
# 0. Keluar""")
#     pilih = int(input("Pilhan menu: "))

#     match pilih:
#         case 1:
#             input_data()
#         case 2:
#             tampil_data()
#             getch()
#         case 0:
#             print("Program selesai!")
#             break
#         case _:
#             print("Program tidak tersedia")
#             getch()

# 4
# import os

# data = [[]]

# def input_data():
#     data.clear()
#     for i in range(3):
#         baris = []
#         for j in range(3):
#             kolom = input(f"Nilai baris {i} kolom {j}: ")
#             baris.append(kolom)
#         data.append(baris)
#         print()

# def tampil_data():
#     print()
#     for i in range(3):
#         for j in range(3):
#             print(f"{data[i][j]}", end="\t")
#         print()
#     print("="*17)

# def getch():
#     try:
#         # For Windows
#         import msvcrt
#         return msvcrt.getch().decode('utf-8')
#     except ImportError:
#         pass

# while True:
#     os.system("cls")
#     print("""\n=== MENU ===
# 1. Input Matriks
# 2. Tampil Matriks
# 0. Keluar""")
#     pilih = int(input("Pilhan menu: "))

#     match pilih:
#         case 1:
#             input_data()
#         case 2:
#             tampil_data()
#             getch()
#         case 0:
#             print("Program selesai!")
#             break
#         case _:
#             print("Program tidak tersedia")
#             getch()


## Demo 13 Record dan AoR
# 1
# Mahasiswa = {
#     "npm" : "",
#     "ipk" : ""
# }

# npm = input("Masukkan NPM: ")
# Mahasiswa["npm"] = npm
# ipk = input("Masukkan IPK: ")
# Mahasiswa["ipk"] = ipk

# print(f"NPM : {Mahasiswa['npm']}")
# print(f"IPK : {Mahasiswa['ipk']}")

# 2
# nama = []
# sks = []
# matkul = {
#     "nama" : nama,
#     "sks" : sks
# }


# while True:
#     print("""\n1. Input
# 2. Tampil
# 0. Exit""")
#     pil = int(input(">>>>> "))

#     if pil == 1:
#         nama.clear()
#         sks.clear()
#         for i in range(2):
#             nama.insert(i,input("Masukkan nama matakuliah: "))
#             sks.insert(i,input("Masukkan jumlah sks matakuliah: "))
#     elif pil == 2:
#         if nama == [] or sks == []:
#             print("Silahkan Input!")
#         else:
#             for i in range(2):
#                 print(f"Nama Matakuliah: {matkul['nama'][i]}")
#                 print(f"Jumlah SKS Matakuliah: {matkul['sks'][i]}")
#     elif pil == 0:
#         print("Program Berhenti!")
#         break
#     else:
#         print("Program Tidak Tersedia!")

## TAMAT