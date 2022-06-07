import os
import math

os.system('clear')

while True :
    print("--------------------------------------------")
    print("Selamat datang di program kalulator ini.")
    print("--------------------------------------------")
    print("Masukkan operasi yang ingin anda lakukan.")
    print(" - Penjumlahan   = 1")
    print(" - Pengurangan   = 2")
    print(" - Pembagian     = 3")
    print(" - Perkalian     = 4")
    print(" - Pangkat       = 5")
    print(" - Sin           = 6")
    print(" - Cos           = 7")
    print(" - Tan           = 8")
    print("--------------------------------------------")
    operasi = input("Masukkan angka pilihan kalian : ")

    jenis_operasi = [
            "Penjumlahan", 
            "Pengurangan", 
            "Pembagian",
            "Perkalian",
            "Pangkat",
            "Sin",
            "Cos",
            "Tan",
                    ]

    os.system('clear')

    print("Baik pilihan kalian adalah operasi", jenis_operasi[int(operasi) - 1])

    if operasi == '1' :
        num1 = input("  - Masukkan angka pertama    : ")
        num2 = input("  - Masukkan angka kedua      : ")
        print("Hasil penjumlahannya adalah   :", float(num1) + float(num2))

    elif operasi == '2' :
        num1 = input("  - Masukkan angka pertama    : ")
        num2 = input("  - Masukkan angka kedua      : ")
        print("Hasil pengurangannya adalah   :", float(num1) - float(num2))

    elif operasi == '3' :
        num1 = input("  - Masukkan angka pertama    : ")
        num2 = input("  - Masukkan angka kedua      : ")
        print("Hasil pembagiannya adalah     :", float(num1) / float(num2))

    elif operasi == '4' :
        num1 = input("  - Masukkan angka pertama    : ")
        num2 = input("  - Masukkan angka kedua      : ")
        print("Hasil perkaliannya adalah     :", float(num1) * float(num2))

    elif operasi == '5' :
        num1 = input("  - Masukkan angka yang akan dipangkatkan : ")
        num2 = input("  - Dipangkatkan sebanyak                 : ")
        
        hasil = 1
        for index in range(int(num2)) :
            hasil = int(hasil) * int(num1)

        print("Hasil perpangkatannya adalah                 :", hasil)

    elif operasi == '6' :
        num1 = input("  - Masukkan bilangannya      : ")
        print("Sin", num1, "adalah", math.sin(math.pi / (180 / int(num1))))

    elif operasi == '7' :
        num1 = input("  - Masukkan bilangannya      : ")
        print("Cos", num1, "adalah", math.cos(math.pi / (180 / int(num1))))

    elif operasi == '8' :
        num1 = input("  - Masukkan bilangannya      : ")
        print("Tan", num1, "adalah", math.tan(math.pi / (180 / int(num1))))

    yesno = input("\n--> Masih mau melakukan kalkulasi? (y/n) : ")

    if (yesno == 'n') or (yesno == 'N') :
        break

    os.system('clear')

os.system('clear')

print("Terima kasih telah menggunakan.")
print("Program ini dibuat oleh --> Gabriel Cesar Hutagalung <--")




