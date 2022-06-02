mySet = { 1,2,3,4,5,6}
yourSet = {4,5,6,7,8,9}

print(mySet.difference(yourSet))
print(yourSet.difference(mySet))

mySet.discard(5)
print(mySet)

mySet.difference_update(yourSet)
print(mySet)

print("Updated Sets again")
mySet = { 1,2,3,4,5,6}
yourSet = {4,5,6,7,8,9}

print("Doing Intersection")
print(mySet.intersection(yourSet))
print(mySet & yourSet) # Same as intersection

print(mySet.intersection_update(yourSet))


mySet = {1,2,3,4,5,6}
yourSet = {4,5,6,7,8,9}

print(mySet)
print(yourSet)
print(mySet.isdisjoint(yourSet))


mySet = {1,2,3}
yourSet = {4,5,6,7,8,9}

print(mySet)
print(yourSet)
print(mySet.isdisjoint(yourSet))

mySet = {1,2,3,4,5}
yourSet = {4,5,6,7,8,9}

print("Doing Union")
print(mySet.union(yourSet))
print(mySet | yourSet)

print("Subset and SuperSet")

mySet = {4,5}
yourSet = {4,5,6,7,8,9}

print(mySet.issubset(yourSet))
print(yourSet.issuperset(mySet))
