def fibo(num):
    num1=0
    num2=1
    for i in range(0,num):
        sum=num1+num2
        yield num1
        num1=num2
        num2=sum

a=fibo(10)
print(a.__next__())
print(a.__next__())