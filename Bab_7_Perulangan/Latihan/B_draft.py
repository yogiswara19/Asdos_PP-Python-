print()
# 1
bilangan = int(input("Masukkan bilangan : "))
print()
for i in range(1,bilangan+1):
    if i % 2 == 0:
        print(f"Perulangan ke {i} bernilai genap")


# 2
print()
print("="*31)
print("===== Penilaian Mahasiswa =====")
print("="*31)

urutan = 1
lanjut = 'y'

while lanjut.lower() == 'y':
    nama = input(f"\nMasukkan nama mahasiswa {urutan}: ")
    semester = 1
    nilai = 0
    while semester <=4:
        temp = float(input(f"Masukkan IP Semester {semester} : "))
        nilai += temp
        semester += 1
    
    print("="*31)
    print(f"IPK sementara {nama} adalah {nilai/4:.2f}")
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