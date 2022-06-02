def my_decorator(func): 
    def another_func():
        print("*****")
        func()
        print("*****")
    
    return another_func

@my_decorator
def greet():
    print("Hello")

greet()
