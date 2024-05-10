print()
# 1
bilangan = int(input("Masukkan bilangan : "))
print()
for i in range(3,bilangan+1,3):
    print(f"Perulangan ke {i} bernilai kelipatan 3")


# 2
print()
print("="*30)
print("====== Perhitungan Gaji ======")
print("="*30)

urutan = 1
lanjut = 'y'

while lanjut.lower() == 'y':
    nama = input(f"\nMasukkan nama karyawan {urutan}: ")
    urut_bulan = 1
    gaji = 0
    while urut_bulan <=3:
        temp = int(input(f"Masukkan gaji bulan ke {urut_bulan} : Rp "))
        gaji += temp
        urut_bulan += 1
    
    print(f"Gaji rata-rata {nama} adalah Rp {float(gaji/3):.2f}")
    urutan += 1
    lanjut = input("\nLanjut (y/n)? ")

print("Program selesai!\n\n")

# 3
genap = 0
ganjil = 0

for i in range(5):
    angka = int(input(f"Masukkan nilai bilangan ke {i+1} : "))
    while angka <= 0:
        print("Nilai wajib diatas 0!\n")
        angka = int(input(f"Masukkan nilai bilangan ke {i+1} : "))
    
    if angka % 2 == 0:
        genap += 1
    else:
        ganjil +=1

print("="*32)
print(f"Jumlah bilangan ganjil : {ganjil}")
print(f"Jumlah bilangan genap  : {genap}")
input()