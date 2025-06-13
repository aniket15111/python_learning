fibo=[]
a=0
b=1
sum=0
num=int(input("Enter the number you want to get fibo sequence: "))
for i in range(num):
    fibo.append(a)
    sum=a+b
    a=b
    b=sum

print(fibo)