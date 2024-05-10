import os
uname = "surabaya"
npm = "1087"
utama = 0
buyer = 0
pendapatan = 0
cek = 0

while utama != 100:
    os.system("cls")
    print("""===== Toko Mas Karna =====
\nMenu Utama :
1. Login
2. Input Pembelian
3. Pembayaran
4. EXIT\n""")

    utama = int(input("Pilih menu : "))

    if utama == 1:
        # Login
        if cek == 0:
            for chance in range(2,-1,-1):
                os.system("cls")
                user = input("Masukkan Username: ")
                pasw = input("Masukkan Password: ")

                if user == uname and pasw == npm:
                    input(f"\nLogin berhasil. Welcome, {npm}!")
                    break
                else:
                    print("\n!! Username dan Password salah !!")
                    input(f"!! Kesempatan login : {chance}!!")
            else:
                input("!! Program berhenti !!")
                exit()
            cek = 1
        else :
            input("Anda sudah login!")

    elif utama == 2:
        # Menu
        if cek == 0:
            input("Silahkan login dahulu!")
        elif cek == 1 or cek == 3:
            # input pembelian
            os.system("cls")
            print("""===== Input Pembelian =====\n\nBrand :
1. Mito
2. Sharp""")
            menu = int(input("\nPilih brand: "))
            while menu not in [1,2]:
                print("Brand tidak tersedia!")
                menu = int(input("\nPilih brand: "))

            # Show menu
            if menu == 1:
                print("\nTipe oven :")
                print("""1. Mito MO-20
2. Mito MO-999
3. Mito MO-120\n""")
            elif menu == 2:
                print("\nTipe oven :")
                print("""1. Sharp EO-18L-W
2. Sharp EO-38BK
3. Sharp EO-28L-PK\n""")

            # tipe
            jenis = 0
            while jenis not in [1,2,3]:
                jenis = int(input("Masukkan tipe oven\t: "))
                if jenis not in [1,2,3]:
                    print("[!] Tipe tersebut tidak ada dalam daftar\n")

            # jumlah
            jumlah = int(input("Masukkan jumlah oven\t: "))
            while jumlah < 1:
                print("[!] Pembelian oven tidak boleh 0 atau minus\n")
                jumlah = int(input("Masukkan jumlah oven\t: "))

            # member
            member = input("Masukkan jenis member (gold/silver/none): ")
            while member not in ["gold", "silver", "none"]: 
                print(f"[!] Jenis member {member} tidak tersedia\n")
                member = input("Masukkan jenis member (gold/silver/none): ")

            input("\nInput pembelian sukses! Silahkan melakukan pembayaran")
            cek = 2
        else:
            input("Silahkan melakukan pembayaran!")

    elif utama == 3:
        if cek == 2:
        # Perhitungan
            if menu ==  1:
                if jenis == 1:
                    total = jumlah * 691000
                    bonus = "Mendapatkan bonus 1 loyang oven"
                    jenis_nama = "Mito MO-20"
                    
                    # cek member
                    if member.lower() == "gold":
                        total = total * 0.9
                    elif member.lower() == "silver":
                        total = total * 0.95
                    
                    # cek jumlah
                    if jumlah>7:
                        total = total-310000

                elif jenis == 2:
                    total = jumlah * 1910000
                    bonus = "Mendapatkan bonus 2 loyang oven dan 1 rak pemanggang"
                    jenis_nama = "Mito MO-999"

                    # cek member
                    if member.lower() == "gold":
                        total = total * 0.9
                    elif member.lower() == "silver":
                        total = total * 0.95
                    
                    # cek jumlah
                    if jumlah>7:
                        total = total-820000

                elif jenis == 3:
                    total = jumlah * 3390000
                    bonus = "Mendapatkan bonus 3 loyang oven, 2 rak pemanggang, dan garansi 12 bulan"
                    jenis_nama = "Mito MO-120"

                    # cek member
                    if member.lower() == "gold":
                        total = total * 0.9
                    elif member.lower() == "silver":
                        total = total * 0.95
                    
                    # cek jumlah
                    if jumlah>7:
                        total = total-1640000

            if menu == 2:
                if jenis == 1:
                    total = jumlah * 788000
                    bonus = "Mendapatkan bonus 2 loyang oven"
                    jenis_nama = "Sharp EO-18L-W"

                    # cek member
                    if member.lower() == "gold":
                        total = total * 0.9
                    elif member.lower() == "silver":
                        total = total * 0.95

                    # cek jumlah
                    if jumlah>7:
                        total = total-420000

                elif jenis == 2:
                    total = jumlah * 1290000
                    bonus = "Mendapatkan bonus 2 loyang oven dan 2 rak pemanggang"
                    jenis_nama = "Sharp EO-38BK"

                    # cek member
                    if member.lower() == "gold":
                        total = total * 0.9
                    elif member.lower() == "silver":
                        total = total * 0.95

                    # cek jumlah
                    if jumlah>7:
                        total = total-970000

                elif jenis == 3:
                    total = jumlah * 2320000
                    bonus = "Mendapatkan bonus 3 loyang oven, 3 rak pemanggang, dan garansi 9 bulan"
                    jenis_nama = "Sharp EO-28L-PK"

                    # cek member
                    if member.lower() == "gold":
                        total = total * 0.9
                    elif member.lower() == "silver":
                        total = total * 0.95

                    # cek jumlah
                    if jumlah>7:
                        total = total-1100000

            # output
            print("\n===== Data Pembelian =====")
            print(f"""Nama\t\t: {npm}
Tipe\t\t: {jenis_nama}
Jumlah\t\t: {jumlah} unit
Total Harga\t: Rp {total:.2f}""")
            print("-"*40)
            print(bonus)

            # pembayaran
            print("\n===== Pembayaran =====")
            print(f"Total Harga\t: Rp {total:.2f}")
            uang = int(input("Masukkan uang\t: Rp "))
            while uang < total:
                print("Uang Anda kurang!")
                uang = int(input("Masukkan uang\t: Rp "))

            print(f"Kembalian\t: Rp {uang-total:.2f}")
            input("\nPembayaran sukses! Terima kasih telah berbelanja")
            buyer += 1
            pendapatan += total
            cek = 3
        else:
            input("Silahkan input dahulu!")

    elif utama == 4:
        if cek == 2:
            input("Silahkan melakukan pembayaran!!")
        else:
            os.system("cls")
            print("Program selesai!")
            print("\n===== Laporan =====")
            print(f"Pelanggan\t: {buyer} orang")
            input(f"Pendapatan\t: Rp {pendapatan:.2f}")
            exit()
    else:
        input("Menu tidak tersedia!")