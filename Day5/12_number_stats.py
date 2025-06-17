from functools import reduce

a=[x for x in range (1,11)]
print(a)

double=list(map((lambda x: x*2),a))
print(double)

filt_even=list(filter(lambda x:x%2==0,a))
print(filt_even)

sum=reduce(lambda a,b:a+b,a)
print(sum)

names = ["aniket", "aastha", "sam"]
upper1=list(map(lambda x:x.upper(),names))
print(upper1)