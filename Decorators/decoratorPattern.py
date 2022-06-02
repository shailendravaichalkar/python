#Decorator Pattern
def my_decorator(func): 
    def another_func(*args, **kwargs):
        print("*****")
        func(*args, **kwargs)
        print("*****")
    return another_func

@my_decorator
def greet(x):
    print(x)


greet("Hello")