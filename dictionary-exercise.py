numbers = input("Enter numbers: ")

numbers_mapping = {
        "1": "Satu",
        "2": "Dua",
        "3": "Tiga",
        "4": "Empat",
        "5": "Lima",

        }

output = ""

for n in numbers:
    count = numbers_mapping.get(n, "Invalid")

    output = output + count + " "

print(output)
