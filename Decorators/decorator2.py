def my_decorator(func): 
    def another_func(x):
        print("*****")
        func(x)
        print("*****")
    
    return another_func

@my_decorator
def greet(x):
    print(x)


greet("Hello")