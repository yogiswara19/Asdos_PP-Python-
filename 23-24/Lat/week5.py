## B
# # 1
# print("=== Coffee Shop ===")
# menu = ["Latte", "Cappucino", "Americano", "Espresso", "Luwak"]
# print(f"Daftar Menu: {menu}")

# menu.remove("Americano")
# menu.sort()
# print(f"Daftar Menu Baru: {menu}")
# print(f"Jumlah Menu yang tersedia: {len(menu)}")

# # 2
# print("=== Nilai Mahasiswa ===")
# nilai = (80, 75, 90, 85, 70, 80, 85, 90, 80, 75)
# print(f"Tuple Nila Mahasiswa: {nilai}")

# cari = int(input("Masukkan nilai yang ingin dicari: "))
# print(f"Jumlah kemunculan nilai {cari} adalah: {nilai.count(cari)}")

# # 3
# print("=== Program Hitung Rata-Rata Pendapatan ===")

# cabang_1 = {}
# cabang_2 = {}

# senin_1 = float(input("Masukkan pendapatan hari senin cabang 1\t\t: Rp "))
# selasa_1 = float(input("Masukkan pendapatan hari selasa cabang 1\t: Rp "))
# rabu_1 = float(input("Masukkan pendapatan hari rabu cabang 1\t\t: Rp "))

# cabang_1['senin'] = senin_1
# cabang_1['selasa'] = selasa_1
# cabang_1['rabu'] = rabu_1
# rata_1 = (senin_1+selasa_1+rabu_1)/3

# senin_2 = float(input("\nMasukkan pendapatan hari senin cabang 2\t\t: Rp "))
# selasa_2 = float(input("Masukkan pendapatan hari selasa cabang 2\t: Rp "))
# rabu_2 = float(input("Masukkan pendapatan hari rabu cabang 2\t\t: Rp "))

# cabang_2['senin'] = senin_2
# cabang_2['selasa'] = selasa_2
# cabang_2['rabu'] = rabu_2
# rata_2 = (senin_2+selasa_2+rabu_2)/3

# # print(cabang_1)
# # print(cabang_2)

# print(f"\nSenin cabang 1\t\t: Rp {cabang_1["senin"]} \t Senin cabang 2\t\t: Rp {cabang_2['senin']}")
# print(f"Selasa cabang 1\t\t: Rp {cabang_1["selasa"]} \t Selasa cabang 2\t: Rp {cabang_2['selasa']}")
# print(f"Rabu cabang 1\t\t: Rp {cabang_1["rabu"]} \t Rabu cabang 2\t\t: Rp {cabang_2['rabu']}")
# print(f"Rata-rata cabang 1\t: Rp {rata_1} \t Rata-rata cabang 2\t: Rp {rata_2}")

## A 
# # 1
# print("=== Toko Alat Tulis Pak Joko ===")
# menu = ["Pensil", "Penghapus", "Buku", "Bolpoin"]
# print(f"Daftar Barang: {menu}")

# menu.append("Penggaris")
# menu.sort()
# print(f"Daftar Barang Baru: {menu}")
# print(f"Jumlah Barang yang tersedia: {len(menu)}")

# # 2
# print("=== Sayuran Bu Susi ===")
# nilai = ("Tomat", "Bayam", "Wortel", "Kubis", "Sawi", "Buncis", "Pare", "Terong", "Labu", "Jagung")
# print(f"Tuple Sayuran: {nilai}")

# cari = input("Masukkan sayuran yang ingin dicari: ")
# print(f"Urutan dari sayur {cari} adalah: {nilai.index(cari)+1}")

# # 3
# print("=== Program Pengecekan Tinggi Badan ===")

# cabang_1 = {}
# cabang_2 = {}

# senin_1 = input("Masukkan nama\t: ")
# selasa_1 = input("Masukkan NPM\t: ")
# rabu_1 = int(input("Masukkan Tinggi\t: "))

# cabang_1['senin'] = senin_1
# cabang_1['selasa'] = selasa_1
# cabang_1['rabu'] = rabu_1

# senin_2 = input("\nMasukkan nama\t: ")
# selasa_2 = input("Masukkan NPM\t: ")
# rabu_2 = int(input("Masukkan Tinggi\t: "))

# cabang_2['senin'] = senin_2
# cabang_2['selasa'] = selasa_2
# cabang_2['rabu'] = rabu_2

# print(f"\nNama Siswa 1\t\t:  {cabang_1["senin"]} \t\t Nama Siswa 2\t\t:  {cabang_2['senin']}")
# print(f"NPM Siswa 1\t\t:  {cabang_1["selasa"]} \t\t NPM Siswa 2\t\t:  {cabang_2['selasa']}")
# print(f"Tinggi siswa 1\t\t:  {bool(cabang_1["rabu"]>=160)} \t Tinggi siswa2\t\t:  {bool(cabang_2['rabu']>=160)}")

## C
# # 1
# print("=== Toko Pakaian Bu Wati ===")
# menu = ["Hoodie", "Polo", "Kaos", "Jaket", "Jersey"]
# print(f"Daftar Pakaian: {menu}")

# menu.remove("Jersey")
# menu.append("Kemeja")
# menu.sort()
# print(f"Daftar Pakaian Baru: {menu}")
# print(f"Jumlah Pakaian yang tersedia: {len(menu)}")

# # 2
# print("=== Sayuran Bu Susi ===")
# nilai = (50.3, 40.5, 70.4, 30.1, 15.7, 65.8, 41.9, 66.6, 73.5, 32.7)
# print(f"Tuple Emas: {nilai}")

# cari = float(input("Masukkan berat emas yang ingin dicari: "))
# print(f"Urutan dari emas {cari} adalah: {nilai.index(cari)+1}")

# # 3
# print("=== Program Hitung 2 Volume Balok ===")

# cabang_1 = {}
# cabang_2 = {}

# senin_1 = int(input("Masukkan tinggi balok 1\t\t: "))
# selasa_1 = int(input("Masukkan panjang balok 1\t: "))
# rabu_1 = int(input("Masukkan lebar balok 1\t\t: "))

# cabang_1['senin'] = senin_1
# cabang_1['selasa'] = selasa_1
# cabang_1['rabu'] = rabu_1
# vol_1 = senin_1*selasa_1*rabu_1

# senin_2 = int(input("\nMasukkan tinggi balok 2\t\t: "))
# selasa_2 = int(input("Masukkan panjang balok 2\t: "))
# rabu_2 = int(input("Masukkan lebar balok 2\t\t: "))

# cabang_2['senin'] = senin_2
# cabang_2['selasa'] = selasa_2
# cabang_2['rabu'] = rabu_2
# vol_2 = senin_2*selasa_2*rabu_2

# print(f"\nTinggi Balok 1\t\t:  {cabang_1["senin"]} \t\t Tinggi Balok 2\t\t:  {cabang_2['senin']}")
# print(f"Panjang Balok 1\t\t:  {cabang_1["selasa"]} \t\t Panjang Balok 2\t:  {cabang_2['selasa']}")
# print(f"Lebar Balok 1\t\t:  {cabang_1["rabu"]} \t\t Lebar Balok 2\t\t:  {cabang_2['rabu']}")
# print(f"Volume Balok 1\t\t:  {vol_1} \t\t Volume Balok 2\t\t:  {vol_2}")