def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
    


num=int(input("Enter a number to check if its prime or not: "))
check=is_prime(num)
if(check):
    print("prime")
else:
    print("not")
