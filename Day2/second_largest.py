a=[3,4,1,2,8,7,6,9,5,9,9,9,10]
max=a[0]
second_max=a[0]
for i in a:
    if max<i:
        second_max=max
        max=i
print(second_max)