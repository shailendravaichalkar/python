#lists are mutable 
# (strings are immutable) 


li = [1, 2, 3]
li1 = [ 'a' , 'b' , 'c']
li2 = [1 , 3.5 , 'a' , 'abc']


# 1st Scenario 

list  = li
li[0] = 5  # We can do this because lists are mutable 
print(f"li is : {li}")
print(f"list is :{list}")

# 2nd Scenario 

list  = li[:]
li[0] = 1
print(f"li is : {li}")
print(f"list is :{list}")
li.append("1 More Done")
print(li)


