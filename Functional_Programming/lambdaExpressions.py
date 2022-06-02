from functools import reduce
myList = [1,2,3]

print(list(map(lambda item: item *2, myList)))

print(list(filter(lambda item: item % 2 != 0, myList)))

print(reduce(lambda acc, item: acc + item, myList))