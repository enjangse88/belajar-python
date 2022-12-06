#!/usr/bin/python3


number = [1, 2, 3, 4, 5]

print(number)

number.append(12)
print(number)

#number.insert(posisi index, angka_yg_diinsert)
number.insert(2, 100)
print(number)

#delete isi list pada posisi index
number.pop(5)
print(number)

number.remove(3)
print(number)
