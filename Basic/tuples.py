#Tuples are immutable list
myTuple = (1,5,2,3,4,5)
# myTuple[0]='z'   is an error

user = {
    (1,2) : [1,2,3],
    'greet' : 'Hello'
}

print(user[(1,2)])

newTuple = myTuple[0:3]

a,b, *other = (1,2,3,4,5,6)

print(a)
print(myTuple.count(5))
print(myTuple.index(5))
print(len(myTuple))