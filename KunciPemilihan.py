# Pemilihan (if...else)
# Demo
nama = input("Masukkan nama: ")

if nama.lower()[0] == "r":
    print(f"{nama} bermain gitar")
else:
    print(f"{nama} tidak bermain gitar")


# Latihan
# 1
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


# 2
print("""\nMenu:
1. Nasi Goreng - Rp 25.000"
2. Mie Goreng - Rp 20.000
3. Ayam Goreng - Rp 30.000
4. Ayam Geprek - Rp 35.000
5. Ayam Mozarella - Rp 40.000""")

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

print("\nNOTA PEMBELIAN")
print(f"Menu yang dipilih: {pilih}")
print(f"Jumlah: {jumlah}")
print(f"Harga: Rp {total}")