print()
# 1
bilangan = int(input("Masukkan bilangan : "))
print("")
for i in range(bilangan+1):
    if i % 2 != 0:
        print(f"Perulangan ke {i} bernilai ganjil")

print()
# 2
print("="*31)
print("======= Penilaian Siswa =======")
print("="*31)

urutan = 1
lanjut = 'y'

while lanjut.lower() == 'y':
    nama = input(f"\nMasukkan nama mahasiswa {urutan}: ")
    urut_nilai = 1
    nilai = 0
    while urut_nilai <=3:
        temp = int(input(f"Masukkan nilai ke {urut_nilai} : "))
        nilai += temp
        urut_nilai += 1
    
    print("="*31)
    print(f"Nilai rata-rata {nama} adalah {float(nilai/3):.1f}")
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

print("="*34)
print(f"Jumlah bilangan ganjil : {ganjil}")
print(f"Jumlah bilangan genap  : {genap}")

input()

# coba = {
#     1:1,
#     2:2
# }
# # print(coba.keys())
# tes = int(input("Angka: "))
# if tes not in coba.keys():
#     print("error pak")
#     exit()