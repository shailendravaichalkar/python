# Password Checker
# Shoub be 8 letters long
# It can have Letters or numbers
# It can only have Special charecters $%#@


import re

while True:
    input_pass = input("Please enter a password : ")
    pattern = re.compile(r"[A-Za-z0-9#%@]{8,}")

    is_Valid = pattern.fullmatch(input_pass)

    if (is_Valid): 
        print("Thats Valid Password")
        break
    else:
        print("Charecters used in password are not allowed!!")
        print("Please Try Again")
        continue