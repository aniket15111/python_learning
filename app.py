weight=int(input("Enter weight: "))
unit=input("Enter L for lbs and K for killograms: ")
if(unit=='l' or unit == 'L'):
    print(f"your are {weight*0.45} Kg")
else:
    print(f"you are {weight*2.296} pounds")