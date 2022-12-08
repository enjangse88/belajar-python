

def halo_user():
    print("Halo user")


def halo_user_parameter(name):
    print(f"Halo {name}")


def halo_user_2parameter(name, level):
    print(f"Halo {name} - {level}")

#function with key word argument
def function_key_word_argument(total_belanja, ongkos_kirim, pajak):
  total_bayar = total_belanja + ongkos_kirim + pajak
  print(f"Total bayar", total_bayar)

#function with return value
def perkalian(a, b):
    hasil_perkalian =  a * b
    #return di kembalikan kepada value yang akan di output
    return hasil_perkalian


def perkalian2(a, b):
    return a * b

print("start")
halo_user()

halo_user_parameter("enjang")
print("========")
halo_user_parameter("SBY")
print("=-=-=-=-=-=-=")
halo_user_2parameter("enjang", 10)

print("Function with keyword argument")
function_key_word_argument(total_belanja=1000000, ongkos_kirim=25000, pajak=15000)

hasil_perkalian = perkalian(5, 10)
print(hasil_perkalian)

hasil_perkalian2 =  perkalian2(2, 10)
print(hasil_perkalian2)
