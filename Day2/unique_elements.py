list1=[1,2,3,2,1,4,5,1,2,3,4,5]
unique=[]
for i in list1:
    if i in unique:
        continue
    else:
        unique.append(i)
print(unique)
