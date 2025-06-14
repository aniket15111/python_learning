def fibo(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return fibo(num-1)+fibo(num-2)


num=int(input("Enter a number to get its factorial"))
print(fibo(num))