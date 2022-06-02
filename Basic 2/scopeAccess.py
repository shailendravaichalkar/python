total = 0

def count():
    global total  # To access global Variable 
    total += 1
    return total


count()
count()
print(count())

# nonlocal is used to access parental variable scope