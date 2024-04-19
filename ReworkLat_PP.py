## Lat 4
# 1
# jam = int(input("Input jam: "))

# jam = jam * 3600
# print(f"Hasil konversi jam ke detik: {jam}")

# 2
# rho  = 5.27
# bil = int(input("Input bilangan: "))
# hasil = (bil**2) * rho
# print(f"Nilai dari K adalah: {hasil:.2f}")

# 3
# bil1 = int(input("Masukkan bilangan pertama: "))
# bil2 = int(input("Masukkan bilangan kedua: "))

# print(f"\nHasil dari penjumlahan: {bil1 + bil2:.2f}")
# print(f"Hasil dari pembagian: {bil1 / bil2:.2f}")
# print(f"Hasil dari pemangkatan: {bil1 ** bil2:.2f}")

# 4
# kasir = input("Masukkan nama kasir\t: ")
# pelanggan = input("Masukkan nama pelanggan\t: ")

# print("\nMasukkan jumlah obat yang dibeli:")
# para = int(input("Paracetamol\t: "))
# anti = int(input("Antimo\t\t: "))
# sup = int(input("Suplemen\t: "))

# total = (para*30200) + (anti*12700) + (sup*190800)
# print()
# print("="*30)
# print(f"Kasir\t\t: {kasir}")
# print(f"Pelanggan\t: {pelanggan}\n")

# print(f"""Detail Pesanan\t: 
# Paracetamol\t: {para} Box
# Antimo\t\t: {anti} Box
# Suplemen\t: {sup} Box
# Total Biaya\t: Rp {total}""")

# 5 + bonus
# print("="*7,"Universitas Langitku Cerah","="*7)
# nama = str(input("Input Nama Mahasiswa\t: "))
# npm = int(input("Input NPM\t\t: "))
# fak = str(input("Input Fakultas\t\t: "))
# prodi = str(input("Input Program Studi\t: "))
# sks = int(input("Input Jumlah SKS\t: "))

# total = sks * 225000

# print()
# print("="*10,"Data Mahasiswa","="*10)
# print(f"""Nama Mahasiswa\t: {nama}
# NPM\t\t: {npm}
# Fakultas\t: {fak}
# Program Studi\t: {prodi}
# Jumlah SKS\t: {sks}
# Total Biaya\t: Rp {total}""")


## Lat 5
# 1
# asam = float(input("Masukkan tingkat keasaman kopi toko Bapak Udin: "))

# if asam <= 4.7:
#     print(f"\nTingkat keasaman kopi Bapak Udin adalah {asam:.2f}% merupakan jenis kopi Liberica")
# elif asam <= 6.5:
#     print(f"\nTingkat keasaman kopi Bapak Udin adalah {asam:.2f}% merupakan jenis kopi Arabica")
# elif asam <= 10:
#     print(f"\nTingkat keasaman kopi Bapak Udin adalah {asam:.2f}% merupakan jenis kopi Robusta")
# else:
#     print(f"\nKopi apa tu man, asem banget !!")

# 2 + bonus
# nama = "Ucup Surucup"
# npm = "211711087"
# kelas = "A"

# print("-- Modul Pemilihan Kelas A --")
# print(""" a. Tampil Nama dan NPM
#  b. Tampil Nama dan Kelas
#  c. Tampil Semua Data""")
# menu = str(input(" Masukkan menu: "))

# match menu:
#     case "a" | "A":
#         print(f"""\nNama\t: {nama}
# NPM\t: {npm}""")
#     case "b" | "B":
#         print(f"""\nNama\t: {nama}
# Kelas\t: {kelas}""")
#     case "c" | "C":
#         print(f"""\nNama\t: {nama}
# NPM\t: {npm}
# Kelas\t: {kelas}""")
#     case 0:
#         print("Program berhenti!")
#     case _:
#         print("\033[43m Program tidak tersedia!")

# 3
# phi = 3.14
# print("="*39)
# print("== Kalkulator Bangun Ruang Sederhana ==")
# print("="*14,"Bapak Ucup","="*13)
# print(""" 1. Volume Bola
#  2. Luas Permukaan Bola
#  3. Volume Balok
#  4. Luas Permukaan Balok
#  0. EXIT""")
# print("="*39)

# menu = int(input(" Input menu: "))

# if menu == 1 or menu == 2 or menu == 3 or menu == 4:
#     if menu == 1:
#         bangun = "Volume Bola"
#         jari= int(input("\n Masukkan jari-jari: "))
#         hasil = (4/3) * phi * jari** 3
#     elif menu == 2:
#         bangun = "Luas Permukaan Bola"
#         jari= int(input("\n Masukkan jari-jari: "))
#         hasil = 4 * phi * jari** 2
#     elif menu == 3:
#         bangun = "Volume Balok"
#         pjg = int(input("\n Masukkan panjang\t: "))
#         leb = int(input(" Masukkan lebar\t\t: "))
#         ting = int(input(" Masukkan tinggi\t: "))
#         hasil = pjg * leb * ting
#     elif menu == 4:
#         bangun = "Luas Permukaan Balok"
#         pjg = int(input("\n Masukkan panjang\t: "))
#         leb = int(input(" Masukkan lebar\t\t: "))
#         ting = int(input(" Masukkan tinggi\t: "))
#         hasil = 2 * ((pjg*leb) + (pjg*ting) + (leb*ting))

#     print("-"*39)
#     print(f"{bangun} adalah\t: {hasil:.2f}")

# elif menu == 0:
#     print("Program Selesai!")
# else:
#     print("Program tidak tersedia!")

# 4
# print("="*39)
# print("="*8,"MbahUcupMechanical.ID","="*8)
# print("="*39)
# print(""" 1. Linear Switch\t: Rp 5000/pcs
#  2. Tactile Switch\t: Rp 7500/pcs
#  3. Clicky Switch\t: Rp 9000/pcs
#  0. EXIT""")
# print("="*39)

# menu = int(input(" Input menu\t : "))
# if menu == 1 or menu == 2 or menu == 3:
#     jmlh = int(input(" Input jumlah\t : "))
#     pel = str(input(" Apakah Anda pelanggan setia? [yes/no]: "))

#     if menu == 1:
#         barang = "Linear"
#         if pel == "yes" and jmlh >= 20:
#             total = (jmlh * 5000) * (90/100)
#         else:
#             total = jmlh * 5000
#     elif menu == 2:
#         barang = "Tactile"
#         if pel == "yes" and jmlh >= 35:
#             total = (jmlh * 7500) * (85/100)
#         else:
#             total = jmlh * 7500
#     elif menu == 3:
#         barang = "Clicky"
#         if pel == "yes" and jmlh >= 65:
#             total = (jmlh * 9000) * (70/100)
#         else:
#             total = jmlh * 9000

#     print()
#     print("="*12,"Data Pembelian","="*11)
#     print(f""" >> Switch\t : {barang}
#  >> Jumlah\t : {jmlh}""")
#     print("="*39)
#     print(f" >> Total Harga\t : Rp {total:.2f}")

#     bayar = float(input(" >> Jumlah bayar : Rp "))
#     while bayar < total:
#         print(" Jumlah bayar kurang!")
#         bayar = float(input(" >> Jumlah bayar : Rp "))

#     print("="*39)
#     print(f" >> Kembalian\t : Rp {bayar - total:.2f}")
# elif menu == 0:
#     print("Program Selesai! :)")
# else:
#     print("Program tidak tersedia!")


## Lat 6
# 1 for - while..do
# for
# angka = int(input("Masukkan bilangan Bapak Ucup: "))

# for i in range(angka):
#     if i % 2 == 0:
#         print(f"Perulangan ke {i+2} bernilai genap")

# while
# angka = int(input("Masukkan bilangan Bapak Ucup: "))
# start = 1

# while start <= angka:
#     if start % 2 == 0:
#         print(f"Perulangan ke {start} bernilai genap")
#     start += 1

# 2
# print("-"*38)
# print("-"*9,"Sekolah Bapak Udin","-"*9)
# print("-"*38)
# jmlh = int(input("Input jumlah siswa : "))
# print("-"*38)

# start = 1
# while start <= jmlh:
#     print()
#     tgs = 1
#     nama = input(f"Masukkan nama siswa ke-{start} : ")
#     tgs1 = int(input(f"Masukkan nilai tugas {tgs}\t : "))
#     tgs2 = int(input(f"Masukkan nilai tugas {tgs+1}\t : "))
#     tgs3 = int(input(f"Masukkan nilai tugas {tgs+2}\t : "))
#     print("-"*38)
#     hasil = float((tgs1 + tgs2 + tgs3)/3)
#     print(f"Nilai rata-rata {nama} adalah {hasil:.1f}")
#     print("-"*38)
#     start += 1

# 3
# import os
# def getch():
#     try:
#         # For Windows
#         import msvcrt
#         return msvcrt.getch().decode('utf-8')
#     except ImportError:
#         pass
# nama = ""
# npm = ""
# alamat = ""
# sks = 0
# menu = 1

# while menu != 0:
#     os.system("cls")
#     print("="*5,"Menu Mahasiswa","="*5)
#     print(""" 1. Input Data
#  2. Tampil Data
#  0. EXIT""")
#     print("="*26)

#     menu = int(input(" Pilih menu : "))
#     if menu == 1:
#         os.system("cls")
#         print("="*5,"Input Data","="*5)
#         nama = str(input("Masukkan nama\t: "))
#         npm = str(input("Masukkan NPM\t: "))
#         alamat = str(input("Masukkan alamat\t: "))
#         sks = int(input("Jumlah SKS \t: "))
#     elif menu == 2:
#         os.system("cls")
#         print("="*5,"Tampil Data","="*5)
#         print(f""" Nama\t: {nama}
#  NPM\t: {npm}
#  Alamat\t: {alamat}
#  SKS\t: {sks}""")
#         print("="*26)
#         print(f" Total bayar SKS : Rp. {sks*250000:.2f}")
#         getch()
#     elif menu == 0:
#         os.system("cls")
#         print(">>Tengkyuuu :)")
#         break
#     else:
#         print(" Menu tidak tersedia!")
#         getch()


## Lat 7
# 1
# import os
# def getch():
#     try:
#         # For Windows
#         import msvcrt
#         return msvcrt.getch().decode('utf-8')
#     except ImportError:
#         pass
# menu = 1
# user = "admin"
# passw = "admin"
# akses = 0

# while menu != 0:
#     os.system("cls")
#     print("""Menu
# [1] Login
# [2] Daftar Peserta
# [3] Lihat Peserta
# [0] Exit""")
    
#     menu = int(input(">>> : "))
#     if menu == 1:
#         os.system("cls")
#         print("==== LOGIN ====")
#         if akses == 0:
#             while akses == 0:
#                 input_user = input("Username : ")
#                 input_pass = input("Password : ")
#                 if input_user != user or input_pass != passw:
#                     print("Username or Password Incorrect...\n")
#                 elif input_user == user and input_pass == passw:
#                     akses = 1
#                     print("Login success!")
#                     getch()
#         elif akses > 0:
#             print("Anda sudah Login!") # nggk keluar, butuh getch
#             getch()
#     elif menu == 2:
#         if akses == 0:
#             print("Silahkan login dahulu!")
#             getch()
#         elif akses > 0:
#             print("="*5,"DAFTAR PESERTA","="*5)

#             nama = input("Nama : ")
#             while nama == "":
#                 print("Nama tidak boleh kosong!")
#                 nama = input("Nama : ")
#                 if nama != "":
#                     break
            
#             member = input("No. Member : ")
#             while len(member) != 9:
#                 print("No Member harus 9 digit!")
#                 member = input("No. Member : ")
#                 if len(member) == 9:
#                     break

#             type_member = input("Jenis Member : ")
#             if type_member == "Bronze" or type_member == "Silver" or type_member == "Gold":
#                 pass
#             else:
#                 while type_member != "Bronze" or type_member != "Silver" or type_member != "Gold":
#                     print("Jenis Member hanya -> Bronze / Silver / Gold!")
#                     type_member = input("Jenis Member : ")
#                     if type_member == "Bronze" or type_member == "Silver" or type_member == "Gold":
#                         break
            
#             akses = 2
#             print("Data berhasil diinput!")
#             getch()
#     elif menu == 3:
#         if akses <= 1:
#             print("Silahkan input dahulu!")
#             getch()
#         elif akses > 1:
#             print("="*5,"DATA PESERTA","="*5)
#             print(f"""\nNama\t\t: {nama}
# Nomor Member\t: {member}
# Jenis Member\t: {type_member}\n""")
#             print("="*5,"*"*12,"="*5)
#             getch()
#     else:
#         os.system("cls")
#         print("Terima kasih telah mengunjungi program ini :)")

# 2
# import os
# def getch():
#     try:
#         # For Windows
#         import msvcrt
#         return msvcrt.getch().decode('utf-8')
#     except ImportError:
#         pass
# judul = "CETAK BENTUK"
# menu = 1

# while menu != 0:
#     os.system("cls")
#     print(judul)
#     print("="*len(judul),"\n")
#     print("""[1] Bentuk Persegi Full
# [2] Bentuk Segitiga Siku Siku
# [3] Bentuk Persegi
# [4] Bentuk Jendela
# [0] EXIT""")
#     menu = int(input("Pilih Menu : "))

#     if menu == 1 or menu == 2 or menu == 3 or menu == 4:
#         sisi = int(input("\nMasukkan panjang sisi : "))
#         if menu == 1:
#             print()
#             print("="*5,"Persegi Full","="*5)
#             for i in range(sisi):
#                 for j in range(sisi):
#                     print("*", end=" ")
#                     if j == sisi-1:
#                         print()
#             getch()
#         elif menu == 2:
#             print()
#             print("="*5,"Segitiga","="*5)
#             for i in range(sisi):
#                 for j in range(i+1):
#                     print("*", end=" ")
#                 print()
#             getch()
#         elif menu == 3:
#             print()
#             print("="*5,"Persegi","="*5)
#             for i in range(sisi):
#                 for j in range(sisi):
#                     if j == 0 or j == sisi-1 or i == 0 or i == sisi-1:
#                         print("*", end=" ")
#                     else:
#                         print(" ",end=" ")
#                 print()
#             getch()
#         elif menu == 4:
#             while sisi % 2 == 0:
#                 print("Sisi harus berjumlah ganjil!")
#                 sisi = int(input("\nMasukkan panjang sisi : "))
#             print()
#             print("="*5,"Jendela","="*5)
#             for i in range(sisi):
#                 for j in range(sisi):
#                     if j == 0 or j == sisi-1 or j == sisi//2 or i == 0 or i == sisi-1 or i == sisi//2:
#                         print("*", end=" ")
#                     else:
#                         if (sisi % 2 == 1):
#                             print(" ",end=" ")
#                         else:
#                             print(" ",end=" ")
#                 print()
#             getch()
#     elif menu == 0:
#         print("Program Selesai!")
#     else:
#         print("Menu tidak tersedia")
#         getch()


## Lat 8 prosedur/fungsi
# 1
# import os

# menu = 1

# def hitungPersegi():
#     print("\tHITUNG LUAS PERSEGI")
#     sisi = int(input("\tMasukkan sisi persegi: "))
#     print(f"\n\tLuas Persegi: {sisi*sisi} cm")
#     input()
# def hitungPerPanjang():
#     print("\tHITUNG LUAS PERSEGI PANJANG")
#     pjg = int(input("\tMasukkan Panjang: "))
#     lbr = int(input("\tMasukkan Lebar: "))
#     print(f"\n\tLuas Persegi Panjang: {pjg*lbr} cm")
#     input()
# def hitungSegitiga():
#     print("\tHITUNG LUAS SEGITIGA")
#     alas = int(input("\tMasukkan Alas: "))
#     tinggi = int(input("\tMasukkan Tinggi: "))
#     print(f"\n\tLuas Segitiga: {(alas*tinggi)*0.5} cm")
#     input()

# while menu != 0:
#     os.system("cls")
#     print("\t---=====","HITUNG LUAS","=====---")
#     print("""[1] Persegi
# [2] Persegi Panjang
# [3] Segitiga
# [0] EXIT""")
#     menu = int(input(">> : "))

#     if menu == 1:
#         hitungPersegi()
#     elif menu == 2:
#         hitungPerPanjang()
#     elif menu == 3:
#         hitungSegitiga()
#     elif menu == 0:
#         print("Program selesai!")
#     else:
#         print("Menu tidak tersedia!")
#         input()

# 2
# import os

# menu = 1
# phi = 3.14

# def hitungBalok():
#     pjg = int(input("\nMasukkan Panjang: "))
#     lbr = int(input("Masukkan Lebar: "))
#     tinggi = int(input("Masukkan Tinggi: "))
#     print(f"\nVolume Balok: {pjg*lbr*tinggi:.2f}")
#     input()
# def hitungTabung(jari,tinggi):
#     print(f"\nVolume Tabung: {phi*(jari**2)*tinggi:.2f}")
#     input()
# def hitungKerucut(jari,tinggi):
#     print(f"\nVolume Kerucut: {(phi*(jari**2)*tinggi)/3:.2f}")
#     input()

# while menu != 0:
#     os.system("cls")
#     print("\t---=====","HITUNG VOLUME BANGUN RUANG","=====---")
#     print("""[1] Balok
# [2] Tabung
# [3] Kerucut
# [0] EXIT""")
#     menu = int(input(">> : "))

#     if menu == 1:
#         hitungBalok()
#     elif menu == 2:
#         jari = int(input("\nMasukkan Jari-jari: "))
#         tinggi = int(input("Masukkan Tinggi: "))
#         hitungTabung(jari,tinggi)
#     elif menu == 3:
#         jari = int(input("\nMasukkan Jari-jari: "))
#         tinggi = int(input("Masukkan Tinggi: "))
#         hitungKerucut(jari,tinggi)
#     elif menu == 0:
#         print("Program selesai!")
#     else:
#         print("Menu tidak tersedia!")
#         input()

# 3
# import os

# isLogin = False
# menu = -1

# def login(input_user,input_pass):
#     global isLogin
#     user = "yogi"
#     passw = "1234"
#     if user != input_user or passw != input_pass:
#         print("Username atau Password salah !\n")
#     elif user == input_user and passw == input_pass:
#         isLogin = True
#         input("Login Success!")   
# def hitungWaktu(jam):
#     print("\n\tHASIL KONVERSI\n")
#     print(f"\tMenit\t: {jam*60} menit")
#     print(f"\tDetik\t: {jam*3600} detik")
#     input()
# def hitungSuhu(cel):
#     print("\n\tHASIL KONVERSI\n")
#     print(f"\tKelvin: {cel+273.15:.2f}K")
#     print(f"\tFahrenheit: {(cel*(9/5)+32):.2f}F")
#     input()
# def tampilGenap(awal,akhir):
#     hasil = 0
#     print("\n\tTAMPIL GENAP")
#     for i in range(awal,akhir+1):
#         if i % 2 == 0:
#             print(i,end=" ")
#             hasil += 1
#     print(f"\nBilangan genap dari {awal} hingga {akhir} berjumlah: {hasil}")
#     input()

# if isLogin == False:
#     os.system("cls")
#     while isLogin == False:
#         input_user = input("USERNAME: ")
#         input_pass = input("PASSWORD: ")
#         login(input_user, input_pass)
# if isLogin == True:
#     while menu != 0:
#         os.system("cls")
#         print("\tKALKULATOR SEDERHANA")
#         print("""[1] Waktu
# [2] Suhu
# [3] Tampil Genap
# [0] EXIT""")
#         menu = int(input(">> : "))

#         if menu == 1:
#             jam = int(input("Input Jam: "))
#             hitungWaktu(jam)
#         elif menu == 2:
#             cel = int(input("Input Celcius: "))
#             hitungSuhu(cel)
#         elif menu == 3:
#             awal = int(input("Input bilangan awal: "))
#             akhir = int(input("Input bilangan akhir: "))
#             tampilGenap(awal,akhir)
#         elif menu == 0:
#             print("Program selesai!")
#         else:
#             input("Menu tidak tersedia!")


## Lat 9 prosedur/fungsi 2
# 1
# import os

# isLogin = True
# total = 0

# def login(input_user,input_pass):
#     global isLogin
#     user = "toko"
#     passw = "1234"
#     if user != input_user or passw != input_pass:
#         print("Username atau Password salah !\n")
#     elif user == input_user and passw == input_pass:
#         isLogin = True
#         input("Login Success!")
# def menuSmartphone(total):
#     # print(total)
#     menu = -1
#     while menu < 1 or menu >3:
#         menu = int(input("Pilih Smartphone : "))
#         if menu < 1 or menu >3:
#             print("Smartphone tidak tersedia!")
#         else:
#             jmlh = int(input("Jumlah : "))
#             if menu == 1:
#                 harga = 1850000
#             elif menu == 2:
#                 harga = 2100000
#             elif menu == 3:
#                 harga = 1525000

#             sub = jmlh*harga
#             total += sub

#             lanjut = input("Lanjut berbelanja [y/n]? ")
#             if lanjut == "n":
#                 os.system("cls")
#                 print("PEMBAYARAN")
#                 print(f"Total Bayar : Rp {total:.1f}")
#                 bayar = int(input("Bayar : Rp "))
#                 while bayar < total:
#                     bayar = int(input("Bayar : Rp "))
#                 print(f"Kembalian : {pembayaran(total,bayar)}")
#                 print("Terimakasih...")
#             else:
#                 menuSmartphone(total)
# def pembayaran(total,bayar):
#     return bayar-total    

# if isLogin == False:
#     os.system("cls")
#     while isLogin == False:
#         input_user = input("USERNAME: ")
#         input_pass = input("PASSWORD: ")
#         login(input_user, input_pass)
# if isLogin == True:
#     os.system("cls")
#     print("Menu Pembayaran Barang")
#     print("""[1] Xiaomi Redmi 10C\t: Rp 1.850.000
# [2] Realme C35\t\t: Rp 2.100.000
# [3] Realme C31\t\t: Rp 1.525.000""")
#     menuSmartphone(total) 

# 2
# import os
# import random

# menu = -1
# akses = 0
# nama = []
# disc = []

# def login():
#     user = "toko"
#     passw = "1234"
#     print("\nLOGIN")
#     input_user = input("USERNAME: ")
#     input_pass = input("PASSWORD: ")
#     while user != input_user or passw != input_pass:
#         if user != input_user or passw != input_pass:
#             print("Username atau Password salah !\n")
#             input_user = input("USERNAME: ")
#             input_pass = input("PASSWORD: ")
#     if user == input_user and passw == input_pass:
#         input("Login Success!")
# def input_data(nama,disc):
#     print("INPUT DATA\n")
#     for i in range(3):
#         nama_temp = input(f"Nama Pelanggan {i+1}: ")
#         disc_temp = random.randint(1,50)
#         print(f"Diskon: {disc_temp}\n")
#         nama.insert(i,nama_temp) # input data ke list
#         disc.insert(i,disc_temp) # input data ke list
#     input("Input data berhasil!")
# def show_data(nama,disc):
#     print("Tampil DATA\n")
#     for i in range(3):
#         print(f"Nama pelanggan {i+1}: {nama[i]}")
#         print(f"Diskon : {disc[i]}")
#     input()

# while menu != 0:
#     os.system("cls")
#     print("Menu Pembayaran Barang")
#     print("""[1] Login
# [2] Input Data
# [3] Tampil Data
# [0] EXIT""")
#     menu = int(input(">> : "))

#     if menu == 1:
#         if akses <= 0:
#             login()
#             akses = 1
#         else:
#             input("Anda sudah login!")
#     elif menu == 2:
#         if akses < 1:
#             input("Anda harus login!")
#         else:
#             input_data(nama,disc)
#             akses = 2
#     elif menu == 3:
#         if akses < 2:
#             input("Anda harus input!")
#         else:
#             show_data(nama,disc)
#     elif menu == 0:
#         print("Program selesai!")
#     else:
#         input("Menu tidak tersedia!")


## Lat 10
# 1
# def find_max(angka1,angka2,angka3):
#     if angka1>angka2 and angka1>angka3:
#         hasil = angka1
#     elif angka2>angka1 and angka2>angka3:
#         hasil = angka2
#     elif angka3>angka1 and angka3>angka1:
#         hasil = angka3
#     return hasil
# def find_min(angka1,angka2,angka3):
#     if angka1<angka2 and angka1<angka3:
#         hasil = angka1
#     elif angka2<angka1 and angka2<angka3:
#         hasil = angka2
#     elif angka3<angka1 and angka3<angka1:
#         hasil = angka3
#     return hasil
# def find_avg(angka1,angka2,angka3):
#     return (angka1+angka2+angka3)/3

# angka1 = int(input("Masukkan angka pertama: "))
# angka2 = int(input("Masukkan angka kedua: "))
# if angka2 == angka1:
#     while angka2 == angka1:
#         print("Angka tidak boleh sama!")
#         angka2 = int(input("Masukkan angka kedua: "))

# angka3 = int(input("Masukkan angka ketiga: "))
# if angka3 == angka1 or angka3 == angka2:
#     while angka3 == angka1 or angka3 == angka2:
#         print("Angka tidak boleh sama!")
#         angka3 = int(input("Masukkan angka ketiga: "))

# maks = find_max(angka1,angka2,angka3)
# minim = find_min(angka1,angka2,angka3)
# avg = find_avg(angka1,angka2,angka3)

# print(f"\nNilai terbesar adalah: {maks}")
# print(f"Nilai terkecil adalah: {minim}")
# print(f"Nilai rata-rata adalah: {avg:.2f}")

# 2a
# import os
# def tampil_siswa():
#     demo = int(input("Masukkan nilai Demo\t:"))
#     tugas = int(input("Masukkan nilai Tugas\t:"))
#     uts = int(input("Masukkan nilai UTS\t:"))
#     uas = int(input("Masukkan nilai UAS\t:"))
#     tampil_nilai(demo,tugas,uts,uas)
# def hitung_nilai(demo,tugas,uts,uas):
#     return (demo*(5/100))+(tugas*(15/100))+(uts*(40/100))+(uas*(40/100))
# def tampil_nilai(demo,tugas,uts,uas):
#     hasil = hitung_nilai(demo,tugas,uts,uas)
#     if hasil >= 85:
#         print(f"\nGreat! Nilai = {hasil:.2f}, mendapatkan A")
#     elif hasil >= 70:
#         print(f"\nGood! Nilai = {hasil:.2f}, mendapatkan B")
#     else:
#         print(f"\nLow! Nilai = {hasil:.2f}, mendapatkan C")

# # Main #
# os.system("cls")
# print("Penilaian Siswa\n")
# tampil_siswa()
# print("-"*35)

# 2b
# import os
# def tampil_siswa():
#     demo = int(input("Masukkan nilai Demo\t:"))
#     tugas = int(input("Masukkan nilai Tugas\t:"))
#     uts = int(input("Masukkan nilai UTS\t:"))
#     uas = int(input("Masukkan nilai UAS\t:"))
#     tampil_nilai(demo,tugas,uts,uas)
# def hitung_nilai(demo,tugas,uts,uas):
#     return (demo*(5/100))+(tugas*(15/100))+(uts*(40/100))+(uas*(40/100))
# def tampil_nilai(demo,tugas,uts,uas):
#     hasil = hitung_nilai(demo,tugas,uts,uas)
#     if hasil >= 85:
#         print(f"\nGreat! Nilai = {hasil:.2f}, mendapatkan A")
#     elif hasil >= 70:
#         print(f"\nGood! Nilai = {hasil:.2f}, mendapatkan B")
#     else:
#         print(f"\nLow! Nilai = {hasil:.2f}, mendapatkan C")

# # Main #
# os.system("cls")
# print("Penilaian Siswa\n")
# siswa = int(input("Masukkan jumlah siswa yang ingin dihitung: "))
# for i in range(siswa):
#     print(f"\nSiswa ke-{i+1}")
#     tampil_siswa()
# print("-"*35)

# 3 bonus
# use gpt, konsep = pakai list dan fungsi dari random.choice (import random)
# import os
# import random

# def show_food():
#     foods = ["Nasi Goreng", "Mie Goreng", "Ayam Goreng", "Bakso", "Soto", "Pizza", "Burger", "Pasta", "Sushi", "Salad"]
#     selected_food = random.choice(foods)
#     print(f"Makanan yang terpilih: {selected_food}")
# def cek_login(username, password):
#     return username == "12345" and password == "fungsi1"
# def cek_ulang():
#     ulang = input("Apakah Anda ingin memilih makanan lagi? (y/n): ")
#     return ulang.lower() == 'y'

# while True:
#     os.system("cls")
#     username = input("Masukkan username: ")
#     password = input("Masukkan password: ")

#     if cek_login(username, password):
#         print("Login berhasil!")
#         break
#     else:
#         print("Username atau password salah. Silakan coba lagi.")

# while True:
#     os.system("cls")
#     show_food()

#     if not cek_ulang():
#         print("Terima kasih. Program selesai.")
#         break


## Lat 11
# 1
# import os

# menu = -1
# akses = 0
# total_tiket = 0
# total_makan = 0

# def cek_login(username, password):
#     return username == "12345" and password == "fungsi2"
# def list_film():
#     print("""\nList Film Bioskop VCG:
# 1. The Tomorrow War
# 2. Jungle Cruise
# 3. Spider-Man: No Way Home
# 4. Mortal Combat""")
#     film = int(input("Masukkan kode film: "))
#     if film == 1 or film == 2 or film == 3 or film == 4:
#         pass
#     else:
#         while film != 1 or film != 2 or film != 3 or film != 4:
#             print("Kode film tidak tersedia!")
#             film = int(input("Masukkan kode film: "))
#             if film == 1 or film == 2 or film == 3 or film == 4:
#                 break

#     tiket = int(input("Masukkan jumlah tiket: "))

#     seat_temp = str(input("Masukkan jenis seat: "))
#     seat = seat_temp.lower()
#     if seat == "bronze" or seat == "silver" or seat == "gold":
#         pass
#     else:
#         while seat != "bronze" or seat != "silver" or seat != "gold":
#             print("Jenis seat tidak tersedia! (Bronze,Silver,Gold)")
#             seat_temp = str(input("Masukkan jenis seat: "))
#             seat = seat_temp.lower()
#             if seat == "bronze" or seat == "silver" or seat == "gold":
#                 break
    
#     input("Silahkan lanjutkan ke menu Bayar atau Makan")
#     return hitung_harga_tiket(tiket,seat)
# def hitung_harga_tiket(tiket,seat):
#     if seat == "bronze":
#         total = (40000+5000) * tiket
#     elif seat == "silver":
#         total = (40000+10000) * tiket
#     elif seat == "gold":
#         total = (40000+15000) * tiket
#     return total
# def list_makan():
#     print("""\nList Beverages Bioskop VCG:
# 1. Pop Corn\t: Rp 30.000
# 2. Fries\t: Rp 20.000
# 3. Cola\t\t: Rp 10.000""")
#     makan = int(input("Masukkan kode beverages: "))
#     if makan == 1 or makan == 2 or makan == 3:
#         pass
#     else:
#         while makan != 1 or makan != 2 or makan != 3:
#             print("Kode beverages tidak tersedia!")
#             makan = int(input("Masukkan kode beverages: "))
#             if makan == 1 or makan == 2 or makan == 3:
#                 break

#     pcs = int(input("Masukkan jumlah pembelian: "))
    
#     input("Silahkan lanjutkan ke menu Bayar atau List Film")
#     return hitung_harga_makan(makan,pcs)
# def hitung_harga_makan(makan,pcs):
#     if makan == 1:
#         hasil = 30000*pcs
#     elif makan == 2:
#         hasil = 20000*pcs
#     elif makan == 3:
#         hasil = 10000*pcs
#     return hasil
# def pembayaran(total_tiket,total_makan):
#     sub_total = total_tiket+total_makan
#     print("\nDetail Pemesanan:")
#     print(f"Total Pesanan Tiket Film: Rp {total_tiket:.2f}")
#     print(f"Total Pesanan Beverages: Rp {total_makan:.2f}")
#     print(f"Total Pesanan: Rp {sub_total:.2f}")
#     if sub_total <= 200000:
#         print("Diskon: 0%")
#         diskon = 100
#     elif sub_total <= 300000:
#         print("Diskon: 10%")
#         diskon = 90
#     elif sub_total <= 500000:
#         print("Diskon: 15%")
#         diskon = 85
#     else:
#         print("Diskon: 20%")
#         diskon = 80
    
#     total = sub_total * (diskon/100)
#     print(f"Total yang harus dibayar: Rp {total:.2f}")
#     print("="*40)

#     nama = input("Masukkan nama Anda: ")
#     bayar = int(input("Bayar: "))
#     if bayar >= total:
#         pass
#     else:
#         while bayar < total:
#             print("Uang Anda tidak cukup!")
#             bayar = int(input("Bayar: Rp "))
#             if bayar >= total:
#                 break

#     print("\nPembayaran berhasil!")
#     print(f"Kembalian: Rp {bayar-total:.2f}")
#     print(f"Terima kasih! Selamat menonton, {nama.title()}")
#     input()


# # MAIN #
# while menu != 0:
#     os.system("cls")
#     print("""Selamat datang di Bioskop VCG!
# Pilih menu:
# 1. Login
# 2. List Film
# 3. Makanan
# 4. Bayar
# 0. Logout""")
#     menu = int(input("Masukkan menu: "))

#     if menu == 1:
#         if akses < 1:
#             while True:
#                 username = input("\nMasukkan username: ")
#                 password = input("Masukkan password: ")

#                 if cek_login(username, password):
#                     akses = 1
#                     input("Login berhasil!")
#                     break
#                 else:
#                     print("Username atau password salah. Silakan coba lagi.")
#         else:
#             input("Anda sudah Login!")
#     elif menu == 2:
#         if akses < 1:
#             input("Anda belum Login!")
#         else:
#             total_tiket = list_film()
#             akses = 2
#     elif menu == 3:
#         if akses < 1:
#             input("Anda belum Login!")
#         else:
#             total_makan = list_makan()
#             akses = 2
#     elif menu == 4:
#         if akses < 1:
#             input("Anda belum Login!")
#         elif akses < 2:
#             input("Belum ada transaksi!")
#         elif akses == 2:
#             pembayaran(total_tiket,total_makan)
#             akses = 1 #bayar
#             total_tiket = 0
#             total_makan = 0
#     elif menu == 0:
#         print("LOGOUT ...")
#     else:
#         input("Menu tidak tersedia!")


## Lat 12
# 1
# import os

# menu = -1
# maks = 5
# buku = ["-","-","-","-","-"]
# # print(len(buku))
# # input()

# while menu != 0:
#     os.system("cls")
#     print("""---=== ARRAY ===---
# [1] Input Buku
# [2] Show Buku
# [3] Reset Buku
# [0] EXIT""")
#     menu = int(input(" -> : "))
#     print()
    
#     if menu == 1:
#         if len(buku) == 5 and buku[1] != "-":
#             input("Data buku penuh, harap reset!")
#         else:
#             buku.clear()
#             for i in range(maks):
#                 # buku_temp = input(f"Masukkan Judul Buku {i+1} : ")
#                 buku.insert(i,input(f"Masukkan Judul Buku {i+1} : "))
#             input("Data Buku berhasil diinput ...")
#     elif menu == 2:
#         for i in range(maks):
#             print(f"Judul Buku {i+1} : {buku[i]}")
#         input("Data Buku berhasil dishow ...")
#     elif menu == 3:
#         buku.clear()
#         for i in range(maks):
#             buku.insert(i,"-")
#         input("Data Buku berhasil direset ...")
#     elif menu == 0:
#         print("Program selesai !")
#     else:
#         input("Menu tidak tersedia !")

# 2
# import os

# menu = -1
# mahasiswa = {
#     "nama" : "-",
#     "npm" : "-",
#     "prodi" : "-",
#     "ipk" : 0.00,
#     "alamat" : "-",
# }


# while menu != 0 :
#     os.system("cls")
#     print("""---=== RECORD ===---
# [1] Input Mahasiswa
# [2] Show Mahasiswa
# [3] Reset Mahasiswa
# [0] EXIT""")
#     menu = int(input(" -> : "))
#     print()

#     if menu == 1:
#         if mahasiswa["npm"] == "-":
#             mahasiswa["nama"] = input("Masukkan Nama Mahasiswa\t  : ")
#             mahasiswa["npm"] = input("Masukkan NPM Mahasiswa\t  : ")
#             mahasiswa["prodi"] = input("Masukkan Prodi Mahasiswa  : ")
#             mahasiswa["ipk"] = float(input("Masukkan IPK Mahasiswa\t  : "))
#             mahasiswa["alamat"] = input("Masukkan Alamat Mahasiswa : ")
#             input("\nData Mahasiswa berhasil diinput ...")
#         else:
#             input("\nData Mahasiswa penuh, harap reset ...")
#     elif menu == 2:
#         print(f"Nama Mahasiswa\t : {mahasiswa["nama"]}")
#         print(f"NPM Mahasiswa\t : {mahasiswa["npm"]}")
#         print(f"Prodi Mahasiswa\t : {mahasiswa["prodi"]}")
#         print(f"IPK Mahasiswa\t : {mahasiswa["ipk"]}")
#         print(f"Alamat Mahasiswa : {mahasiswa["alamat"]}")
#         input("\nData Mahasiswa berhasil dishow ...")
#     elif menu == 3:
#         mahasiswa["nama"] = "-"
#         mahasiswa["npm"] = "-"
#         mahasiswa["prodi"] = "-"
#         mahasiswa["ipk"] = 0.00
#         mahasiswa["alamat"] = "-"
#         input("\nData Mahasiswa berhasil direset ...")
#     elif menu == 0:
#         print("Program selesai !")
#     else:
#         input("Menu tidak tersedia !")

# 3
# import os

# menu = -1
# mhs_max = 5
# mahasiswa_template = {
#     "nama" : "-",
#     "npm" : "-",
#     "ipk" : 0.00,
#     "buku1": "-",
#     "buku2": "-"
# }
# dataMhs = {}


# while menu != 0 :
#     os.system("cls")
#     print("""---=== RECORD ===---
# [1] Input Mahasiswa
# [2] Show Mahasiswa
# [3] Reset Mahasiswa
# [0] EXIT""")
#     menu = int(input(" -> : "))

#     if menu == 1:
#         if len(dataMhs) == 0:
#             for i in range(mhs_max):
#                 print(f"\nData Mahasiswa ke-{i+1}")
#                 print("-"*30)
#                 mahasiswa = dict.fromkeys(mahasiswa_template.keys())
#                 key = i
#                 dataMhs.update({key:mahasiswa})
#                 mahasiswa["nama"] = input("Masukkan Nama Mahasiswa\t  : ")
#                 dataMhs
#                 mahasiswa["npm"] = input("Masukkan NPM Mahasiswa\t  : ")
#                 mahasiswa["ipk"] = float(input("Masukkan IPK Mahasiswa\t  : "))
#                 mahasiswa["buku1"] = input("Masukkan judul buku 1\t  : ")
#                 mahasiswa["buku2"] = input("Masukkan judul buku 2\t  : ")
#                 # print(dataMhs)
#                 print("-"*30)
#             input("\nData Mahasiswa berhasil diinput ...")
#         else:
#             input("\nData Mahasiswa penuh, harap reset ...")
#     elif menu == 2:
#         if len(dataMhs) != 0:
#             for i in range(mhs_max):
#                 print(f"\nData Mahasiswa ke-{i+1}")
#                 print("-"*30)
#                 print(f"Nama Mahasiswa\t : {dataMhs[i]["nama"]}")
#                 print(f"NPM Mahasiswa\t : {dataMhs[i]["npm"]}")
#                 print(f"IPK Mahasiswa\t : {dataMhs[i]["ipk"]}")
#                 print(f"Judul Buku 1\t : {dataMhs[i]["buku1"]}")
#                 print(f"Judul Buku 2\t : {dataMhs[i]["buku2"]}")
#                 print("-"*30)
#         else:
#             for i in range(mhs_max):
#                 print(f"\nData Mahasiswa ke-{i+1}")
#                 print("-"*30)
#                 print("Nama Mahasiswa\t : -")
#                 print("NPM Mahasiswa\t : -")
#                 print("IPK Mahasiswa\t : 0.00")
#                 print("Judul Buku 1\t : -")
#                 print("Judul Buku 2\t : -")
#                 print("-"*30)
#         input("\nData Mahasiswa berhasil dishow ...")
#     elif menu == 3:
#         dataMhs.clear()
#         input("\nData Mahasiswa berhasil direset ...")
#     elif menu == 0:
#         print("Program selesai !")
#     else:
#         input("Menu tidak tersedia !")


## TAMAT