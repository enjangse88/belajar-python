#add with statement so it could automtically close file 

import csv

with open("users.csv", "r") as users:
    users_csv = csv.reader(users, delimiter=",")

    for row in users_csv:
        print(f"Name : {row[0]}, Username : {row[1]}. Role : {row[-1]}")

