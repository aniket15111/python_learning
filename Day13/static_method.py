class Math:
    def __init__(self,a):
        self.a=a
    def display(self):
        return self.a
    @staticmethod
    def add(a,b):
        a=20
        return a+b
    
a=Math(10)
print(a.display())
print(Math.add(10,20))