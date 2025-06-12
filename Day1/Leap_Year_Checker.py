# Note: A year is a leap year if "any one of " the following conditions are satisfied: 

# The year is multiple of 400.
# The year is a multiple of 4 and not a multiple of 100.
year=int(input("Enter year to check if its leap year or not: "))
if((year%4==0 and year%100!=0) or year%400==0):
    print("leap year")
else:
    print("not leap year")
