## B
# # 1
# kalimat = "Universitas Atma Jaya Yogyakarta merupakan salah satu PTS terbaik di Indonesia"

# print(f"Index kelipatan 2 kurang dari 12: {kalimat[0:13:2]}")
# print(f"string a ada di kalimat: {"a" in kalimat}")
# print(f"Paling besar: {max(kalimat)}")
# print(f"Paling kecil: {min(kalimat)}")
# print(f"Panjang karakter: {len(kalimat)}")
# print(f"Diakhiri dengan kata 'Indonesia': {kalimat.endswith("Indonesia")}")

# # 2
# kalimat = "iphone adalah salah satu merk handphone terbesar di dunia"
# print(f"\nsemua karakter string berhuruf besar: {kalimat.isupper()}")
# print(f"kalimat bisa dicetak: {kalimat.isprintable()}")
# print(f"hanya memiliki white space: {kalimat.isspace()}")

# # 3
# import datetime as dt

# # input
# tanggal = int(input("\nTanggal\t: "))
# bulan = int(input("Bulan\t: "))
# tahun = int(input("Tahun\t: "))

# # proses
# lahir = dt.date(tahun,bulan,tanggal)
# print(f"tanggal lahir\t: {lahir}")
# print(f"hari lahir\t: {lahir:%A}")

# hari_ini = dt.date.today()
# print(f"tanggal hari ini: {hari_ini}")
# umur_hari = hari_ini - lahir
# umur_tahun = umur_hari.days // 365
# umur_bulan = (umur_hari.days % 365) // 30
# print(f"umur sekarang\t: {umur_tahun} tahun, {umur_bulan} bulan")


## A
# # 1
# kalimat = "samsung adalah salah satu brand handphone paling populer di dunia"

# print(f"Index ke 26-30\t: {kalimat[26:31]}")
# print(f"Paling besar: {max(kalimat)}")
# print(f"Paling kecil: {min(kalimat)}")
# print(f"String i ada di kalimat: {"i" in kalimat}")
# print(f"Panjang karakter: {len(kalimat)}")
# print(f"Kalimat diawali dengan kata 'populer': {kalimat.startswith("populer")}")

# # 2
# kalimat = "iphone adalah salah satu merk handphone terbesar di dunia"
# print(f"\nsemua karakter string berhuruf kecilr: {kalimat.islower()}")
# print(f"kalimat bersifat alfanumerik: {kalimat.isalnum()}")
# print(f"setiap kata diawali dengan huruf kapital: {kalimat.istitle()}")

# # 3
# import datetime as dt

# # input
# tanggal = int(input("\nTanggal\t: "))
# bulan = int(input("Bulan\t: "))
# tahun = int(input("Tahun\t: "))

# # proses
# lahir = dt.date(tahun,bulan,tanggal)
# print(f"tanggal lahir\t: {lahir}")
# print(f"hari lahir\t: {lahir:%A}")

# hari_ini = dt.date.today()
# print(f"tanggal hari ini: {hari_ini}")
# umur_hari = hari_ini - lahir
# umur_tahun = umur_hari.days // 365
# umur_bulan = (umur_hari.days % 365) // 30
# print(f"umur sekarang\t: {umur_tahun} tahun, {umur_bulan} bulan")