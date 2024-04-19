# Data majemuk (list,tuples,sets,dict)
# print()

## 1
# list
# print("\nLIST")
# buah_list = ["apel", "jeruk"]
# print(f"Isi list buah: {buah_list}")
# print(f"Urutan ke 2 adalah buah: {buah_list[1]}")

# set
# print("\nSET")
# barang_dapur_set = {"piring", "sendok"}

# print(f"Set barang dapur: {barang_dapur_set}")

# barang_dapur_set.add("mangkok")

# print(f"Set barang dapur setelah penambahan: \n{barang_dapur_set}")

# tuple
# print("\nTUPLE")
# produk1 = ("Processor", 10000000, 10)
# produk2 = ("Keyboard", 500000, 5)

# print(f"Informasi produk 1: {produk1}")

# dict
# print("\nNESTED DICTIONARY")
# katalog_buku = {
#     "BK001": {"judul": "Python Programming", "penulis": "John Doe"},
#     "BK002": {"judul": "Data Science Handbook", "penulis": "Jane Smith"},
# }

# kode_unik = "BK002"
# print(f"""Informasi tentang buku dengan kode {kode_unik}: 
#     Judul: {katalog_buku[kode_unik]['judul']}
#     Penulis: {katalog_buku[kode_unik]['penulis']}""")

# print()

## 2
# list_barang = ["HP","Laptop","Kacamata"]
# data = {
#     "nama" : "Ucup",
#     "npm" : "232499085",
#     "list_barang" : list_barang
# }
# print("Data")
# print(f"Nama\t: {data["nama"]}")
# print(f"NPM\t: {data["npm"]}")
# print("Barang\t: ")
# for i in list_barang:
#     print(f"\t - {i}")


# nama_baru = input("\nMasukkan nama baru: ")
# npm_baru = input("Masukkan npm baru: ")
# barang_baru = input("Masukkan list barang baru: ")

# data_baru = data.copy()
# data_baru["nama"] = nama_baru
# data_baru["npm"] = npm_baru
# data_baru["list_barang"] = barang_baru.split()

# # output
# print("\nData Lama")
# print(f"Nama\t: {data["nama"]}")
# print(f"NPM\t: {data["npm"]}")
# print("Barang\t: ")
# for i in data["list_barang"]:
#     print(f"\t - {i}")

# print("\nData Baru")
# print(f"Nama\t: {data_baru["nama"]}")
# print(f"NPM\t: {data_baru["npm"]}")
# print("Barang\t: ")
# for i in data_baru["list_barang"]:
#     print(f"\t - {i}")

# print()


# Pemilihan (if...else)
# Demo
# nama = input("Masukkan nama: ")

# if nama.lower()[0] == "r":
#     print(f"{nama} bermain gitar")
# else:
#     print(f"{nama} tidak bermain gitar")


# Lat
# print()

# berat = float(input("Masukkan berat (kg): "))
# tinggi = float(input("Masukkan tinggi (m): "))

# bmi = berat / tinggi**2

# if bmi <= 18.5:
#     print("Underweight")
# elif bmi <= 25.0:
#     print("Normal")
# elif bmi <= 30.0:
#     print("Overweight")
# elif bmi > 30:
#     print("Obese")

# TAMBAH 1 TTG MENU PAKE MATCH
# print("\nMenu:")
# print("1. Nasi Goreng - Rp 25.000")
# print("2. Mie Goreng - Rp 20.000")
# print("3. Ayam Goreng - Rp 30.000")
# print("4. Ayam Geprek - Rp 35.000")
# print("5. Ayam Mozarella - Rp 40.000")
# menu = int(input("Masukkan menu pilihan: "))
# jumlah = int(input("Masukkan jumlah: "))

# match menu:
#     case 1:
#         pilih = "Nasi Goreng"
#         total = 25000 * jumlah
#     case 2:
#         pilih = "Mie Goreng"
#         total = 20000 * jumlah
#     case 3:
#         pilih = "Ayam Goreng"
#         total = 30000 * jumlah
#     case 4:
#         pilih = "Ayam Geprek"
#         total = 35000 * jumlah
#     case 5:
#         pilih = "Ayam Mozarella"
#         total = 40000 * jumlah

# print("\nNOTA PEMBELIAN")
# print(f"Menu yang dipilih: {pilih}")
# print(f"Jumlah: {jumlah}")
# print(f"Harga: Rp {total}")

# print()


# Perulangan (for atau while)
# Demo
# def count_sheep(n):
#     # your code
#     for i in range(n):
#         print(f"{i+1} sheep...",end="")

# print(count_sheep(2))

# while True:
#     jumlah = int(input("\nMasukkan jumlah: "))
#     for i in range(jumlah):
#         print(f"{i+1} sheep...",end="")
    
#     isAgain = input("\nHitung lagi (y/n)?: ")
#     if isAgain == "n":
#         break
# print("\nGoodnight...")


# Lat
# print()

# n = int(input("Masukkan batasan: "))
    
# for i in range(n):
#     if i % 2:
#         print((i+1)**2)
#     else:
#         print((i+1)**3)

# TAMBAH 1 LANJUTAN MENU -while
# import os

# menu = -1
# while menu != 0:
#     os.system("cls")
#     print("Menu:")
#     print("1. Nasi Goreng - Rp 25.000")
#     print("2. Mie Goreng - Rp 20.000")
#     print("3. Ayam Goreng - Rp 30.000")
#     print("4. Ayam Geprek - Rp 35.000")
#     print("5. Ayam Mozarella - Rp 40.000")
#     print("0. END")
#     menu = int(input("Masukkan menu pilihan: "))

#     match menu:
#         case 1:
#             jumlah = int(input("Masukkan jumlah: "))
#             pilih = "Nasi Goreng"
#             total = 25000 * jumlah
#         case 2:
#             jumlah = int(input("Masukkan jumlah: "))
#             pilih = "Mie Goreng"
#             total = 20000 * jumlah
#         case 3:
#             jumlah = int(input("Masukkan jumlah: "))
#             pilih = "Ayam Goreng"
#             total = 30000 * jumlah
#         case 4:
#             jumlah = int(input("Masukkan jumlah: "))
#             pilih = "Ayam Geprek"
#             total = 35000 * jumlah
#         case 5:
#             jumlah = int(input("Masukkan jumlah: "))
#             pilih = "Ayam Mozarella"
#             total = 40000 * jumlah
#         case 0:
#             print("Program Selesai!")
#             break
#         case _:
#             input("Menu tidak tersedia!")

#     if menu > 5:
#         continue
#     else:
#         print("\nNOTA PEMBELIAN")
#         print(f"Menu yang dipilih: {pilih}")
#         print(f"Jumlah: {jumlah}")
#         print(f"Harga: Rp {total}")
#         bayar = int(input("Bayar: Rp "))
#         while bayar < total:
#             print("Pembayaran kurang !")
#             bayar = int(input("Bayar: Rp "))
        
#         input(f"Kembalian: Rp {bayar - total}")


# TAMBAH 1 TTG ROCK PAPER SCISSORS -for/while
# original
# player1 = input("Masukkan nama pemain 1: ")
# player2 = input("Masukkan nama pemain 2: ")
# avg_name = (len(player1) + len(player2)) // 2

# for i in range(avg_name):
#     print(f"\nRound {i+1}")
#     tangan1 = input(f"{player1}: ")
#     tangan2 = input (f"{player2}: ")

#     while tangan1.lower() != "batu" or tangan1.lower() != "gunting" or tangan1.lower() != "kertas" or tangan2.lower() != "batu" or tangan2.lower() != "gunting" or tangan2.lower() != "kertas":
#         print("Invalid!")
#         tangan1 = input(f"\n{player1}: ")
#         tangan2 = input (f"{player2}: ")
#         if tangan1.lower() == "batu" or tangan1.lower() == "gunting" or tangan1.lower() == "kertas" or tangan2.lower() == "batu" or tangan2.lower() == "gunting" or tangan2.lower() == "kertas":
#             break
#     if tangan1.lower() == "batu":
#         if tangan2.lower() == "batu":
#             print("Imbang !")
#         elif tangan2.lower() == "gunting":
#             print(f"{player1} Menang !")
#         elif tangan2.lower() == "kertas":
#             print(f"{player2} Menang !")
#     elif tangan1.lower() == "gunting":
#         if tangan2.lower() == "batu":
#             print(f"{player2} Menang !")
#         elif tangan2.lower() == "gunting":
#             print("Imbang!")
#         elif tangan2.lower() == "kertas":
#             print(f"{player1} Menang !")
#     elif tangan1.lower() == "kertas":
#         if tangan2.lower() == "batu":
#             print(f"{player1} Menang !")
#         elif tangan2.lower() == "gunting":
#             print(f"{player2} Menang !")
#         elif tangan2.lower() == "kertas":
#             print("Imbang !")

# print("Terima kasih telah bermain !")


# simplified by gpt
# print("\nRock, Paper, Scissors Game!\n")
# player1 = input("Masukkan nama pemain 1: ")
# player2 = input("Masukkan nama pemain 2: ")
# avg_name = (len(player1) + len(player2)) // 2

# skor_player1 = 0
# skor_player2 = 0

# for i in range(avg_name):
#     print(f"\n=== Round {i+1} ===")
#     tangan1 = input(f"{player1}: ")
#     tangan2 = input(f"{player2}: ")

#     while tangan1.lower() not in ["batu", "gunting", "kertas"] or tangan2.lower() not in ["batu", "gunting", "kertas"]:
#         print("Invalid!")
#         tangan1 = input(f"\n{player1}: ")
#         tangan2 = input(f"{player2}: ")

#     if tangan1.lower() == tangan2.lower():
#         print("Imbang !")
#     elif (tangan1.lower() == "batu" and tangan2.lower() == "gunting") or \
#          (tangan1.lower() == "gunting" and tangan2.lower() == "kertas") or \
#          (tangan1.lower() == "kertas" and tangan2.lower() == "batu"):
#         print(f"{player1} Menang !")
#         skor_player1 += 1
#     else:
#         print(f"{player2} Menang !")
#         skor_player2 += 1

# print("\n=== Skor Akhir ===")
# print(f"{player1}: {skor_player1}")
# print(f"{player2}: {skor_player2}")
# print("\nTerima kasih telah bermain !")

# print()