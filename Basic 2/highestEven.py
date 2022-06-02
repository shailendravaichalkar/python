def highestEven(li):
    hightestEvenNumber = 0
    for item in li:
        if item % 2 == 0 and item > hightestEvenNumber:
            hightestEvenNumber = item
            
    return hightestEvenNumber


print(highestEven([10,2,3,6,7,8,9,11]))

print("Alternative way")

def highestEven2(li):
    even = []
    for item in li:
        if item % 2 == 0:
            even.append(item)
    return max(even)        
    
print(highestEven2([10,2,3,6,7,8,9,11]))

#hghgvbvb v fbfvdvfdvgnhgn vbkkdededxdcmnmn jnjlkmknjnjn 