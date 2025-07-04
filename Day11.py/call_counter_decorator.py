counter=0
def my_decorator(func):
    def fun():
        print("hello")
        return func()  
    return fun

@my_decorator
def counter_decorator():
    print("function called")
    global counter
    counter+=1



counter_decorator()
counter_decorator()
print(counter)