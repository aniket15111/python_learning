class Math:
    def __init__(self,a):
        self.a=a
    def display(self):
        return self.a
    def change_variable(cls,a):
        cls.a=a
    
a=Math(10)
print(a.display())
a.change_variable(20)
print(a.display())