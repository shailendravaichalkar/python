someList = [ 'a', 'd' , 'c', 'a', 'c','t', 'o','d' ]
duplicateList = list({char for char in someList if (someList.count(char) > 1)})
print(duplicateList)

