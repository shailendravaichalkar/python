from time import time
from typing import Text
def performance(fn):
    def check_performance(*argv, **kwarg):
        t1 = time()
        result = fn(*argv, **kwarg)
        t2 = time()
        print(f'time taken is {t2 - t1} s')
        return result
    return check_performance


@performance
def fib(num):
    print("Using List")
    a = 0
    b = 1
    li = []
    for i in range(num):
        li.append(a)
        temp = a
        a = b
        b = temp + b    
    return li
  
print(fib(10))

@performance
def fib2(num):
    print("Using generators")
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b
        

for x in fib2(10):
    print(x)


