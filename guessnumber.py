#!/usr/bin/python3

trying = 0

secret_number = 7
limit = 3

while trying <= 3:
    number = int(input("Masukan angka: "))
    if secret_number == number:
        print("Selamat angkanya berhasil ketebak")
        break

    trying += 1
