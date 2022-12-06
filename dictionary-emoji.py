#exercise dictionary emoji application

message = input(">>> ")

emoji_mapping = {
        "senyum": ":)",
        "manyun": ":(",
        "sedih": "T_T",
        "ketawa": ":))"

        }

words = message.split(" ")

output = ""
for w in words:
    output =  output + emoji_mapping.get(w, w) + " "

print(output)
