list = [1,2,3,4,5]

#Adding
print(list)

list.append(100)
print(list)

list.insert(2,7)
print(list)

list.extend([9,10,11])
print(list)


#removing
list.pop()
print(list)

list.pop()
print(list)

list.pop(0)
print(list)

new_list = list.pop(1)      # Index
print(list)
print(new_list)

new_list = list.remove(100)   # Value
print(list)
print(new_list)

# Only Pop function returns Value.  VALUE which is pop'ed 
# All other functions returns None

list.clear()
print(list)





