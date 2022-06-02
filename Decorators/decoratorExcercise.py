from time import time
def performance(fn):
    def check_performance(*argv, **kwarg):
        t1 = time()
        result = fn(*argv, **kwarg)
        t2 = time()
        print(f'time taken is {t2 - t1} s')
        return result
    return check_performance


@performance
def long_func():
    print(1)
    for i in range(100):
        i += i ** i

@performance
def long_func2():
    print(2)
    for i in list(range(1000)):
        i += i ** i

long_func()
long_func2()





