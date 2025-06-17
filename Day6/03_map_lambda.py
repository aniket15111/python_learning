nums = [1, 2, 3, 4, 5, 6, 7]
sq=list(map(lambda x:x*x,nums))
print(sq)

ev=list(filter(lambda x:x%2==0,nums))
print(ev)

from functools import reduce
sum=reduce(lambda x,y:x+y, nums)
print(sum)

nums1 = [3, 7, 2, 9, 4]
maximum = reduce(lambda x, y: x if x > y else y, nums1)
print(maximum)

sort=list(sorted(nums1))
print(sort)