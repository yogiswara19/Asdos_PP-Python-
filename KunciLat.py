list_barang = ["HP","Laptop","Kacamata"]
data = {
    "nama" : "Ucup",
    "npm" : "232499085",
    "list_barang" : list_barang
}
print("Data")
print(f"Nama\t: {data["nama"]}")
print(f"NPM\t: {data["npm"]}")
print("Barang\t: ")
for i in list_barang:
    print(f"\t - {i}")

# input user
nama_baru = input("\nMasukkan nama baru: ")
npm_baru = input("Masukkan npm baru: ")
barang_baru = input("Masukkan list barang baru: ")

# copy dict + update data
data_baru = data.copy()
data_baru["nama"] = nama_baru
data_baru["npm"] = npm_baru
data_baru["list_barang"] = barang_baru.split()

# output
print("\nData Lama")
print(f"Nama\t: {data["nama"]}")
print(f"NPM\t: {data["npm"]}")
print("Barang\t: ")
for i in data["list_barang"]:
    print(f"\t - {i}")

print("\nData Baru")
print(f"Nama\t: {data_baru["nama"]}")
print(f"NPM\t: {data_baru["npm"]}")
print("Barang\t: ")
for i in data_baru["list_barang"]:
    print(f"\t - {i}")