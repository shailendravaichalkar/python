def super_fun(*args):
    print(*args)
    print(args)
    return(sum(args))

super_fun(1,2,3,4)
print(super_fun(3,4,5))

#kwargs is keyword arguments

def superFun(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items

    return(sum(args) + total)

print(superFun(1,2,3, num1=5, num2=10))