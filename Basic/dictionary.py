# Dictionary
# it is unordered key value pair

dictionary = {
    'a' : 1,
    'b' : 3,
    'x' : 5
}

print(dictionary['b'])

print(dictionary)


dictionary = {
    'a' : [1,2,3],
    'b' : 'X',
    'x' : True
}

print(dictionary['a'][1])

myList = [
    {
        'a' : [1,2,3],
        'b' : 'X',
        'x' : True
    },
     {
        'a' : [4,5,6],
        'b' : 'Y',
        'x' : False
    },
]

print(myList[0]['a'][1])
print(myList)

#Dictionary Value can be in any data tpe
#Dictioray Key has to be immutable 
# Key has to be uniq else it will be overright the value

