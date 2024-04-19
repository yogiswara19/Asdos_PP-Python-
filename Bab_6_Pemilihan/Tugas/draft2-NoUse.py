# Data login
nama = "yogi"
npm = "11087"

# Membersihkan layar
import os
os.system("cls" if os.name == "nt" else "clear")

# Login
user = input("Masukkan Username: ")
pasw = input("Masukkan Password: ")

if user != nama or pasw != npm:
    print("!! Username dan Password salah !!")
    print("!! Login Gagal !!")
    exit()

# Menampilkan menu
os.system("cls" if os.name == "nt" else "clear")
print(f"Login berhasil. Welcome, {user}!")
print("\n===== TOKO MAS KARNA =====")
print("1. Lenovo")
print("2. Samsung")
print("0. EXIT")
menu = input("\nPilih menu: ")

if menu == '0':
    print("Program keluar...")
    exit()
elif menu not in ['1', '2']:
    print("Menu tidak tersedia!")
    exit()

# os.system("cls" if os.name == "nt" else "clear")

# Menampilkan daftar tablet
if menu == '1':
    print("1. Lenovo Tab 2")
    print("2. Lenovo Tab P11 Pro")
    print("3. Lenovo Legion Y700")
elif menu == '2':
    print("1. Samsung Galaxy Tab S6")
    print("2. Samsung Galaxy Tab S7 FE 5G")
    print("3. Samsung Galaxy Tab S8")

tablet_type = input("Masukkan jenis tablet: ")
if tablet_type not in ['1', '2', '3']:
    print("Pilihan tablet tidak valid!")
    exit()

quantity = int(input("Masukkan jumlah tablet: "))

# Input member
member = input("Masukkan jenis member (Platinum/Diamond/None): ").lower()
if member not in ["platinum", "diamond", "none"]:
    print("Jenis member tidak valid.")
    exit()

if member == "platinum":
    member_index = 1
elif member == "diamond":
    member_index = 2
else:
    member_index = 0

# Perhitungan total dan bonus
prices = {
    '1': [2000000, 5000000, 7500000],
    '2': [3500000, 7000000, 9000000]
}

potongan = {
    '1': [800000, 1600000, 2400000],
    '2': [1500000, 3000000, 4500000]
}

discounts = {
    0: [1, 1, 1],
    1: [0.95, 0.95, 0.95],
    2: [0.90, 0.90, 0.90]
}

bonuses = {
    '1': [
        ["Mendapatkan 2 casing tablet", "Mendapatkan 2 casing tablet", "Mendapatkan 2 casing tablet"],
        ["Mendapatkan 3 casing tablet dan 1 memory card", "Mendapatkan 3 casing tablet dan 1 memory card", "Mendapatkan 3 casing tablet dan 1 memory card"],
        ["Mendapatkan 5 casing tablet, 1 memory card, dan 1 power bank", "Mendapatkan 5 casing tablet, 1 memory card, dan 1 power bank", "Mendapatkan 5 casing tablet, 1 memory card, dan 1 power bank"]
    ],
    '2': [
        ["Mendapatkan 3 casing tablet", "Mendapatkan 3 casing tablet", "Mendapatkan 3 casing tablet"],
        ["Mendapatkan 3 casing tablet dan 2 memory card", "Mendapatkan 3 casing tablet dan 2 memory card", "Mendapatkan 3 casing tablet dan 2 memory card"],
        ["Mendapatkan 5 casing tablet, 2 memory card, dan 2 power bank", "Mendapatkan 5 casing tablet, 2 memory card, dan 2 power bank", "Mendapatkan 5 casing tablet, 2 memory card, dan 2 power bank"]
    ]
}

total = prices[menu][int(tablet_type) - 1] * quantity * discounts[member_index][int(tablet_type) - 1] - potongan[menu][int(tablet_type) - 1]
bonus = bonuses[menu][int(tablet_type) - 1][member_index]

# Output
# os.system("cls" if os.name == "nt" else "clear")
print("\n===== Data Pembelian =====")
print(f"Nama\t\t: {user}")
print(f"Jenis\t\t: {'Lenovo' if menu == '1' else 'Samsung'} {'Tab 2' if tablet_type == '1' else 'Tab P11 Pro' if tablet_type == '2' else 'Legion Y700' if tablet_type == '3' else 'Galaxy Tab S6' if tablet_type == '1' else 'Galaxy Tab S7 FE 5G' if tablet_type == '2' else 'Galaxy Tab S8'}")
print(f"Jumlah\t\t: {quantity} unit")
print(f"Total Harga\t: Rp {total}")
print("-" * 40)
print(bonus)
