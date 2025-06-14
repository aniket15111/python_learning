def sum_args(*args):
    print(sum(args))

def prod(*args):
    produ=1
    for i in args:
        produ*=i
    return produ

a=[1,2,3,4,5,6]
sum_args(*a)
print(prod(*a))