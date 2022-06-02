#Square
myList = [5,4,3]

print(list(map(lambda item: item**2,myList)))


# Sort the Tuple

a = [(0,2), (4,3), (10,-1),(9,9)]
a.sort()   # sorting on first key
print(a)

a.sort(key=lambda x : x[1])  # sort based on second key

print(a)