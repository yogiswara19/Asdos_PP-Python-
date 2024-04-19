## RENCANA 3 SOAL
print()

# # 1 pemilihan sederhana

print("=== KALKULATOR VOLUME BANGUN RUANG ===")
jenis = input("Masukkan Bangun Ruang\t: ")

if jenis.lower() == "kubus":
    rusuk = float(input("Masukkan panjang rusuk\t: "))
    hasil = rusuk**3
elif jenis.lower() == "balok":
    panjang = float(input("Masukkan panjang balok\t: "))
    lebar = float(input("Masukkan lebar balok\t: "))
    tinggi = float(input("Masukkan tinggi balok\t: "))
    hasil = panjang*lebar*tinggi
elif jenis.lower() == "tabung":
    phi = 3.14
    jari = float(input("Masukkan jari-jari tabung\t: "))
    tinggi = float(input("Masukkan tinggi tabung\t: "))
    hasil = phi*(jari**2)*tinggi
elif jenis.lower() == "kerucut":
    phi = 3.14
    jari = float(input("Masukkan jari-jari kerucut\t: "))
    tinggi = float(input("Masukkan tinggi kerucut\t: "))
    hasil = (1/3)*phi*(jari**2)*tinggi

print(f"Hasil volume {jenis.lower()}\t: {hasil:.1f}")


# jenis = input("\nMasukkan Bangun Ruang\t: ")

# if jenis.lower() == "kubus":
#     rusuk = float(input("Masukkan panjang rusuk\t: "))
#     hasil = rusuk**3
# elif jenis.lower() == "balok":
#     panjang = float(input("Masukkan panjang balok\t: "))
#     lebar = float(input("Masukkan lebar balok\t: "))
#     tinggi = float(input("Masukkan tinggi balok\t: "))
#     hasil = panjang*lebar*tinggi
# elif jenis.lower() == "tabung":
#     phi = 3.14
#     jari = float(input("Masukkan jari-jari tabung\t: "))
#     tinggi = float(input("Masukkan tinggi tabung\t: "))
#     hasil = phi*(jari**2)*tinggi
# elif jenis.lower() == "kerucut":
#     phi = 3.14
#     jari = float(input("Masukkan jari-jari tabung\t: "))
#     tinggi = float(input("Masukkan tinggi tabung\t: "))
#     hasil = (1/3)*phi*(jari**2)*tinggi

# print(f"Hasil volume {jenis.lower()}\t: {hasil:.1f}")


# 2 berhubungan ama tipe data majemuk
# print("\n\n=== INPUT DATA PELANGGAN ===")

# nama = input("Masukkan nama\t\t: ")
# transportasi = input("Masukkan jenis mobil\t: ")
# jemput = input("Masukkan tempat penjemputan\t: ")
# antar = input("Masukkan tempat pengantaran\t: ")
# jarak = int(input("Masukkan jarak tempuh(km)\t: "))

# if transportasi.lower() == "besar":
#     if jarak <= 2:
#         hasil = jarak*150000
#     elif jarak <= 5:
#         hasil = jarak*125000
#     elif jarak <= 8:
#         hasil = jarak*100000
# elif transportasi.lower() == "kecil":
#     if jarak <= 3:
#         hasil = jarak*100000
#     elif jarak <= 6:
#         hasil = jarak*75000
#     elif jarak <= 9:
#         hasil = jarak*50000
# else:
#     hasil = jarak*200000
    
# print("\n=== DATA DIRI ===")
# print(f"Nama\t\t: {nama}")
# print(f"Transportasi\t: {transportasi.lower()}")
# print(f"Tempat jemput\t: {jemput}")
# print(f"Tempat antar\t: {antar}")
# print(f"Jarak tempuh\t: {jarak} Km")
# print(f"Harga\t\t: Rp {hasil}")


# 3 pake match-case, bikin menu
# print("\n\n=== WARUNG MAKAN KINASIH ===")
# print("Menu:")
# print("1. Nasi Tongseng\tRp 35.000")
# print("2. Mie Tek-Tek\t\tRp 25.000")
# print("3. Ayam Kecap\t\tRp 20.000")
# print("4. Ayam Gulai\t\tRp 30.000")
# print("5. Ayam Suwir\t\tRp 22.000\n")
# menu = int(input("Masukkan menu pilihan: "))
# jumlah = int(input("Masukkan jumlah: "))

# match menu:
#     case 1:
#         pilih = "Nasi Tongseng"
#         total = 35000 * jumlah
#     case 2:
#         pilih = "Mie Tek-Tek"
#         total = 25000 * jumlah
#     case 3:
#         pilih = "Ayam Kecap"
#         total = 20000 * jumlah
#     case 4:
#         pilih = "Ayam Gulai"
#         total = 30000 * jumlah
#     case 5:
#         pilih = "Ayam Suwir"
#         total = 22000 * jumlah

# print("\n=== NOTA PEMBELIAN ===")
# print(f"Menu yang dipilih: {pilih}")
# print(f"Jumlah: {jumlah}")
# print(f"Harga: Rp {total}")

input()
print()