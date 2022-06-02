# We can do the same using comprehensions as well

someList = [ 'a', 'd' , 'c', 'a', 'c','t', 'o','d' ]
duplicateList = []
sortedList= sorted(someList)

for index, letter in enumerate(sortedList):
    if (sortedList[index - 1] == letter):
        duplicateList.append(letter)

print(duplicateList)


print("Another way of Doing Same")

for letters in someList:
    if (someList.count(letter) > 1) and (letter not in someList):
        duplicateList.append(letter)

print(duplicateList)