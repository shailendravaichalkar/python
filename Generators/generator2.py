# Yeild do not create complete list in memory Instead it iterate 1 Item and pause
#pauses the function and comes back when 'next' called


def generators_func(num):
    for i in range(num):
        yield i

g = generators_func(10)
print(g)
print(next(g))
next(g)
next(g)
print(next(g))
next(g)
print(next(g))