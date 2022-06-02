# List and Set Comprehensions are same
# insted of [] , we can make use of {} for sets. 
myList = []

for char in "Hello":
    myList.append(char)

print(myList)


myList2 = {char for char in "Hello"}
print(myList2)

myList3 = {num for num in range(0,10)}
print(myList3)

myList4 = {num**2 for num in range(0,10)}
print(myList4)

myList5 = {num**2 for num in range(0,10) if num % 2 == 0}
print(myList5)

