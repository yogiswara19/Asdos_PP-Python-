# Data majemuk (list,tuples,sets,dict)
# print()

# list_barang = ["HP","Laptop","Kacamata"]
# data = {
#     "nama" : "Ucup",
#     "npm" : "232499085",
#     "list_barang" : list_barang
# }
# print("Data")
# print(f"Nama\t: {data["nama"]}")
# print(f"NPM\t: {data["npm"]}")
# print(f"Barang\t: {data["list_barang"]}")

# nama_baru = input("\nMasukkan nama baru: ")
# data_baru = data.copy()
# data_baru["nama"] = nama_baru

# print("\nData Lama")
# print(f"Nama\t: {data["nama"]}")
# print(f"NPM\t: {data["npm"]}")
# print(f"Barang\t: {data["list_barang"]}")

# print("\nData Baru")
# print(f"Nama\t: {data_baru["nama"]}")
# print(f"NPM\t: {data_baru["npm"]}")
# print(f"Barang\t: {data_baru["list_barang"]}")

# print()


# Pemilihan (if...else)
# print()

# n = int(input("Masukkan angka: ").strip())

# if n % 2 == 0:
#     if n >= 2 and n <= 5:
#         print("Tidak Baik")
#     if n >= 6 and n <= 20:
#         print("Baik") 
#     if n > 20:
#         print("Tidak Baik")
# else:
#     print("Baik")

# print()


# Perulangan (for atau while)
# print()

# n = int(input("Masukkan batasan: "))
    
# for i in range(n):
#     a = i ** 2
#     print(a)

# print()


# Fungsi
# print()

# def tambah(angka1,angka2):
#     return angka1 + angka2

# def kali(angka1,angka2):
#     return angka1 * angka2

# angka1 = int(input("Masukkan angka 1: "))
# angka2 = int(input("Masukkan angka 2: "))

# hasil1 = tambah(angka1,angka2)
# hasil2 = kali(angka1,angka2)

# print(f"\nHasil penjumlahan: {hasil1}")
# print(f"Hasil perkalian: {hasil2}")

# print()

# n = int(input("Masukkan batasan: "))
    
# if n % 2:
#     for i in range(1,n+4,2):
#         print(i**2,end=" ")
# else:
#     pass