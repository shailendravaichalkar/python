user = {
    'basket' : [1,2,3],
    'greet' : 'Hello',
    'age' : 22
}

print('basket' in user)
print('Hello' in user)

print('Hello' in user.keys())
print('Hello' in user.values())

print(user.items())

# user.clear() # clear the dictionary

user2 = user.copy();
print(user.clear())
print(user2)


print(user2.pop('age'))
print(user2)

print(user2.update({'greet' : 'Good Morning'}))
print(user2)

print(user2.update({'age' : 55}))
print(user2)