kata = input("masukkan kata yang diinginkan : ")

# dipecah per huruf
kata_list = []
final = []
for kata in kata:
    kata_list.append(kata)

# bikin _
for kata in kata_list:
    final.append("_")

# game
for chance in range(9,-1,-1):

    # cetak kata
    for i in final:
        print(i,end=" ")

    if kata_list == final:
        print(f"\nSelamat! Anda berhasil menebak kata {kata}")
        print("Permainan tebak kata selesai.")
        exit()
    else:

        # input
        tebak = input("\nMasukkan tebakan huruf: ")
        index = 0

        # pengecekan
        if len(tebak) > 1:
            print("Tebakan tidak valid. Masukkan satu huruf.")
        else:
            if tebak in kata_list:
                print(f"Huruf {tebak} benar!")
                for kata in kata_list:
                    if kata == tebak:
                        final.pop(index)
                        final.insert(index,tebak)
                    index += 1
            else:
                print(f"Huruf {tebak} salah. Sisa poin {chance}")