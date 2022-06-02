user = {
    'basket' : [1,2,3],
    'greet' : 'Hello'
}

# print(user[age])  This is an error

print(user.get('age'))

print(user.get('age', 55))  # If age is 'None' then add default value 55 to it

user = {
    'basket' : [1,2,3],
    'greet' : 'Hello',
    'age' : 22
}

print(user.get('age', 55)) # Will print original Value


# Another way of creating dictionary

user2 = dict (name = 'Sha')
print(user2)