## RENCANA 3 SOAL
print()

# 1 ttg BMI, pemilihan sederhana

print("=== BODY MASS INDEX ===")
berat = float(input("Masukkan berat (kg): "))
tinggi = float(input("Masukkan tinggi (m): "))

bmi = berat / tinggi**2

if bmi <= 18.5:
    print("Underweight")
elif bmi <= 25.0:
    print("Normal")
elif bmi <= 30.0:
    print("Overweight")
elif bmi > 30:
    print("Obese")


# 2 berhubungan ama tipe data majemuk
# plan -> pemilihan berdasarkan jumlah barang dimasukkan ke brp koper
print("\n\n=== INPUT DATA DIRI ===")

nama = input("Masukkan nama\t\t: ")
transportasi = input("Masukkan transportasi\t: ")
asal = input("Masukkan kota asal\t: ")
tujuan = input("Masukkan kota tujuan\t: ")
barang = input("Masukkan barang bawaan\t: ")
jumlah_barang = len(barang.split())

if transportasi.lower() == "kereta":
    if jumlah_barang <= 2:
        koper = "1 koper kecil"
    elif jumlah_barang <= 4:
        koper = "2 koper kecil"
    elif jumlah_barang <= 6:
        koper = "3 koper kecil"
elif transportasi.lower() == "pesawat":
    if jumlah_barang <= 3:
        koper = "1 koper besar"
    elif jumlah_barang <= 6:
        koper = "2 koper besar"
    elif jumlah_barang <= 9:
        koper = "3 koper besar"
else:
    koper = f"{jumlah_barang} koper sedang"
    
print("\n=== DATA DIRI ===")
print(f"Nama\t\t: {nama}")
print(f"Transportasi\t: {transportasi}")
print(f"Kota asal\t: {asal}")
print(f"Kota tujuan\t: {tujuan}")
print(f"Barang\t\t: {barang}")
print(f"Koper\t\t: {koper}")


# 3 pake match-case, bikin menu
print("\n\n=== WARUNG MAKAN KINASIH ===")
print("Menu:")
print("1. Nasi Goreng\t\tRp 25.000")
print("2. Mie Goreng\t\tRp 20.000")
print("3. Ayam Goreng\t\tRp 30.000")
print("4. Ayam Geprek\t\tRp 35.000")
print("5. Ayam Mozarella\tRp 40.000\n")
menu = int(input("Masukkan menu pilihan: "))
jumlah = int(input("Masukkan jumlah: "))

match menu:
    case 1:
        pilih = "Nasi Goreng"
        total = 25000 * jumlah
    case 2:
        pilih = "Mie Goreng"
        total = 20000 * jumlah
    case 3:
        pilih = "Ayam Goreng"
        total = 30000 * jumlah
    case 4:
        pilih = "Ayam Geprek"
        total = 35000 * jumlah
    case 5:
        pilih = "Ayam Mozarella"
        total = 40000 * jumlah

print("\n=== NOTA PEMBELIAN ===")
print(f"Menu yang dipilih: {pilih}")
print(f"Jumlah\t\t : {jumlah}")
print(f"Harga\t\t : Rp {total}")
bayar = float(input("Masukkan uang\t : Rp "))
print(f"Kembalian\t : Rp {bayar-total}")

input()
print()