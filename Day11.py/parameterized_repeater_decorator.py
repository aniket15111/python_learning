def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
            return
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()