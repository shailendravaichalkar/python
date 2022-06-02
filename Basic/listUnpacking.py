li = [1,2,3]
a,b,c = 1,2,3 #variable 
a,b,c =[1,2,3] # list unpacking
print(b)

a,b,c,*other =[1,2,3,4,5,6,7,8,9]
print(other)


a,b,c,*other,d =[1,2,3,4,5,6,7,8,9]
print(other)
print(d)
