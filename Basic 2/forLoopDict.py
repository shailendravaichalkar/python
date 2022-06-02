dictionary = {
    'a' : 1,
    'b' : 3,
    'x' : 5
}

for item in dictionary:
    print(item)

for key in dictionary.keys():  # Same as above
    print(key)

for value in dictionary.values():
    print(value)

for item in dictionary.items():
    print(item)

for k,v in dictionary.items():
    print(f'Key = {k} and Value = {v}')