def deco(fun):
    def new():
        print("Hello guys")
        fun()
        print("after the deco function")
        return fun()
        
    return new

@deco
def my_deco():
    print("here is the decorator called")

my_deco()