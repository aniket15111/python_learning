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