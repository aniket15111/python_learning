class Cycler:
    def __init__(self,a):
        self.a=a
        self.counter=0
        pass
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter>len(self.a)-1:
            self.counter=0
        term=self.a[self.counter]
        self.counter+=1
        return term


c = Cycler(['A', 'B', 'C'])
print(next(c))  # A
print(next(c))  # B
print(next(c))  # C
print(next(c))  # A
print(next(c))  # B