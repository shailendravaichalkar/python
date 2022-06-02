username = input("Please enter username : ")
password = input("Please enter pasword : ")

passwordLength = len(password)
stars = '*' * passwordLength

print(f"Hey {username}, your password [{stars}] is {passwordLength} letters long")

print(f"Hey {username}, your password [{stars}] is {len(password)} letters long")
