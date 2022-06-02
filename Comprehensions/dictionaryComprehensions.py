simple_dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

my_dict = {key:value**2 for key, value in simple_dict.items()}
print(my_dict)

my_dict = {key:value**2 for key, value in simple_dict.items() if value % 2 ==0}
print(my_dict)