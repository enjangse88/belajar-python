try:
    level = input("level kamu: ")
    level = int(level)
    level = level / 0
    print(level)
except ZeroDivisionError:
    print("Error tidak bisa di bagi 0")
except ValueError:
    print("Yang kamu masukan bukan angka")
