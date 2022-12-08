users = open("users.txt", "r")

#baca 1 line
#print(users.readline())

#baca semua lines
array = users.readlines()

#print(array)

#array loop 
index = 1
for user in array:
    print(f"{index} -- {user}")
    index += 1

users.close()



