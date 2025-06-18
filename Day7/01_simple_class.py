class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    
    def walk(self,distance):
        print (f"{self.name} is walking {distance} meters")
        return
dog1=Dog("tommy","husky")
dog1.walk(100)
