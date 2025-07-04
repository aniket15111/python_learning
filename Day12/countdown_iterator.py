class iterator:
    def __init__(self,n):
        self.n=n
        pass
    def __iter__(self):
        return self
    def __next__(self):
        if self.n>0:
            a=self.n
            self.n=self.n-1
            return a
        else:
            raise StopIteration
        

i1=iterator(5)
for i in i1:
    print(i)
        
