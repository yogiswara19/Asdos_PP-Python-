import os
import time
from colorama import init, Fore, Back, Style    

os.system("cls")
print("==== Menu Kasir Bu Mega ====")
print("""
1. Input pesanan
0. EXIT""")
print(20*"=")
pilihan = str(input("Masukkan pilihan menu\t: "))
os.system("clear")
match pilihan :
    case "1": 
        order = {}
        kasir = str(input("Masukkan nama kasir\t: "))
        pelanggan = str(input("Masukkan nama pelanggan\t: "))
        daftar_makanan = {
            "AG" : "Ayam Goreng\t Rp 15.000",
            "AB" : "Ayam Bakar\t Rp 18.500",
            "AM" : "Ayam Madu\t Rp 20.000"
        }
        print("DAFTAR MAKANAN")
        print(daftar_makanan["AG"])
        print(daftar_makanan["AB"])
        print(daftar_makanan["AM"])
        print(20*"-")
        ayam_goreng = int(input("Masukkan jumlah Ayam Goreng\t: "))
        ayam_bakar = int(input("Masukkan jumlah Ayam Bakar\t: "))
        ayam_madu = int(input("Masukkan jumlah Ayam Madu\t: "))
        print(20*"=")
        ask_drink = str(input("Apakah Anda ingin menambah minuman (y/n) : "))
        
        teh = 0
        kopi = 0
        soda = 0
        if ask_drink == "y" :
            minuman = {
            "ET" : "Es Teh\t Rp 4.000",
            "EK" : "Es Kopi\t Rp 5.000",
            "ES" : "Es Soda\t Rp 10.000"}
            print("DAFTAR MINUMAN")
            print(minuman["ET"])
            print(minuman["EK"])
            print(minuman["ES"])
            print(20*"-")
            teh = int(input("Masukkan jumlah Es Teh\t: "))
            kopi = int(input("Masukkan jumlah Es Kopi\t: "))
            soda = int(input("Masukkan jumlah Es Soda\t: "))
            print(20*"=")
        # os.system("clear")
        jumlah = int(input("Masukkan jumlah orang yang makan\t\t: "))
        member = str(input("Masukkan jenis member (gold/diadmond/silver)\t: "))
        order = {
            "ksr" : (f"{kasir}"),
            "plg" : (f"{pelanggan}"),
            "ag" : (f"{ayam_goreng}"),
            "ab" : (f"{ayam_bakar}"),
            "am" : (f"{ayam_madu}"),
            "et" : (f"{teh}"),
            "ek" : (f"{kopi}"),
            "es" : (f"{soda}"),
            "mbr" : (f"{member}"),
        }
        os.system("clear")
        print("===== NOTA PEMBAYARAN =====")
        print("Nama Kasir\t: " + str(order["ksr"]))
        print("Nama Pelanggan\t: " + str(order["plg"]))
        print(20*"-")
        print("Ayam Goreng\t: " + str(order["ag"]))
        print("Ayam Bakar\t: " + str(order["ab"]))
        print("Ayam Madu\t: " + str(order["am"]))
        if ask_drink =="y" :
            print("Es Teh\t\t: " + str(order["et"]))
            print("Es Kopi\t\t: " + str(order["ek"]))
            print("Es Soda\t\t: " + str(order["es"]))
        print("Member\t\t: " + str(order["mbr"]))
        status_order = str(input("Masukkan status order (take away/dine-in) ?\t: "))
        
        #kalkulasi
        sub_harga = ((ayam_goreng*15000)+(ayam_bakar*18500)+(ayam_madu*20000)+(teh*4000)+(kopi*5000)+(soda*10000))
        print(f"Subtotal harga\t: Rp {sub_harga}")
        
        jumlah_item = (ayam_bakar+ayam_goreng+ayam_madu+soda+kopi+teh)
        #diskon member
        if member.lower() == "gold" :
            sub_harga*=0.85
        if member.lower() == "diamond" :
            sub_harga*=0.90
        if member.lower() == "silver" :
            sub_harga*=0.95
            
        #diskon jika lebih dari
        if sub_harga >= 500000 :
            sub_harga-=20000
        elif sub_harga >= 250000 :
            sub_harga-=10000
            
        #diskon status order
        if status_order == "take away" :
            sub_harga = sub_harga + (jumlah_item*2000)
        print(f"Total harga\t: Rp {sub_harga}")
        bayar = int(input("Bayar\t: "))
        kembalian = bayar-sub_harga
        print(f"Kembalian\t: Rp {kembalian}")

        text = "[Loading] ################\n"
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)  # Delay 0.1 detik
        # os.system("clear")
        init ()
        print(f"{Fore.GREEN}Data berhasil dimasukkan ke database{Style.RESET_ALL}")
        print("Terima Kasih telah Berkunjung!")
        
    case 0: 
        print("Terima kasih telah berkunjung!")

input()