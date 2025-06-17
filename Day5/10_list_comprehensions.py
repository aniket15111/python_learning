a=[0,1,2,3,4,5,6,7,8,9]
square=[x*x for x in a]
print(square)

even=[x for x in a if x%2==0]
print(even)

b=["hi", "python", "world"]
words=[len(x) for x in b]
print(words)

c=["cat", "apple", "sky", "banana"]
words1=[x for x in c if len(x)<4]
print(words1)

d=[1, -2, 4, -5]
fil=[x if x>=0 else 0 for x in d ]
print(fil)

e=[[1, 2], [3, 4], [5]]
flat=[x for y  in e for x in y]
print(flat)

f=[(x,x*x) for x in range(1,6)]
print(f)

g=["apple", "banana", "orange", "grape"]
fil_vow=[x for x in g if x[0] in ['a','e','i','o','u']]
print(fil_vow)

h={x:x*x for x in range(1,6)}
print(h)

i = {'a': 1, 'b': 2, 'c': 3}
swap={x:y for y,x in i.items()}
print(swap)

s = "hello"
cout={x:s.count(x) for x in set(s)}
print(cout)