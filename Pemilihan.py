import os
os.system("cls")

# If-Elif-Else Statement
while True:
    print("-"*10,"Konversi Nilai (If-Elif-Else)","-"*10)
    nilai = float(input("Masukkan nilai: "))

    if nilai >= 85:
        konversi = "A"
    elif nilai >= 80:
        konversi = "A-"
    elif nilai >=75:
        konversi = "B+"
    elif nilai >= 65:
        konversi = "B"
    elif nilai >= 60:
        konversi = "B-"
    elif nilai >= 55:
        konversi = "C+"
    elif nilai >= 40:
        konversi = "C"
    elif nilai >= 20:
        konversi = "D"
    else:
        konversi = "E"

    print(f"Konversi nilai : {konversi}")

    is_done = input("Konversi lagi (y/n)? ")
    if is_done == "n":
        break

print()

# Match-Case
while True:
    print("-"*10,"Konversi Nilai (Match-Case)","-"*10)
    nilai = float(input("Masukkan nilai: "))

    match nilai:
        case _ if nilai >= 85:
            konversi = "A"
        case _ if nilai >= 80:
            konversi = "A-"
        case _ if nilai >= 75:
            konversi = "B+"
        case _ if nilai >= 65:
            konversi = "B"
        case _ if nilai >= 60:
            konversi = "B-"
        case _ if nilai >= 55:
            konversi = "C+"
        case _ if nilai >= 40:
            konversi = "C"
        case _ if nilai >= 20:
            konversi = "D"
        case _:
            konversi = "E"

    print(f"Konversi nilai : {konversi}")

    is_done = input("Konversi lagi (y/n)? ")
    if is_done == "n":
        break