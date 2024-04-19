## RENCANA 3 SOAL
print()

# # 1 pemilihan sederhana

print("=== KALKULATOR LUAS BANGUN DATAR ===")
jenis = input("Masukkan Bangun datar\t: ")

if jenis.lower() == "persegi":
    sisi = float(input("Masukkan sisi\t\t: "))
    hasil = sisi**2
elif jenis.lower() == "persegi panjang":
    panjang = float(input("Masukkan panjang\t: "))
    lebar = float(input("Masukkan lebar\t\t: "))
    hasil = panjang*lebar
elif jenis.lower() == "segitiga":
    panjang = float(input("Masukkan panjang alas\t: "))
    tinggi = float(input("Masukkan tinggi\t\t: "))
    hasil = (panjang*tinggi)/2
elif jenis.lower() == "trapesium":
    sisi_a = float(input("Masukkan sisi a\t\t: "))
    sisi_b = float(input("Masukkan sisi b\t\t: "))
    tinggi = float(input("Masukkan tinggi\t\t: "))
    hasil = ((sisi_a+sisi_b)/2) * tinggi

print(f"Hasil luas {jenis.lower()}\t: {hasil:.1f}")


jenis = input("\nMasukkan Bangun datar\t: ")

if jenis.lower() == "persegi":
    sisi = float(input("Masukkan sisi\t\t: "))
    hasil = sisi**2
elif jenis.lower() == "persegi panjang":
    panjang = float(input("Masukkan panjang\t: "))
    lebar = float(input("Masukkan lebar\t\t: "))
    hasil = panjang*lebar
elif jenis.lower() == "segitiga":
    panjang = float(input("Masukkan panjang alas\t: "))
    tinggi = float(input("Masukkan tinggi\t\t: "))
    hasil = (panjang*tinggi)/2
elif jenis.lower() == "trapesium":
    sisi_a = float(input("Masukkan sisi a\t\t: "))
    sisi_b = float(input("Masukkan sisi b\t\t: "))
    tinggi = float(input("Masukkan tinggi\t\t: "))
    hasil = ((sisi_a+sisi_b)/2) * tinggi

print(f"Hasil luas {jenis.lower()}\t: {hasil:.1f}")


# # 2 berhubungan ama tipe data majemuk
# print("\n\n=== INPUT DATA PELANGGAN ===")

# nama = input("Masukkan nama\t\t: ")
# layanan = input("Masukkan pilihan layanan: ")
# tujuan = input("Masukkan kota tujuan\t: ")
# paket = int(input("Masukkan jumlah paket\t: "))

# if layanan.lower() == "express":
#     if paket <= 4:
#         kurir = "1 orang kurir motor"
#     elif paket <= 8:
#         kurir = "2 orang kurir motor"
#     elif paket <= 16:
#         kurir = "3 orang kurir motor"
# elif layanan.lower() == "instan":
#     if paket <= 5:
#         kurir = "1 orang kurir mobil"
#     elif paket <= 10:
#         kurir = "2 orang kurir mobil"
#     elif paket <= 15:
#         kurir = "3 orang kurir mobil"
# else:
#     kurir = f"{paket//2} orang kurir motor"
    
# print("\n=== DATA DIRI ===")
# print(f"Nama\t\t: {nama}")
# print(f"Layanan\t\t: {layanan}")
# print(f"Kota tujuan\t: {tujuan}")
# print(f"Jumlah paket\t: {paket}")
# print(f"Kurir\t\t: {kurir}")


# 3 pake match-case, bikin menu
# print("\n\n=== WARUNG MAKAN KINASIH ===")
# print("Menu:")
# print("1. Nasi Briyani\t\tRp 40.000")
# print("2. Kwetiau Goreng\tRp 20.000")
# print("3. Bebek Goreng\t\tRp 25.000")
# print("4. Bebek Geprek\t\tRp 30.000")
# print("5. Bebek Bakar\t\tRp 35.000\n")
# menu = int(input("Masukkan menu pilihan: "))
# jumlah = int(input("Masukkan jumlah: "))

# match menu:
#     case 1:
#         pilih = "Nasi Briyani"
#         total = 40000 * jumlah
#     case 2:
#         pilih = "Kwetiau Goreng"
#         total = 20000 * jumlah
#     case 3:
#         pilih = "Bebek Goreng"
#         total = 25000 * jumlah
#     case 4:
#         pilih = "Bebek Geprek"
#         total = 30000 * jumlah
#     case 5:
#         pilih = "Bebek Bakar"
#         total = 35000 * jumlah

# print("\n=== NOTA PEMBELIAN ===")
# print(f"Menu yang dipilih: {pilih}")
# print(f"Jumlah: {jumlah}")
# print(f"Harga: Rp {total}")

input()
print()