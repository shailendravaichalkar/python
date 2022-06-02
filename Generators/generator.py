# range is the generator
# Every generators are iterable


def generators_func(num):
    result = 0
    for i in range(num):
        result += i
    return (result)

print(generators_func(10))