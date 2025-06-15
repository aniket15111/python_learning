try:
    # a=3/0
    # if(b):
    #     print("b")
    c=int(input("Enter a integer"))
except ZeroDivisionError:
    print("can not divide by 0")
except NameError:
    print("b is not defined")
except ValueError:
    print("Enter integer")