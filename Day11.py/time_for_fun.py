import time as t
def decorator(func):
    def wrap():
        print(t.ctime())
        func()
        print(t.ctime())
        return
    return wrap

@decorator
def ti():
    t.sleep(5)
    print("here the function is called")


ti()