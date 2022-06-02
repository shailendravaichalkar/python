list1 = ['a', 'x','c','c','d','d','d','e','f','a','e','b']

print(list1.index('d'))

print(list1.index('d',0,5)) # Value,Start searching for, End Searching for list1.index('d',0,2) is error

# print(list1.index('d',0,2)) #error

print('a' in list1)
print('x' in list1)

print(list1.count('c')) # Count of 'c' in the list1

print(sorted(list1)) # Returns the sorted list1 without modifying the actual list1
print(list1) # Original list1 is non intact 

list1.sort()  #Modifies the original list1
print(list1)

new_list1 = list1.copy()   # same as new_list1 = list1[:]   ; This copies the list1

list1.reverse()
print(list1)

print(list1[::-1]) #Reverse again

print("Range Ex 1")
print(list(range(1,100)))

print("Range Ex 2")
print(list(range(100)))

print("One last thing Join")

sentance = '!'
new_sentance = sentance.join(['Hi','my','name','is','JOJO'])
print(new_sentance)


new_sentance = ' & '.join(['Hi','my','name','is','JOJO'])
print(new_sentance)
