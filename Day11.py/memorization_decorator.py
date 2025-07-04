def memorize(fun):
    cache={}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args]=fun(*args)
            return cache[args]
    return wrapper


@memorize
def fib(n):
    print(f"Calculating fib({n})")
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)



fib(5)



