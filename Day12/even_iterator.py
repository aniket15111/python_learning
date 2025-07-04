class even_iterator:
    def __init__(self,num):
        self.num=num
        self.n=0
        pass
    def __iter__(self):
        return self
    def __next__(self):
        while self.n <= self.num:
            if self.n%2==0 :
                even=self.n
                self.n+=1
                return even
            else:
                self.n+=1
        raise StopIteration
        
e=even_iterator(8)
for i in e:
    print(i)
        
