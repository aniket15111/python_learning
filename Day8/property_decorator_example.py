class Temperature:
    def __init__(self,celcius):
        self.celcius=celcius
    @property
    def fehrnhite(self):
        return (self.celcius*1.8)+32
    
temp1=Temperature(30)
print(temp1.fehrnhite)