class ZipIterator:
    def __init__(self,a,b):
        self.a=a 
        self.b=b
        self.counter_a=0
        self.counter_b=0
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.a)==self.counter_a or len(self.b)==self.counter_b:
            raise StopIteration

        zipped=(self.a[self.counter_a],self.b[self.counter_b])
        self.counter_a+=1
        self.counter_b+=1
        return zipped
        

zi = ZipIterator([1, 2, 3], ["a", "b"])
for pair in zi:
    print(pair)
# (1, "a")
# (2, "b")
