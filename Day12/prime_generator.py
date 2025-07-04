def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:          
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False  

    i = 5
    while i * i <= n:   
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6         
    return True


def primes_up_to(limit):
    for num in range(2, limit + 1):
        if is_prime(num):      
            yield num


a=primes_up_to(100)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())