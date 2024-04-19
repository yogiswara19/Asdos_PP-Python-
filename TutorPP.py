# 07/02 '24

## var dkk
# 2 
# nama_peserta = input("Nama Peserta: ")
# umur_peserta = int(input("Umur Peserta: "))
# alamat_peserta = input("Alamat Peserta: ")

# print(f"""\nNama Peserta: {nama_peserta}
# Umur Peserta: {umur_peserta}
# Alamat Peserta: {alamat_peserta}""")

# 3
# X = 7.1
# A = 731
# C = 2

# print(type(int(X)))
# print(str(A))
# print(bool(C))

# x = "hello, world, apa kabar, kalian?"
# print(x.split(",",2))
# print(x.split(",",1))


## string
# 1
# print("""Saya
# adalah
# anak
# sistem
# informasi""")

# 2
# a = "Greg yogi"
# b = "   greg yogi "

# print(a.upper())
# print(a.lower())
# print(b.strip())
# print(a.replace("Greg","Gregorius"))
# print(a + "" + b)

# 3
# c = "greg yogi"
# print(f"Nama saya: {c.capitalize()}")


# data_mahasiwa = {
#     'MAH01':'Saya',
#     'MAH02':'Dia',
#     'MAH03':'Kalian'
# }

# for mahasiswa, value in data_mahasiwa.items():
#     print(mahasiswa)
#     print(value)

## Fungsi 12/02 '24
# Latihan
# 1
# import os
# i = 3
# cek = 0

# def pageLogin():
#     global i
#     os.system("cls")
#     print("======== Page Login ========\n")
#     while True:
#         inputUser = input("Masukkan username: ")
#         inputPass = input("Masukkan password: ")
#         print("----------------------------")
#         log = cekLogin(inputUser, inputPass)
#         if log == True:
#             input("Login berhasil!")
#             break
#         else:
#             print("Username atau password salah!")
#             i -= 1
#             if i != 0 :
#                 print(f"Kesempatan login Anda tersisa : {i}\n")
#             else:
#                 input("Kesempatan login Anda habis")
#                 return 0
       
# def cekLogin(inputUser, inputPass):
#     user = "11087"
#     passw = "1234"

#     if inputUser == user and inputPass == passw:
#         return True
#     else:
#         return False

# # def find_max(angka1, angka2, angka3, angka4):
# #     return max(angka1,angka2,angka3,angka4)

# # def find_min(angka1, angka2, angka3, angka4):
# #     return min(angka1,angka2,angka3,angka4)

# # def menu2():
#     angka1 = int(input("\nMasukkan angka pertama: "))
#     angka2 = int(input("Masukkan angka kedua: "))
#     angka3 = int(input("Masukkan angka ketiga: "))
#     angka4 = int(input("Masukkan angka keempat: "))
#     print(f"\nNilai terbesar:\t {find_max(angka1, angka2, angka3, angka4)}")
#     input(f"Nilai terkecil:\t {find_min(angka1, angka2, angka3, angka4)}")


# while True:
#     os.system("cls")
#     print("""====== Program Pembantaian Asdos ======
# 1. Login
# 2. Cari Angka
# 0. EXIT
# =======================================""")
#     menu = int(input("Pilih menu: "))

#     match menu:
#         case 1:
#             if cek == 0:
#                 log = pageLogin()
#                 if log == 0:
#                     break
#                 else:
#                     cek = 1
#             else:
#                 input("Anda sudah login!")
#         case 2:
#             if cek == 1:
#                 menu2()
#             else:
#                 input("Harap Login!")
#         case 0:
#             print("Program selesai!")
#             break
#         case _:
#             input("Menu tidak tersedia!")


# 2
# goreng = 0
# bakar = 0
# gurame = 0
# teh = 0
# kelamud = 0
# jeruk = 0

# def page1():
#     i = 0
#     cek = False
#     while True:
#         os.system("cls")
#         print("""====== Program Pembantaian Asdos 2 ======
# 1. Input Pesanan
# 2. Pembayaran
# 0. Kembali
# =========================================""")
#         menu1 = int(input("Pilih menu: "))

#         match menu1:
#             case 1:
#                 if i == 0:
#                     os.system("cls")
#                     cek = pageFood()
#                     if cek == True:
#                         pageDrink()
#                     i = 1
#                 else:
#                     input("Silahkan bayar dahulu!")
#             case 2:
#                 if i == 1:
#                     if cek == False:
#                         pagePurchase()
#                     else:
#                         pagePurchaseDrink()
#                     i = 0
#                 else:
#                     input("Silahkan pesan dahulu!")
#             case 0:
#                 print("Program selesai!")
#                 break
#             case _:
#                 input("Menu tidak tersedia!")

# def pageFood():
#     global goreng, bakar, gurame
#     print("="*40)
#     print("Input Pesanan")
#     print("="*40)
#     print("""1. Paket Ayam Goreng
# 2. Paket Ayam Bakar
# 3. Paket Gurame""")
#     print("="*40)
#     print("Masukkan pesanan makanan Anda:")
#     goreng = int(input("Ayam Goreng Kremes\t: "))
#     bakar = int(input("Ayam Bakar Madu\t\t: "))
#     gurame = int(input("Gurame Sedap Malam\t: "))
#     minum = input("\nMau nambah minum? (y/n) : ")
#     if minum.lower() == "n":
#         return False #klo nggk minum
#     else:
#         return True

# def pageDrink():
#     global teh, kelamud, jeruk
#     print()
#     print("="*40)
#     print("Input Minuman")
#     print("="*40)
#     print("""1. Es Teh Manis
# 2. Es Kelapa Muda
# 3. Es Jeruk Susu""")
#     print("="*40)
#     print("Masukkan pesanan minuman Anda:")
#     teh = int(input("Es Teh Manis\t: "))
#     kelamud = int(input("Es Kelapa Muda\t: "))
#     jeruk = int(input("Es Jeruk Susu\t: "))

# def pagePurchase():
#     os.system("cls")
#     print("="*40)
#     print("Pembayaran")
#     print("="*40)
#     print(f"Total Harga\t\t: Rp {totalMakan()}")
#     print("="*40)
#     uang = int(input("Masukkan uang\t\t: Rp "))
#     while uang < totalMakan():
#         print("Uang anda kurang!")
#         uang = int(input("\nMasukkan uang\t\t: Rp "))
#     print("="*40)
#     print(f"Uang kembalian\t\t: Rp {uang - totalMakan()}")
#     print("="*40)
#     input("\nTerima kasih, Selamat makan!")

# def pagePurchaseDrink():
#     os.system("cls")
#     print("="*40)
#     print("Pembayaran")
#     print("="*40)
#     print(f"Subtotal Makan\t\t: Rp {totalMakan()}")
#     print(f"Subtotal Minum\t\t: Rp {totalMinum()}")
#     print("="*40)
#     print(f"Total Harga\t\t: Rp {totalMakan()+totalMinum()}")
#     print("="*40)
#     uang = int(input("Masukkan uang\t\t: Rp "))
#     while uang < (totalMakan()+totalMinum()):
#         print("Uang anda kurang!")
#         uang = int(input("\nMasukkan uang\t\t: Rp "))
#     print("="*40)
#     print(f"Uang kembalian\t\t: Rp {uang - (totalMakan()+totalMinum())}")
#     print("="*40)
#     input("\nTerima kasih, Selamat makan!")

# def totalMakan():
#     global goreng, bakar, gurame
#     return (goreng * 32000) + (bakar * 34000) + (gurame * 37000)

# def totalMinum():
#     global teh, kelamud, jeruk
#     return (teh * 5000) + (kelamud * 18500) + (jeruk * 15500)

# while True:
#     os.system("cls")
#     print("""====== Program Pembantaian Asdos 2 ======
# 1. Login
# 0. EXIT
# =========================================""")
#     menu = int(input("Pilih menu: "))

#     match menu:
#         case 1:
#             if cek == 0:
#                 log = pageLogin()
#                 if log == 0:
#                     break
#                 else:
#                     cek = 1
#                     page1()
#             else:
#                 input("Anda sudah login!")
#         case 0:
#             print("Program selesai!")
#             break
#         case _:
#             input("Menu tidak tersedia!")



## Class
# class Kucing:
#     def __init__(self, warna, usia):
#         self.warna = warna
#         self.usia = usia

#     def bersuara(self):
#         print(f"Meow!, Kucing ini berwarna {self.warna} dan berusia {self.usia}")

# # Instance dari class Kucing
# obj = Kucing
# kucing_kesayangan = obj(warna="hitam", usia=3)

# # panggil method pada instance
# kucing_kesayangan.bersuara()


## Latihan
# import os

# class TokoBuah:
#     def __init__(self):
#         self.daftar_buah = {}

#     def tambah_buah(self, nama, harga):
#         self.daftar_buah[nama] = harga

#     def tampilkan_daftar_buah(self):
#         print("Daftar Buah di Toko:")
#         for nama, harga in self.daftar_buah.items():
#             print(f"{nama}: Rp {harga}")

#     def hapus_buah(self, nama):
#         if nama in self.daftar_buah:
#             del self.daftar_buah[nama]
#             print(f"{nama} berhasil dihapus dari daftar buah.")
#         else:
#             print(f"{nama} tidak ditemukan dalam daftar buah.")

#     def hitung_total_harga(self, belanjaan):
#         total_harga = 0
#         for nama, jumlah in belanjaan.items():
#             if nama in self.daftar_buah:
#                 total_harga += self.daftar_buah[nama] * jumlah
#             else:
#                 print(f"{nama} tidak tersedia di toko.")
#         return total_harga


# toko_buah = TokoBuah()
# while True:
#     os.system("cls")
#     print("""\nMenu
# 1. Tambah Buah
# 2. Tampilkan Daftar Buah
# 3. Hapus Buah
# 4. Hitung Total Harga Belanjaan
# 0. Keluar""")

#     pilihan = input("Masukkan pilihan Anda: ")

#     if pilihan == "1":
#         nama_buah = input("Masukkan nama buah: ")
#         harga_buah = int(input("Masukkan harga buah: "))
#         toko_buah.tambah_buah(nama_buah, harga_buah)
#         input(f"{nama_buah} berhasil ditambahkan ke dalam daftar buah.")

#     elif pilihan == "2":
#         toko_buah.tampilkan_daftar_buah()
#         input()

#     elif pilihan == "3":
#         nama_buah = input("Masukkan nama buah yang ingin dihapus: ")
#         toko_buah.hapus_buah(nama_buah)
#         input()

#     elif pilihan == "4":
#         belanjaan = {}
#         while True:
#             nama_buah = input("\nMasukkan nama buah yang ingin dibeli (kosongkan untuk selesai): ")
#             if not nama_buah:
#                 break
#             jumlah = int(input(f"Masukkan jumlah {nama_buah} yang ingin dibeli: "))
#             belanjaan[nama_buah] = jumlah

#         total_harga = toko_buah.hitung_total_harga(belanjaan)
#         input(f"Total harga belanjaan: Rp {total_harga}")

#     elif pilihan == "0":
#         print("Terima kasih telah menggunakan layanan kami.")
#         break

#     else:
#         input("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


## GUI
# Demo
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# def Perkenalan(namaDepan_var, namaBelakang_var):
#     frame = ttk.Frame(win)
#     frame.pack(padx=10, pady=10, fill="x", expand=True)

#     namaDepan_label = ttk.Label(frame, text="Masukkan nama depan")
#     namaDepan_label.pack(padx=10, pady=10)
#     namaDepan_entry = ttk.Entry(frame, textvariable=namaDepan_var)
#     namaDepan_entry.pack(fill="x", expand=True)

#     namaBelakang_label = ttk.Label(frame, text="Masukkan nama belakang")
#     namaBelakang_label.pack(padx=10, pady=10)
#     namaBelakang_entry = ttk.Entry(frame, textvariable=namaBelakang_var)
#     namaBelakang_entry.pack(fill="x", expand=True)

#     btn = ttk.Button(frame, text="Perkenalan", command=lambda:tombolSapa(namaDepan_var, namaBelakang_var))
#     btn.pack(pady=10, fill="x", expand=True)

# def tombolSapa(namaDepan_var, namaBelakang_var):
#     if namaDepan_var.get() == "" or namaBelakang_var.get() == "":
#         messagebox.showerror(title="Error", message="Nama depan & belakang wajib diisi")
#     else:
#         messagebox.showinfo(title="Success", message=f"Halo {namaDepan_var.get()} {namaBelakang_var.get()}, Salam kenal")
#         namaDepan_var.set("")
#         namaBelakang_var.set("")


# win = tk.Tk()
# win.configure(bg="white")
# win.geometry('300x300')
# win.title("Halaman Perkenalan")
# namaDepan = tk.StringVar()
# namaBelakang = tk.StringVar()

# Perkenalan(namaDepan, namaBelakang)
# win.mainloop()

# Latihan
# gpt w/ class
# import tkinter as tk

# class Calculator:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Simple Calculator")
#         self.entry = tk.Entry(master, width=30, borderwidth=5)
#         self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#         self.create_buttons()

#     def create_buttons(self):
#         buttons = [
#             ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#             ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#             ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#             ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
#         ]

#         for (text, row, col) in buttons:
#             button = tk.Button(self.master, text=text, padx=20, pady=10, command=lambda t=text: self.button_click(t))
#             button.grid(row=row, column=col)

#     def button_click(self, value):
#         current = self.entry.get()

#         if value == 'C':
#             self.entry.delete(0, tk.END)
#         elif value == '=':
#             try:
#                 result = eval(current)
#                 self.entry.delete(0, tk.END)
#                 self.entry.insert(tk.END, str(result))
#             except Exception as e:
#                 self.entry.delete(0, tk.END)
#                 self.entry.insert(tk.END, "Error")
#         else:
#             self.entry.insert(tk.END, value)


# def main():
#     root = tk.Tk()
#     calculator = Calculator(root)
#     root.mainloop()


# if __name__ == "__main__":
#     main()

# gpt
import tkinter as tk

# Fungsi
def button_click(value):
    current = entry.get()

    if value == 'C':
        entry.delete(0, tk.END)
    elif value == '=':
        result = str(eval(current))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    else:
        entry.insert(tk.END, value)


# Tampilan
root = tk.Tk()
root.title("Kalkulator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

root.mainloop()
