# # Perulangan (for atau while)
# # Demo
while True:
    jumlah = int(input("\nMasukkan jumlah: "))
    for i in range(jumlah):
        print(f"{i+1} sheep...",end="")
    
    isAgain = input("\nHitung lagi (y/n)?: ")
    if isAgain == "n":
        break
print("\nGoodnight...")


# Latihan
# 1
n = int(input("Masukkan batasan: "))
    
for i in range(n):
    if i % 2:
        print((i+1)**2)
    else:
        print((i+1)**3)


# # 2
import os

menu = -1
while menu != 0:
    os.system("cls")
    print("""\nMenu:
1. Nasi Goreng - Rp 25.000"
2. Mie Goreng - Rp 20.000
3. Ayam Goreng - Rp 30.000
4. Ayam Geprek - Rp 35.000
5. Ayam Mozarella - Rp 40.000
0. END""")
    
    menu = int(input("Masukkan menu pilihan: "))

    match menu:
        case 1:
            jumlah = int(input("Masukkan jumlah: "))
            pilih = "Nasi Goreng"
            total = 25000 * jumlah
        case 2:
            jumlah = int(input("Masukkan jumlah: "))
            pilih = "Mie Goreng"
            total = 20000 * jumlah
        case 3:
            jumlah = int(input("Masukkan jumlah: "))
            pilih = "Ayam Goreng"
            total = 30000 * jumlah
        case 4:
            jumlah = int(input("Masukkan jumlah: "))
            pilih = "Ayam Geprek"
            total = 35000 * jumlah
        case 5:
            jumlah = int(input("Masukkan jumlah: "))
            pilih = "Ayam Mozarella"
            total = 40000 * jumlah
        case 0:
            print("Program Selesai!")
            break
        case _:
            input("Menu tidak tersedia!")

    if menu > 5:
        continue
    else:
        print("\nNOTA PEMBELIAN")
        print(f"Menu yang dipilih: {pilih}")
        print(f"Jumlah: {jumlah}")
        print(f"Harga: Rp {total}")
        bayar = int(input("Bayar: Rp "))
        while bayar < total:
            print("Pembayaran kurang !")
            bayar = int(input("Bayar: Rp "))
        
        input(f"Kembalian: Rp {bayar - total}")


# 3
print("\nRock, Paper, Scissors Game!\n")
player1 = input("Masukkan nama pemain 1: ")
player2 = input("Masukkan nama pemain 2: ")
avg_name = (len(player1) + len(player2)) // 2

skor_player1 = 0
skor_player2 = 0

for i in range(avg_name):
    print(f"\n=== Round {i+1} ===")
    tangan1 = input(f"{player1}: ")
    tangan2 = input(f"{player2}: ")

    while tangan1.lower() not in ["batu", "gunting", "kertas"] or \
        tangan2.lower() not in ["batu", "gunting", "kertas"]:
        print("Invalid!")
        tangan1 = input(f"\n{player1}: ")
        tangan2 = input(f"{player2}: ")

    if tangan1.lower() == tangan2.lower():
        print("Imbang !")
    elif(tangan1.lower() == "batu" and tangan2.lower() == "gunting") or \
        (tangan1.lower() == "gunting" and tangan2.lower() == "kertas") or \
        (tangan1.lower() == "kertas" and tangan2.lower() == "batu"):
        print(f"{player1} Menang !")
        skor_player1 += 1
    else:
        print(f"{player2} Menang !")
        skor_player2 += 1

print("\n=== Skor Akhir ===")
print(f"{player1}: {skor_player1}")
print(f"{player2}: {skor_player2}")
print("\nTerima kasih telah bermain !")