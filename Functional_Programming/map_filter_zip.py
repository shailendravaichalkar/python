# map(), filter(), zip(), reduce()
from functools import reduce # this import only needs for import

myList = [1,2,3]
yourList = [10,15,25]
theirList = (23,45,66)

def multiply_by2(li):             # Pure Function
    newList = []
    for item in li:
        newList.append(item*2)
    return(newList)

print(multiply_by2(myList))

# map function
def multiply_by4(item):      
    return item * 4

print(list(map(multiply_by4, myList)))

# filter function
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, myList)))

# zip function
print(list(zip(yourList, myList)))  # collection into tuple 
print(list(zip(yourList, myList,theirList)))  # collection into tuple 