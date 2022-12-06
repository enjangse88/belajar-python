
#dictionary user
# user {key:value}

user = {
        "name": "Enjang Setiawan",
        "age": 30,
        "is_admin": True
        }

#function get, untuk mencegah muncul error
#error ini muncul karena key nya tidak ada
# name = user["name"]
name =  user.get("name")


print(name)
